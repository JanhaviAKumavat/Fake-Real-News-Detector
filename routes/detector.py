from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash
)


from utils.decorators import login_required
from utils.predictor import predict_news
from database.database import get_db_connection




detector_bp = Blueprint(
    "detector",
    __name__
)





# ==========================================
# DETECTOR PAGE
# ==========================================


@detector_bp.route(
    "/detector",
    methods=["GET","POST"]
)

@login_required
def detector():


    result = None

    confidence = None

    news_text = ""





    if request.method == "POST":


        news_text = request.form.get(
            "news_text"
        )



        if not news_text or news_text.strip()=="":


            flash(
                "Please enter news text",
                "warning"
            )


            return redirect(
                url_for(
                    "detector.detector"
                )
            )






        try:



            # ==========================
            # AI PREDICTION
            # ==========================


            prediction = predict_news(
                news_text
            )



            result = prediction.get(
                "result"
            )


            confidence = prediction.get(
                "confidence"
            )






            # ==========================
            # CHECK MODEL RESULT
            # ==========================


            if result not in [
                "Fake News",
                "Real News"
            ]:


                flash(
                    "AI model failed to predict.",
                    "danger"
                )


                return render_template(

                    "detector.html",

                    result=None,

                    confidence=None,

                    news_text=news_text

                )









            # ==========================
            # SAVE HISTORY
            # ==========================


            user_id = session.get(
                "user_id"
            )



            connection = get_db_connection()


            cursor = connection.cursor()



            cursor.execute(

                """
                INSERT INTO prediction_history
                (
                    user_id,
                    news_text,
                    prediction,
                    confidence
                )

                VALUES
                (%s,%s,%s,%s)

                """,

                (

                    user_id,

                    news_text,

                    result,

                    confidence

                )

            )



            connection.commit()



            cursor.close()

            connection.close()





        except Exception as e:


            print(
                "Detector Error:",
                e
            )


            flash(
                "Prediction failed.",
                "danger"
            )







    return render_template(

        "detector.html",

        result=result,

        confidence=confidence,

        news_text=news_text

    )