import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ===============================
# Load Dataset
# ===============================

fake_news = pd.read_csv("model/Fake.csv")
real_news = pd.read_csv("model/True.csv")


# ===============================
# Add Labels
# Fake = 0
# Real = 1
# ===============================

fake_news["label"] = 0
real_news["label"] = 1


# ===============================
# Combine Dataset
# ===============================

data = pd.concat(
    [fake_news, real_news],
    axis=0
)


# Shuffle Data

data = data.sample(
    frac=1,
    random_state=42
)


# Reset Index

data.reset_index(
    drop=True,
    inplace=True
)


# ===============================
# Select Text Column
# ===============================

data["text"] = (
    data["title"].fillna("")
    + " "
    + data["text"].fillna("")
)


X = data["text"]
y = data["label"]


# ===============================
# Split Dataset
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ===============================
# TF-IDF Vectorizer
# ===============================

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7
)


X_train_vector = vectorizer.fit_transform(
    X_train
)

X_test_vector = vectorizer.transform(
    X_test
)


# ===============================
# Train Model
# ===============================

model = LogisticRegression(
    max_iter=1000
)


model.fit(
    X_train_vector,
    y_train
)


# ===============================
# Model Accuracy
# ===============================

prediction = model.predict(
    X_test_vector
)


accuracy = accuracy_score(
    y_test,
    prediction
)


print(
    "Model Accuracy:",
    accuracy * 100,
    "%"
)


# ===============================
# Save Model
# ===============================

joblib.dump(
    model,
    "model/model.pkl"
)


joblib.dump(
    vectorizer,
    "model/vectorizer.pkl"
)


print(
    "Model and Vectorizer Saved Successfully!"
)