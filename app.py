from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import numpy as np
from PIL import Image
import os
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'dev-secret-change-me')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# Create DB
with app.app_context():
    db.create_all()


# Load ML models (map names shown in UI -> actual model files)
# Mapping: MobileNet (lightweight CNN) -> Models/CNN_model.h5, VGG16 -> Models/VGG16_model.h5
models = {}
models_loaded = False
try:
    # Import TensorFlow only when available; this avoids import errors on machines without TF installed
    import tensorflow as tf

    models = {
        'MobileNet': {'model': tf.keras.models.load_model(os.path.join(BASE_DIR, 'Models', 'CNN_model.h5')), 'input_size': (150, 150)},
        'VGG16': {'model': tf.keras.models.load_model(os.path.join(BASE_DIR, 'Models', 'VGG16_model.h5')), 'input_size': (125, 125)}
    }
    models_loaded = True
    print('Models loaded:', list(models.keys()))
except ImportError:
    print('TensorFlow is not installed in this environment. Predictions will be disabled until TensorFlow is installed.')
except Exception as e:
    print('Warning: Failed to load models at startup:', e)


def login_required(f):
    from functools import wraps

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id'):
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/methodology')
def methodology():
    return render_template('methodology.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            flash('Please fill out all fields.', 'danger')
            return render_template('register.html')

        existing = User.query.filter_by(email=email).first()
        if existing:
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('login'))

        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash(f'Welcome back, {user.name}!', 'success')
            next_page = request.args.get('next') or url_for('predict')
            return redirect(next_page)
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    result = None
    confidence = None
    image_url = None
    error_message = None

    if request.method == 'POST':
        file = request.files.get('file')
        selected_model = request.form.get('model')

        if not file or file.filename == '':
            error_message = 'Please select an image file.'
            flash(error_message, 'danger')
        elif selected_model not in models:
            error_message = 'Please select a valid model.'
            flash(error_message, 'danger')
        else:
            try:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                model_info = models[selected_model]
                model = model_info['model']
                input_size = model_info['input_size']

                img = Image.open(filepath).convert('RGB').resize(input_size)
                img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

                predictions = model.predict(img_array)
                confidence = round(np.max(predictions) * 100, 2)
                result = 'Uninfected' if np.argmax(predictions) == 1 else 'Parasitized'
                image_url = os.path.relpath(filepath, BASE_DIR).replace('\\\\', '/')
            except Exception as e:
                error_message = f'Error processing file: {str(e)}'
                flash(error_message, 'danger')

        # If request is AJAX (from fetch), return JSON response
        wants_json = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json
        if wants_json:
            if error_message:
                return { 'error': error_message }, 400
            return { 'result': result, 'confidence': confidence, 'image_url': image_url }, 200

    return render_template('predict.html', result=result, confidence=confidence, image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)
