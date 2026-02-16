# MalaDetect AI - Malaria Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An AI-powered web application for automated malaria detection in blood cell images using deep learning models. The system classifies microscopic blood smear images as either **Parasitized** (infected) or **Uninfected** (healthy) with high accuracy.

## 🎯 Project Overview

This Flask-based web application leverages convolutional neural networks to assist healthcare professionals in malaria diagnosis. The system provides instant analysis of blood cell images with confidence scores, supporting early detection and treatment decisions.

### Key Features

- **AI-Powered Detection**: Multiple deep learning models (MobileNet, VGG16, Custom CNN)
- **High Accuracy**: 92-93% accuracy on test datasets
- **User-Friendly Interface**: Drag-and-drop image upload with real-time preview
- **Model Comparison**: Performance metrics and detailed analysis
- **Secure Authentication**: User registration and session management
- **Responsive Design**: Modern UI with dark/light theme support

## 🏗️ System Architecture

```
Frontend (HTML/CSS/JS) → Flask Backend → TensorFlow Models → Prediction Results
```

### Models Implemented

| Model | Accuracy | Speed | Use Case |
|-------|----------|-------|----------|
| **MobileNet** | 93.1% | Very Fast | Production deployment |
| **Custom CNN** | 92.8% | Fast | Lightweight inference |
| **VGG16** | 85.2% | Slower | Research comparison |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- 4GB+ RAM recommended

### Installation

1. **Clone the repository**
```bash
gh repo clone afnannawaz841-a11y/maladetect
cd maladetect
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the application**
```
http://localhost:5000
```

## 📋 Dependencies

```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Bcrypt==1.0.1
TensorFlow==2.13.0
Pillow==10.0.0
NumPy==1.24.3
Werkzeug==2.3.7
```

## 🖥️ Usage

### For End Users

1. **Register/Login**: Create an account or sign in
2. **Upload Image**: Drag-and-drop or browse blood cell images
3. **Select Model**: Choose between MobileNet or VGG16
4. **Get Results**: View classification with confidence score

### For Developers

```python
# Load and use models directly
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load model
model = load_model('Models/CNN_model.h5')

# Preprocess image
img = Image.open('blood_cell.jpg').convert('RGB').resize((150, 150))
img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

# Predict
prediction = model.predict(img_array)
result = 'Uninfected' if np.argmax(prediction) == 1 else 'Parasitized'
```

## 📊 Performance Metrics

### Model Comparison

- **MobileNet**: 93.1% accuracy, 92.5% precision, 93.8% recall
- **Custom CNN**: 92.8% accuracy, 92.1% precision, 93.2% recall  
- **VGG16**: 85.2% accuracy, 85.4% precision, 86.8% recall

### Classification Results

- **True Positive Rate**: 93.2% (Parasitized detection)
- **True Negative Rate**: 92.8% (Uninfected detection)
- **False Positive Rate**: ~7%
- **False Negative Rate**: ~7%

## 🗂️ Project Structure

```
malaria-detection/
├── app.py                 # Flask application
├── Models/               # Trained model files
│   ├── CNN_model.h5
│   └── VGG16_model.h5
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   └── ...
├── static/              # CSS, JS, images
├── Dataset/             # Training data
├── requirements.txt     # Dependencies
└── README.md
```

## 🔧 Configuration

### Environment Variables

```bash
export FLASK_SECRET=your-secret-key
export FLASK_ENV=development  # or production
```

### Database Setup

The application uses SQLite by default. The database is automatically created on first run.

## 🧪 Testing

### Manual Testing

1. Use provided example images in `/static/images/`
2. Test with various image formats (JPG, PNG)
3. Verify model switching functionality

### Model Validation

Models were trained and validated on standard malaria datasets with 80/20 train-test split.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: NIH Malaria Dataset
- **Frameworks**: Flask, TensorFlow, Tailwind CSS
- **Models**: MobileNet, VGG16 architectures
- **Research**: Based on deep learning approaches for medical image classification

## 📞 Contact

- **Email**: team@maladetect.ai
- **Project**: AI Research Lab
- **Response Time**: 24-48 hours

## 🔮 Future Enhancements

- [ ] Real-time batch processing
- [ ] Mobile application development
- [ ] Integration with hospital systems
- [ ] Multi-language support
- [ ] Advanced model ensemble methods

---

**⚠️ Medical Disclaimer**: This system is for research and educational purposes. Always consult qualified medical professionals for clinical diagnosis and treatment decisions.
