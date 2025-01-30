# model.py
import cv2
import numpy as np
from tensorflow.keras.models import load_model # type: ignore

# Load the trained model
model = load_model('TumorDetectionFINAL.h5')

# Define the labels based on your model's classes
labels = ['glioma_tumour', 'meningioma_tumour', 'no_tumour', 'pituitary_tumour']

def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not loaded. Please check the file path.")
    
    # Resize and normalize the image
    img_resized = cv2.resize(img, (150, 150))
    img_array = np.array(img_resized)  # Normalizing the image
    img_array_expanded = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array_expanded

def predict_tumor(image_path):
    # Preprocess the image
    img_array = preprocess_image(image_path)
    
    # Predict
    prediction = model.predict(img_array)
    predicted_class_index = prediction.argmax()
    predicted_class_name = labels[predicted_class_index]
    predicted_class_probability = prediction[0][predicted_class_index]
    
    # Return the prediction details
    return {
        "Prediction Index": int(predicted_class_index),
        "Predicted Class Probability": float(predicted_class_probability),
        "Prediction": predicted_class_name
    }
