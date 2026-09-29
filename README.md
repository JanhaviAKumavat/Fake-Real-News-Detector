# 📰 Fake Real News Detector Using AI & Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.0-black)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange)
![Database](https://img.shields.io/badge/MySQL-9.1.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)


## 📌 Project Overview

Fake Real News Detector is an Artificial Intelligence based web application that identifies whether a given news article is **REAL NEWS** or **FAKE NEWS** using Machine Learning and Natural Language Processing (NLP).

The system analyzes the text content of news articles and predicts authenticity using a trained ML model.

The application provides:

- User Registration & Login
- Secure Authentication
- News Prediction
- Confidence Score
- Prediction History
- User Profile Management
- Admin Dashboard
- Contact Management


---

# 🚀 Features


## 👤 User Module

✅ User Registration  
✅ User Login / Logout  
✅ Password Encryption  
✅ Profile Management  
✅ View Prediction History  
✅ Real-Time News Detection  


## 🤖 AI News Detection Module

✅ Text Based News Analysis  
✅ NLP Text Cleaning  
✅ TF-IDF Feature Extraction  
✅ Machine Learning Prediction  
✅ Fake / Real Classification  
✅ Confidence Percentage  


## 🛠 Admin Module

✅ Admin Login  
✅ Dashboard Analytics  
✅ Manage Users  
✅ View Predictions  
✅ View Contact Messages  


---

# 🧠 Machine Learning Workflow


```
News Text Input

        ↓

Text Cleaning

        ↓

Tokenization

        ↓

TF-IDF Vectorization

        ↓

Machine Learning Model

        ↓

Prediction

        ↓

REAL NEWS / FAKE NEWS

        ↓

Confidence Score
```


---

# 🏗️ Project Architecture


```
Fake_News_Detector/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── model/
│   ├── train_model.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   ├── Fake.csv
│   └── True.csv
│
├── database/
│   ├── database.py
│   ├── schema.sql
│   ├── user_queries.py
│   ├── admin_queries.py
│   └── detector_queries.py
│
├── routes/
│   ├── home.py
│   ├── auth.py
│   ├── detector.py
│   ├── profile.py
│   ├── history.py
│   ├── contact.py
│   └── admin.py
│
├── utils/
│   ├── helper.py
│   ├── predictor.py
│   ├── validators.py
│   ├── decorators.py
│   ├── admin_required.py
│   ├── login_required.py
│   ├── news_api.py
│   └── logger.py
│
├── templates/
│   │
│   ├── layout.html
│   │
│   ├── includes/
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── loader.html
│   │   └── flash_message.html
│   │
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── detector.html
│   ├── contact.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   └── history.html
│
├── admin/
│   │
│   ├── templates/
│   │   │
│   │   ├── admin_layout.html
│   │   │
│   │   ├── includes/
│   │   │   ├── sidebar.html
│   │   │   ├── topbar.html
│   │   │   ├── footer.html
│   │   │   └── flash_message.html
│   │   │
│   │   ├── dashboard.html
│   │   ├── users.html
│   │   ├── user_details.html
│   │   ├── predictions.html
│   │   ├── prediction_details.html
│   │   ├── messages.html
│   │   ├── reports.html
│   │   ├── analytics.html
│   │   ├── settings.html
│   │   ├── profile.html
│   │   ├── logs.html
│   │   ├── activity.html
│   │   └── error404.html
│   │
│   ├── static/
│   │   │
│   │   ├── css/
│   │   │   ├── admin_layout.css
│   │   │   ├── sidebar.css
│   │   │   ├── topbar.css
│   │   │   ├── dashboard.css
│   │   │   ├── users.css
│   │   │   ├── predictions.css
│   │   │   ├── messages.css
│   │   │   ├── reports.css
│   │   │   ├── analytics.css
│   │   │   ├── settings.css
│   │   │   └── responsive.css
│   │   │
│   │   ├── js/
│   │   │   ├── sidebar.js
│   │   │   ├── dashboard.js
│   │   │   ├── users.js
│   │   │   ├── predictions.js
│   │   │   ├── charts.js
│   │   │   └── notifications.js
│   │   │
│   │   └── images/
│   │
│   └── README.md
│
├── static/
│   │
│   ├── css/
│   │   ├── style.css
│   │   ├── navbar.css
│   │   ├── footer.css
│   │   ├── home.css
│   │   ├── about.css
│   │   ├── services.css
│   │   ├── detector.css
│   │   ├── contact.css
│   │   ├── profile.css
│   │   ├── login.css
│   │   ├── register.css
│   │   └── responsive.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── navbar.js
│   │   ├── detector.js
│   │   ├── validation.js
│   │   └── animation.js
│   │
│   └── images/
│
├── instance/
│
├── logs/
│   ├── app.log
│   └── error.log
│
└── tests/
    ├── test_auth.py
    ├── test_detector.py
    ├── test_database.py
    └── test_admin.py


```


---

# 💻 Technology Stack


## Frontend

| Technology | Version |
|------------|---------|
| HTML5 | Latest |
| CSS3 | Latest |
| JavaScript | ES6 |
| Bootstrap | 5.x |


## Backend

| Technology | Version |
|------------|---------|
| Python | 3.12 |
| Flask | 3.1.0 |
| Jinja2 | 3.1.4 |
| Werkzeug | 3.1.3 |


## Machine Learning

| Library | Version |
|---------|---------|
| Scikit-learn | 1.6.0 |
| Pandas | 2.2.3 |
| NumPy | 2.1.3 |
| Joblib | 1.4.2 |


## Database

| Technology | Version |
|------------|---------|
| MySQL | 9.1.0 |
| mysql-connector-python | 9.1.0 |


---

# 📂 Dataset

Dataset used:

**Fake and Real News Dataset**

Contains:

- Fake News Articles
- Real News Articles


Files:

```
Fake.csv
True.csv
```


Dataset is used for training and testing the Machine Learning model.


---

# ⚙️ Installation Guide


## 1. Clone Repository


```bash
git clone https://github.com/JanhaviAKumavat/Fake_News_Detector.git
```


## 2. Navigate Project Folder


```bash
cd Fake_News_Detector
```


## 3. Create Virtual Environment


```bash
python -m venv venv
```


Activate environment:


Windows:

```bash
venv\Scripts\activate
```


Linux/Mac:

```bash
source venv/bin/activate
```


---

# 📦 Install Dependencies


```bash
pip install -r requirements.txt
```


---

# 🗄️ Database Configuration


Create MySQL Database:


```sql
CREATE DATABASE fake_news_detector;
```


Import database tables:


```sql
SOURCE database/schema.sql;
```


Update database credentials in:


```
config.py
```


Example:


```python
MYSQL_HOST="localhost"
MYSQL_USER="root"
MYSQL_PASSWORD="your_password"
MYSQL_DATABASE="fake_news_detector"
```


---

# 🤖 Train Machine Learning Model


Navigate:


```bash
cd model
```


Run:


```bash
python train_model.py
```


Generated files:


```
model.pkl

vectorizer.pkl
```


---

# ▶️ Run Application


From project root:


```bash
python app.py
```


Application runs on:


```
http://127.0.0.1:5000
```


---

# 🔐 Default Admin Login


```
Email:
admin@fakenews.com


Password:
admin123
```


---

# 📰 How To Use


1. Register a new account

2. Login into system

3. Enter news article text

4. Click "Detect News"

5. System predicts:


```
REAL NEWS

or

FAKE NEWS
```


with confidence percentage.


---

# 📊 Machine Learning Model


The system uses:


### TF-IDF Vectorizer

Converts text data into numerical features.


### Classification Model

Trained model:

```
Machine Learning Classifier
```


Prediction output:


```
0  → Fake News

1  → Real News
```


---

# 🔒 Security Features


✔ Password Hashing  
✔ Login Required Detection  
✔ Session Management  
✔ Input Validation  
✔ Protected Admin Routes  


---

# 📸 Application Screenshots


Add screenshots here:


```
screenshots/

├── home.png

├── login.png

├── detector.png

└── admin_dashboard.png

```


---

# 🔮 Future Enhancements


- Google News Verification
- Fact Checking API Integration
- Multi-language Detection
- Deep Learning Model Integration
- Browser Extension
- AI Chatbot Assistant
- Voice Based News Detection


---

# 👩‍💻 Developer


**Janhavi Kumavat**

AI & Machine Learning Project


GitHub:

https://github.com/JanhaviAKumavat


---

# 📜 License


This project is licensed under the MIT License.
