# 🖼️ Image Detector

A simple web app that uses a pre-trained machine learning model to detect emotions from uploaded images.  
Built with **Streamlit**, **SQLite3**, and **Python**, it allows users to upload an image, get instant predictions, and view past results stored in a local database.  

---

## 🚀 Features

- Upload any image directly from your device  
- Get a real-time emotion prediction using a trained ML model  
- Displays the confidence percentage for each result  
- Saves all uploads and predictions automatically in an SQLite database  
- View past predictions directly on the app  
- Clean, white-themed interface for better readability  

---

## 🧠 Tech Stack

- **Python 3**  
- **Streamlit** – for the web interface  
- **SQLite3** – for local database storage  
- **TensorFlow / PyTorch** – for model inference  
- **Pillow (PIL)** – for image handling  

---

## 🗂️ Project Structure


📁 image_detector/
│
├── app.py # Main Streamlit app
├── database.py # Database setup and query functions
├── model.py # Model loading and prediction logic
├── requirements.txt # Dependencies list
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/image_detector.git
cd image_detector
```


2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py
Then open your browser and visit http://localhost:8501

💾 Database
Every prediction is automatically saved in a file named predictions.db.
You can view the stored data directly in the app or by using any SQLite viewer.

🧩 Example Usage
    1    Upload an image (JPEG, JPG, or PNG).
    2    The app processes it and predicts the emotion.
    3    See the detected emotion and its confidence level.
    4    Scroll down to view your saved predictions table.

🛠️ Future Improvements
    •    Allow multiple image categories beyond emotions
    •    Add login/user management
    •    Connect to a cloud database like Firebase or PostgreSQL
    •    Optimise model inference for faster predictions
    •    Option to download prediction reports
