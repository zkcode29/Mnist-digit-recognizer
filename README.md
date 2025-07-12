# MNIST Digit Recognizer 🧠

A simple web application built with Python, Scikit-learn, and Gradio that can recognize handwritten digits (0-9) from an uploaded image or a drawing canvas.

This project was built as part of the ARCH Technologies Machine Learning Internship. It demonstrates the complete lifecycle of a machine learning project, from training a model to deploying it in an interactive web interface.

---

### ✨ Features

*   **Real-time Prediction:** Draw a digit on the canvas and get an instant prediction.
*   **Image Upload:** Upload your own image of a handwritten digit for classification.
*   **Preprocessing Pipeline:** Images are automatically resized, normalized, and processed to match the model's training data format.
*   **Robust Model:** Uses a `RandomForestClassifier` trained on the famous MNIST dataset for a good balance of speed and accuracy.

---

### 🛠️ Technologies Used

*   **Python:** The core programming language.
*   **Scikit-learn:** For training and building the machine learning model.
*   **Gradio:** To create the fast and easy-to-use web interface.
*   **NumPy:** For numerical operations and image manipulation.
*   **Joblib:** For saving and loading the trained Scikit-learn model.

---

### 🚀 How to Run This Project Locally

To run this application on your own machine, follow these steps:

**1. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/mnist-digit-recognizer.git
cd mnist-digit-recognizer
