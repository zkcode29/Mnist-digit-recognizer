import os
import joblib
import numpy as np
import cv2
import gradio as gr

# Step 1: Download model from Google Drive if not exists
import gdown
model_path = "rf_clf_model.pkl"
drive_id = "1wi4aNfZLMPtqgXcGns_w6HhHSVFM8Pkp"
if not os.path.exists(model_path):
    url = f"https://drive.google.com/uc?id={drive_id}"
    gdown.download(url, model_path, quiet=False)

# Step 2: Load the model
model = joblib.load(model_path)

# Step 3: Define prediction function
def predict_digit(image):
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (28, 28))
    image = 255 - image
    image = image / 255.0
    image = image.reshape(1, -1)
    return int(model.predict(image)[0])

# Step 4: Launch Gradio interface
gr.Interface(
    fn=predict_digit,
    inputs=gr.Image(type="numpy", image_mode="L"),
    outputs="label",
    title="🧠 MNIST Digit Recognizer",
    description="Upload or draw a digit (0–9)."
).launch()
