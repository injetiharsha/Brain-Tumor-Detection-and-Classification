# Brain Tumour Detection using CNN

## Overview
This project is a **Brain Tumour Detection System** that leverages a **Convolutional Neural Network (CNN)** to classify brain MRI images. It offers an intuitive **Tkinter GUI** for both single image detection and batch processing (folder mode). The system preprocesses images, predicts the tumour type, and displays the results in real-time.

## Features
- **Single Image Classification:** Upload a single MRI image and get a prediction of the tumour type.
- **Batch Image Processing:** Select a folder containing multiple MRI images and view predictions for all images in a grid layout.
- **CNN-based Classification:** The pre-trained model classifies images into the following four categories:
  - **Glioma Tumour:** A type of tumour originating from glial cells.
  - **Meningioma Tumour:** A tumour that forms in the meninges surrounding the brain.
  - **Pituitary Tumour:** A tumour occurring in the pituitary gland.
  - **No Tumour:** Indicates the absence of a tumour.
- **Interactive GUI:** Built using Tkinter, the interface displays images and predictions with a scrollable layout for batch processing.

## Datasets
- **Training Dataset:**  
  The model was trained on the dataset available at [Kaggle: Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset). This dataset provided a diverse set of MRI images across different tumour types, which helped in developing a robust model.
  
- **Testing Dataset:**  
  The testing dataset was obtained from [Kaggle: Brain MRI Images for Brain Tumor Detection](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection). This dataset was used to validate the model’s performance on unseen data.

## Technology Stack
- **Python 3.7+**
- **TensorFlow/Keras:** For loading and running the CNN model.
- **OpenCV:** For image processing.
- **PIL (Pillow):** For image manipulation within the GUI.
- **Tkinter:** For building the graphical user interface.
- **NumPy:** For numerical operations and handling image data.

## Model Details
The CNN model is saved as `TumorDetectionFINAL.h5` and is designed to classify MRI images into the following categories:
- **Glioma Tumour**
- **Meningioma Tumour**
- **Pituitary Tumour**
- **No Tumour**

### Prediction Workflow
1. **Image Preprocessing:**  
   - The selected image is loaded using OpenCV.
   - It is resized to 150x150 pixels and normalized.
   - A batch dimension is added to suit the model's input requirements.
   
2. **Model Prediction:**  
   - The preprocessed image is fed into the CNN model.
   - The model outputs class probabilities.
   - The class with the highest probability is selected as the prediction.
   
3. **Result Display:**  
   - For single image mode, the prediction (tumour type and probability) is displayed alongside the image.
   - For folder mode, images and their corresponding predictions are arranged in a grid with a scrollable interface.
  
4. 
Future Enhancements
Increase Model Accuracy:
Explore additional data augmentation and incorporate more diverse datasets to improve the model's robustness.

Enhanced GUI Features:
Add functionalities such as real-time webcam integration or more detailed visual analytics.

Web Deployment:
Consider developing a web application using frameworks like Flask or Django for broader accessibility.

Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

6. 
## Installation & Setup
### Prerequisites
Ensure you have Python 3.7 or higher installed. Install the required dependencies using pip:
```bash
pip install tensorflow opencv-python pillow numpy

## Running the Application
##For Single Image Detection:
file.py
##For Batch Folder Processing:
folder.py


