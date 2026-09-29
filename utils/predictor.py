import joblib

from config import Config

from utils.helper import (
    clean_text,
    format_result,
    calculate_confidence
)



# ==================================
# Load ML Model
# ==================================

def load_model():

    try:

        model = joblib.load(
            Config.MODEL_PATH
        )


        vectorizer = joblib.load(
            Config.VECTORIZER_PATH
        )


        print("ML Model Loaded Successfully")


        return model, vectorizer



    except Exception as e:


        print(
            "Model Loading Error:",
            e
        )


        return None, None





# Load model

model, vectorizer = load_model()





# ==================================
# Predict News
# ==================================

def predict_news(news_text):


    if not news_text:


        return {

            "result":"Invalid Input",

            "confidence":0

        }




    if model is None or vectorizer is None:


        return {

            "result":"Model Error",

            "confidence":0

        }





    try:


        cleaned_text = clean_text(
            news_text
        )



        vector = vectorizer.transform(
            [cleaned_text]
        )



        prediction = model.predict(
            vector
        )[0]



        probability = model.predict_proba(
            vector
        )[0]



        result = format_result(
            prediction
        )



        confidence = calculate_confidence(
            probability
        )



        return {

            "result":result,

            "confidence":confidence

        }





    except Exception as e:


        print(
            "Prediction Error:",
            e
        )


        return {

            "result":"Error",

            "confidence":0

        }