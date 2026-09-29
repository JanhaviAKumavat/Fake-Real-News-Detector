from flask import Blueprint, render_template, session, redirect, url_for, flash

from utils.decorators import login_required
from database.database import get_db_connection



# ==========================================
# HISTORY BLUEPRINT
# ==========================================


history_bp = Blueprint(
    "history",
    __name__
)





# ==========================================
# USER PREDICTION HISTORY
# ==========================================


@history_bp.route("/history")
@login_required
def history():


    user_id = session.get(
        "user_id"
    )


    predictions = []



    try:


        connection = get_db_connection()


        cursor = connection.cursor(
            dictionary=True
        )



        query = """

        SELECT

            id,
            news_text,
            prediction,
            confidence,
            created_at

        FROM prediction_history

        WHERE user_id = %s

        ORDER BY created_at DESC

        """



        cursor.execute(
            query,
            (user_id,)
        )



        predictions = cursor.fetchall()



        cursor.close()

        connection.close()



    except Exception as e:


        print(
            "History Error:",
            e
        )


        flash(
            "Unable to load prediction history",
            "danger"
        )



    return render_template(
        "history.html",
        predictions=predictions
    )