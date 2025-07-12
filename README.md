
# MNIST Digit Recognizer

A simple web application built with **Python**, **Scikit-learn**, and **Gradio** that recognizes handwritten digits (0–9) from either an uploaded image or drawing canvas.

---

##  Features

* **Real-time Prediction** – Draw a digit and get an instant result.
*  **Image Upload** – Upload a handwritten digit image for classification.
*  **Preprocessing Pipeline** – Automatically resizes, inverts, normalizes input.
*  **Robust Model** – Uses `RandomForestClassifier` trained on the MNIST dataset for 95%+ accuracy.

---

##  Technologies Used

| Tool         | Purpose                           |
| ------------ | --------------------------------- |
| Python       | Main programming language         |
| Scikit-learn | Training and using ML models      |
| Gradio       | Web interface for predictions     |
| NumPy        | Matrix & array operations         |
| OpenCV       | Image processing                  |
| Joblib       | Saving/loading model file         |
| gdown        | Downloads model from Google Drive |

---

##  Model Download

> The trained model (`rf_clf_model.pkl`) is too large for GitHub (130MB)
> It is **automatically downloaded** from Google Drive the first time you run the app.

📎 [Learn more → MODEL\_SOURCE.md](./MODEL_SOURCE.md)

---

##  How to Run This Project Locally

###  1. Clone the Repository

git clone https://github.com/zkcode29/Mnist-digit-recognizer.git


cd Mnist-digit-recognizer


###  2. Install Required Libraries

```bash
pip install -r requirements.txt
```

###  3. Run the Application

```bash
python app.py
```

 The model will automatically download the first time using `gdown`.

---


##  Files Included

| File               | Description                            |
| ------------------ | -------------------------------------- |
| `app.py`           | Main Python app that loads model + UI  |
| `requirements.txt` | Python libraries needed                |
| `MODEL_SOURCE.md`  | Info about model download & Drive link |
| `README.md`        | Project instructions (this file)       |

---

##  Author

**Izaz Khan**
Bachelors in Artificial Intelligence


---


