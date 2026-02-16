# 🚀 SentientAI – Feedback Sentiment Analyzer

SentientAI is a full-stack Django web application that analyzes user feedback and classifies it into **Positive**, **Negative**, or **Neutral** sentiments using a machine learning model.

---

## 📌 Project Overview

This project combines **Web Development + Machine Learning** to create an AI-powered feedback analysis system.

**Workflow:**

User Input → Django Backend → ML Model → Sentiment Prediction → UI Display

---

## 🛠 Tech Stack

**Backend**
- Django
- Python

**Frontend**
- HTML
- CSS
- JavaScript

**Machine Learning**
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression

**Model Handling**
- Joblib

---

## ✨ Features

✔ Real-time sentiment prediction  
✔ Custom trained ML model  
✔ Clean and modern UI  
✔ Full-stack architecture  
✔ Lightweight & fast inference  

---

## ⚙ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SentientAI.git
cd SentientAI

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Django Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000

🤖 Machine Learning Model

The sentiment classifier was trained using:

TF-IDF Vectorization

Logistic Regression

Multiple labeled sentiment datasets

The trained model is serialized using Joblib for fast predictions