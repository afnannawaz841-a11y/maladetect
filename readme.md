## Malaria Disease Detection using Deep Learnig with Flask App
Malaria is a serious illness. The root cause are insects that infect humans through the bite of female Anopheles mosquitoes. It can be cured if the right steps are taken. Microscopic diagnoses are poorly maintained and rely heavily on microscopist ability and knowledge. It is very common for microscopes to operate alone in low-cost settings, without a solid system in place that can guarantee the conservation of their capabilities and thus curable quality. This results in wrong diagnostic conclusion in this area. Therefore, these facts have encouraged us to take up this building project. Diagnosis of Malaria through ML will not only benefit Health Care but also assist in our studies as Machine Learning is a new benefit to the industry.
This final year project, is based on Malaria Disease Detection using Deep Learning. We have used the MobileNet(150 CNN) and VGG16 for the classification of images. It is found out that 150CNN provides better accuracy than VGG16 in our project. The model is first trained on the training set then tested to classify the images as Parasitized or Uninfected. 
In this project design and implementation of the deep neural networks, and learning are presented. We have used an approach and an algorithm to detect Malaria using Deep Learning. We have implemented an Artificial Neural Network and Convolution Neural Network used for the classification of the infected and uninfected images of blood samples. 


## Installation of required software and libraries

1. Extract the downloaded project folder.

2. Follow the video and Install the TensorFlow and CUDA toolkit 
	https://youtu.be/b9e3J-NJ8TY
	
	Downgrade numpy to 1.26.4 by using the below command
	pip install numpy==1.26.4
	
3. Open the Anaconda prompt (search Anaconda prompt in the search menu) and change the directory to the project folder 
	example:
		cd path-of-project-folder
		
4. Switch to tf environment (which was created at the time of installing the TensorFlow) using the following command
	>>> conda activate tf
	
5. In tf environment, Install Requirements using the following command
	>>> pip install -r requirements.txt
	
	
## Steps to train the model after installing the software 

1. Open the Anaconda prompt (search Anaconda prompt in search menu) and change the directory to the project folder
	example:
		cd path-of-project-folder

2. Switch to tf environment (which was created at the time of installing the TensorFlow) using the following command
	>>> conda activate tf
	
3. Open Jupyter notebook using the following command

	>> jupyter notebook
	
4. Once the jupyter notebook is opened in the default browser, Open the Malaria_Detection.ipynb and run all the cells. Once the training is over the trained model will be saved in Models directory with file name CNN_model.h5 and VGG16_model.h5

## Run the Flask web app using the trained model

1. Open the Anaconda prompt (search Anaconda prompt in the search menu) and change the directory to the project folder
	example:
		cd path-of-project-folder

2. Switch to tf environment (which was created at the time of installing the TensoFlow) using the following command
	>>> conda activate tf
	
3. Run the following command to launch Flask Webapp
	>>> python app.py
	
4. The app is running at 
	http://127.0.0.1:5000
	
	
#### Download Dataset

Dataset Name: Malaria Cell Images Dataset

Dataset Link: https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/data

1. Once the dataset is downloaded, you will get an archive folder
2. Extract the archive folder
3. Copy and paste the two folders Parasitized and Uninfected into the dataset folder of the project directory.


## Tech Stack

**Language:** Python

**Libraries:** Keras, TensorFlow, NumPy

## Deep Learning Models Used

**For classification:** MobileNet(150CNN) and VGG16



## Authors


Afnan 
