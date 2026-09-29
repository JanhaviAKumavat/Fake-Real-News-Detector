from flask import (
    Blueprint,
    render_template,
    session,
    flash
)

from utils.decorators import login_required
from database.database import get_db_connection


# ==========================================
# PROFILE BLUEPRINT
# ==========================================

profile_bp = Blueprint(
    "profile",
    __name__
)


# ==========================================
# PROFILE PAGE
# ==========================================

@profile_bp.route("/profile")
@login_required
def profile():

    user_id = session.get("user_id")

    user = None

    stats = {
        "total": 0,
        "fake": 0,
        "real": 0
    }

    recent_predictions = []

    try:

        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        # =====================================
        # USER DETAILS
        # =====================================

        cursor.execute(
            """
            SELECT
                id,
                full_name,
                email,
                created_at
            FROM users
            WHERE id=%s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        # =====================================
        # TOTAL DETECTIONS
        # =====================================

        cursor.execute(
            """
            SELECT COUNT(*) AS total_count
            FROM prediction_history
            WHERE user_id=%s
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if row:
            stats["total"] = row["total_count"]

        # =====================================
        # FAKE NEWS COUNT
        # =====================================

        cursor.execute(
            """
            SELECT COUNT(*) AS fake_count
            FROM prediction_history
            WHERE user_id=%s
            AND prediction='Fake News'
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if row:
            stats["fake"] = row["fake_count"]

        # =====================================
        # REAL NEWS COUNT
        # =====================================

        cursor.execute(
            """
            SELECT COUNT(*) AS real_count
            FROM prediction_history
            WHERE user_id=%s
            AND prediction='Real News'
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if row:
            stats["real"] = row["real_count"]

        # =====================================
        # RECENT PREDICTIONS
        # =====================================

        cursor.execute(
            """
            SELECT
                news_text,
                prediction,
                confidence,
                created_at
            FROM prediction_history
            WHERE user_id=%s
            ORDER BY created_at DESC
            LIMIT 5
            """,
            (user_id,)
        )

        recent_predictions = cursor.fetchall()

        print("Recent Predictions:")
        print(recent_predictions)

        cursor.close()
        connection.close()

    except Exception as e:

        print("Profile Error:", e)

        flash(
            "Unable to load profile data",
            "danger"
        )

    return render_template(
        "profile.html",
        user=user,
        stats=stats,
        recent_predictions=recent_predictions
    )