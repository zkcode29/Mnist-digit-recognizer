#  Where is the Model File?

This project uses a trained **RandomForestClassifier** model for digit recognition.  
The model file (`rf_clf_model.pkl`) is too large to upload directly to GitHub.

---

##  Model Location
The model is stored on **Google Drive** and automatically downloaded by the app when it runs.

### 🔗 Direct Download Link:
[Click here to view/download the model from Google Drive](https://drive.google.com/file/d/1wi4aNfZLMPtqgXcGns_w6HhHSVFM8Pkp/view?usp=drive_link)

---

## How It Works in Code

When you run `app.py`, it will:
1. Check if `rf_clf_model.pkl` exists.
2. If not, it downloads the file using `gdown` from the link above.
3. Then it loads the model and starts the digit recognition app.

 No need to manually download anything!

---

##  For Beginners

If you're not familiar with `.pkl` files or model loading, don’t worry:
- This is a **pre-trained machine learning model**
- It’s loaded behind the scenes automatically when you run the app
