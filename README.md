# 🏠 House Price Recommendation System (Divar-like)

A machine learning-based recommendation system for predicting and suggesting house prices, inspired by platforms like Divar.

This project uses data science and machine learning techniques to analyze housing data, predict prices, and recommend similar listings.

---

## 🚀 Features

* 🔍 House price prediction using Machine Learning models
* 📊 Data preprocessing and feature engineering pipeline
* 🤖 Recommendation system for similar property listings
* ⚡ Fast and lightweight implementation
* 🧠 Scalable ML architecture
* 🐳 Docker-ready (for reproducible deployment)

---

## 🧠 Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy

---

## 📂 Project Structure

```text
Divar-Recom-system/
│
├── main.py
├── model.py
├── data/
│   └── dataset.csv
├── utils.py
├── requirements.txt
└── README.md
```

---

## 🔗 Clone the Repository

```bash
git clone https://github.com/Milad-Noori/Divar-Recom-system.git
cd Divar-Recom-system
```

---

## ⚙️ Installation

### 1. Create virtual environment (optional)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

After running, the system will:

* Load dataset
* Train ML model
* Predict house prices
* Recommend similar listings

---

## 📊 Machine Learning Pipeline

```text
Raw Housing Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Train/Test Split
    ↓
Model Training (Scikit-learn)
    ↓
Prediction + Recommendation Engine
```

---

## 🧪 Example Output

```text
Predicted Price: 2,500,000 USD
Similar Houses:
- House A (2,450,000 USD)
- House B (2,600,000 USD)
- House C (2,480,000 USD)
```

---

## 🐳 Docker (Optional)

```bash
docker build -t house-recommender .
docker run house-recommender
```

---

## 🚀 Future Improvements

* Deep Learning-based recommendation system
* Real-time API (FastAPI / Flask)
* Web dashboard (React / Streamlit)
* Geo-based recommendations
* Advanced ranking system

---

## 👨‍💻 Author

**Milad Noori**

* GitHub: https://github.com/Milad-Noori
* Machine Learning & AI Developer
