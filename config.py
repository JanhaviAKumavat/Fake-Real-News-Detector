import os


class Config:

    # ==========================
    # Flask Configuration
    # ==========================

    SECRET_KEY = "fake_news_detector_secret_key"

    # Session Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


    # ==========================
    # MySQL Configuration
    # ==========================

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DB = "fake_news_detector"

    # Return database rows as dictionary
    MYSQL_CURSORCLASS = "DictCursor"


    # ==========================
    # Upload Configuration
    # ==========================

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads"
    )


    # ==========================
    # Machine Learning Model Path
    # ==========================

    MODEL_PATH = os.path.join(
        BASE_DIR,
        "model",
        "model.pkl"
    )

    VECTORIZER_PATH = os.path.join(
        BASE_DIR,
        "model",
        "vectorizer.pkl"
    )