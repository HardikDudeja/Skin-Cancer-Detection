# Skin-Cancer-Detection
# IDEA :

The main idea of this project is to create a tool such that it takes an image of a mole as input and, through various manipulations and trained ML models, predict whether a mole can be malign or not.

Being the most common type of cancer, skin cancer detection is pretty costly, which causes many problems in its early detection. If detected early, skin cancer is almost 99 percent curable. In our project, we tend to cater to this need to detect skin cancer through image analysis of mole and predicting whether it is malign or benign

# Development Process and Stages :

Our project is based on constructing a CNN model that can predict that a specific mole can be malignant or not.

Data abstraction: To train our CNN model, we used a set of images from the International Skin Imaging Collaboration: Melanoma Project. The photos were taken from different sets, including UDA1, UDA2, MSK1, MSK2. for training purposes, 1043 benign images were used along with 717 malign images. For testing purposes, a total of 115 benign pictures along with 77 malign photos were used.

# Preprocessing: 

The preprocessing step for data analysis was divided into two significant stages for each image.

i) visual inspection to segregate images with low quality or with no credible information.

ii) image resizing with the included transformation of each image to 128 by 128 by 3.


# CNN Model : 

We developed a simple CNN model from scratch and trained it using different data sets and evaluated each image whether it is malignant or benign. The accuracy of this model came out at 94%, which proved to be just enough for our cancer prediction.

i) Data Amplification : Images were scaled and rotated to avoid noise and remove unnecessary data.

ii)Transferred Learning :- Using a pre-trained network construct some supplementary layer at the end for better performance of our model. 

# Model Evaluation : 
To evaluate the outcomes of our model we have used ROC curves and evaluated the area under these curves using AUC score. We maintained a balance between false positive rate and true positive rate that ultimately increased our models precision and accuracy. Using the classification reports we have displayed our CNN model’s precision and accuracy. To determine the performance of classification models we have also used a confusion matrix.

# Tools Used : 

TensorFlow

Keras

Python

Matplotlib Library

Scikit - Learn

Django, HTML5, CSS

	
# Results

We created a website that allows the user to upload an image of a mole and runs our CNN model in the backend with help of python to predict whether the image uploaded by the user is malignant or benign. All these tasks run in real time to predict accurate and precise reports for skin cancer detection. 

# WEBSITE

![Alt text](img1.png?raw=true "Title")
![Alt text](img3.png?raw=true "Title")
![Alt text](img4.png?raw=true "Title")

# WORKING

![Alt text](img5.png?raw=true "Title")
![Alt text](img6.png?raw=true "Title")

# MODELS AND THEIR ACCURACY

![Alt text](img2.png?raw=true "Title")
![Alt text](img7.png?raw=true "Title")
![Alt text](img8.png?raw=true "Title")


The accuracy of our model came out just above 94% which we feel is sufficient, but surely it can be improved.

