from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    flash,
    send_file,
    request,
    jsonify
)

from utils.validators import (
    validate_email,
    validate_name,
    validate_password,
    validate_password_match
)

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils.decorators import admin_required
from utils.validators import validate_email, validate_name, validate_password

from database.database import get_db_connection
import json





# ==================================================
# ADMIN BLUEPRINT
# ==================================================


admin_bp = Blueprint(

    "admin",

    __name__,

    url_prefix="/admin",

    template_folder="../admin/templates",

    static_folder="../admin/static",

    static_url_path="static"

)









# ==================================================
# PDF BUILDER HELPER
# ==================================================


def build_reports_pdf(reports, title="Detection Reports"):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(letter)
    )

    styles = getSampleStyleSheet()

    elements = [Paragraph(title, styles["Title"])]

    data = [["User", "News Text", "Prediction", "Confidence", "Date"]]

    for r in reports:

        news_preview = r["news_text"]

        if len(news_preview) > 70:
            news_preview = news_preview[:70] + "..."

        data.append([
            r["full_name"],
            news_preview,
            r["prediction"],
            f'{r["confidence"]}%',
            str(r["created_at"])
        ])

    table = Table(
        data,
        repeatRows=1,
        colWidths=[100, 260, 90, 80, 120]
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(table)

    doc.build(elements)

    buffer.seek(0)

    return buffer









# ==================================================
# DASHBOARD
# ==================================================


@admin_bp.route("/dashboard")
@admin_required
def dashboard():


    stats = {

        "users":0,

        "predictions":0,

        "fake":0,

        "real":0

    }


    recent_activity=[]



    try:


        connection = get_db_connection()


        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """
            SELECT COUNT(*) AS total
            FROM users
            WHERE role='user'
            """

        )


        stats["users"] = cursor.fetchone()["total"]





        cursor.execute(

            """
            SELECT COUNT(*) AS total
            FROM prediction_history
            """

        )


        stats["predictions"] = cursor.fetchone()["total"]





        cursor.execute(

            """
            SELECT COUNT(*) AS total
            FROM prediction_history
            WHERE prediction='Fake News'
            """

        )


        stats["fake"] = cursor.fetchone()["total"]





        cursor.execute(

            """
            SELECT COUNT(*) AS total
            FROM prediction_history
            WHERE prediction='Real News'
            """

        )


        stats["real"] = cursor.fetchone()["total"]






        cursor.execute(

            """

            SELECT

            users.full_name,

            prediction_history.prediction,

            prediction_history.confidence,

            prediction_history.created_at


            FROM prediction_history


            JOIN users


            ON prediction_history.user_id = users.id


            ORDER BY prediction_history.created_at DESC


            LIMIT 10

            """

        )


        recent_activity = cursor.fetchall()



        cursor.close()

        connection.close()



    except Exception as e:


        print(
            "Dashboard Error:",
            e
        )


        flash(

            "Unable to load dashboard data",

            "danger"

        )





    return render_template(

        "dashboard.html",

        stats=stats,

        recent_activity=recent_activity

    )









# ==================================================
# USERS MANAGEMENT
# ==================================================


@admin_bp.route("/users")
@admin_required
def users():


    users=[]



    try:


        connection=get_db_connection()


        cursor=connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """

            SELECT

            id,

            full_name,

            email,

            role,

            created_at


            FROM users


            ORDER BY created_at DESC


            """

        )


        users=cursor.fetchall()



        cursor.close()

        connection.close()



    except Exception as e:


        print(
            "Users Error:",
            e
        )





    return render_template(

        "users.html",

        users=users

    )









# ==================================================
# ADD USER
# ==================================================


@admin_bp.route("/users/add", methods=["POST"])
@admin_required
def add_user():


    full_name = request.form.get("full_name")

    email = request.form.get("email")

    password = request.form.get("password")

    role = request.form.get("role", "user")



    if not validate_name(full_name):

        flash("Enter a valid name.", "danger")

        return redirect(url_for("admin.users"))



    if not validate_email(email):

        flash("Enter a valid email.", "danger")

        return redirect(url_for("admin.users"))



    if not validate_password(password):

        flash("Password must contain uppercase, lowercase and number.", "danger")

        return redirect(url_for("admin.users"))



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            "SELECT id FROM users WHERE email=%s",

            (email,)

        )



        if cursor.fetchone():

            flash("Email already registered.", "danger")

            cursor.close()

            connection.close()

            return redirect(url_for("admin.users"))



        cursor.execute(

            """
            INSERT INTO users (full_name, email, password, role)
            VALUES (%s, %s, %s, %s)
            """,

            (full_name, email, password, role)

        )



        connection.commit()

        cursor.close()

        connection.close()



        flash("User added successfully.", "success")



    except Exception as e:


        print("Add User Error:", e)

        flash("Unable to add user.", "danger")



    return redirect(url_for("admin.users"))









# ==================================================
# UPDATE USER
# ==================================================


@admin_bp.route("/users/<int:user_id>/update", methods=["POST"])
@admin_required
def update_user(user_id):


    full_name = request.form.get("full_name")

    email = request.form.get("email")

    role = request.form.get("role")



    if not validate_name(full_name):

        flash("Enter a valid name.", "danger")

        return redirect(url_for("admin.users"))



    if not validate_email(email):

        flash("Enter a valid email.", "danger")

        return redirect(url_for("admin.users"))



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            "SELECT id FROM users WHERE email=%s AND id!=%s",

            (email, user_id)

        )



        if cursor.fetchone():

            flash("That email is already used by another account.", "danger")

            cursor.close()

            connection.close()

            return redirect(url_for("admin.users"))



        cursor.execute(

            """
            UPDATE users
            SET full_name=%s, email=%s, role=%s
            WHERE id=%s
            """,

            (full_name, email, role, user_id)

        )



        connection.commit()

        cursor.close()

        connection.close()



        if session.get("user_id") == user_id:

            session["user_name"] = full_name

            session["email"] = email

            session["role"] = role



        flash("User updated successfully.", "success")



    except Exception as e:


        print("Update User Error:", e)

        flash("Unable to update user.", "danger")



    return redirect(url_for("admin.users"))









# ==================================================
# DELETE USER
# ==================================================


@admin_bp.route("/users/<int:user_id>/delete", methods=["POST"])
@admin_required
def delete_user(user_id):


    if session.get("user_id") == user_id:

        flash("You can't delete your own account while logged in.", "danger")

        return redirect(url_for("admin.users"))



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            "DELETE FROM users WHERE id=%s",

            (user_id,)

        )



        connection.commit()

        cursor.close()

        connection.close()



        flash("User deleted successfully.", "success")



    except Exception as e:


        print("Delete User Error:", e)

        flash("Unable to delete user. They may have related prediction records.", "danger")



    return redirect(url_for("admin.users"))









# ==================================================
# PREDICTIONS
# ==================================================


@admin_bp.route("/predictions")
@admin_required
def predictions():


    predictions=[]



    try:


        connection=get_db_connection()


        cursor=connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """

            SELECT

            prediction_history.*,

            users.full_name


            FROM prediction_history


            JOIN users


            ON prediction_history.user_id = users.id


            ORDER BY created_at DESC


            """

        )


        predictions=cursor.fetchall()



        cursor.close()

        connection.close()



    except Exception as e:


        print(
            "Prediction Error:",
            e
        )





    return render_template(

        "predictions.html",

        predictions=predictions

    )









# ==================================================
# CONTACT MESSAGES
# ==================================================


@admin_bp.route("/messages")
@admin_required
def messages():


    messages=[]



    try:


        connection=get_db_connection()


        cursor=connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """

            SELECT *

            FROM contact_messages

            ORDER BY created_at DESC


            """

        )


        messages=cursor.fetchall()



        cursor.close()

        connection.close()



    except Exception as e:


        print(
            "Messages Error:",
            e
        )





    return render_template(

        "messages.html",

        messages=messages

    )
# ==================================================
# MARK MESSAGE AS READ
# ==================================================


@admin_bp.route("/messages/<int:message_id>/mark-read", methods=["POST"])
@admin_required
def mark_message_read(message_id):


    try:


        connection = get_db_connection()

        cursor = connection.cursor()



        cursor.execute(

            """
            UPDATE contact_messages
            SET status='Read'
            WHERE id=%s AND status='New'
            """,

            (message_id,)

        )



        connection.commit()

        cursor.close()

        connection.close()



    except Exception as e:


        print("Mark Read Error:", e)



    return jsonify({"success": True})









# ==================================================
# MARK MESSAGE AS REPLIED
# ==================================================


@admin_bp.route("/messages/<int:message_id>/mark-replied", methods=["POST"])
@admin_required
def mark_message_replied(message_id):


    try:


        connection = get_db_connection()

        cursor = connection.cursor()



        cursor.execute(

            """
            UPDATE contact_messages
            SET status='Replied'
            WHERE id=%s
            """,

            (message_id,)

        )



        connection.commit()

        cursor.close()

        connection.close()



    except Exception as e:


        print("Mark Replied Error:", e)



    return jsonify({"success": True})









# ==================================================
# DELETE MESSAGE
# ==================================================


@admin_bp.route("/messages/<int:message_id>/delete", methods=["POST"])
@admin_required
def delete_message(message_id):


    try:


        connection = get_db_connection()

        cursor = connection.cursor()



        cursor.execute(

            "DELETE FROM contact_messages WHERE id=%s",

            (message_id,)

        )



        connection.commit()

        cursor.close()

        connection.close()



        flash("Message deleted successfully.", "success")



    except Exception as e:


        print("Delete Message Error:", e)

        flash("Unable to delete message.", "danger")



    return redirect(url_for("admin.messages"))









# ==================================================
# REPORTS PAGE
# ==================================================


@admin_bp.route("/reports")
@admin_required
def reports():


    reports=[]



    try:


        connection=get_db_connection()


        cursor=connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """

            SELECT


            prediction_history.id,

            prediction_history.user_id,

            prediction_history.news_text,

            prediction_history.prediction,

            prediction_history.confidence,

            prediction_history.created_at,

            users.full_name



            FROM prediction_history



            JOIN users



            ON prediction_history.user_id = users.id



            ORDER BY prediction_history.created_at DESC


            """

        )


        reports=cursor.fetchall()



        cursor.close()

        connection.close()



    except Exception as e:


        print(
            "Reports Error:",
            e
        )





    return render_template(

        "reports.html",

        reports=reports

    )









# ==================================================
# EXPORT ALL REPORTS (PDF)
# ==================================================


@admin_bp.route("/export-reports")
@admin_required
def export_reports():


    try:


        connection=get_db_connection()


        cursor=connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """

            SELECT


            users.full_name,

            prediction_history.news_text,

            prediction_history.prediction,

            prediction_history.confidence,

            prediction_history.created_at



            FROM prediction_history



            JOIN users



            ON prediction_history.user_id = users.id



            ORDER BY prediction_history.created_at DESC


            """

        )



        reports=cursor.fetchall()



        cursor.close()

        connection.close()



        pdf_buffer = build_reports_pdf(

            reports,

            title="All Detection Reports"

        )



        return send_file(

            pdf_buffer,

            mimetype="application/pdf",

            as_attachment=True,

            download_name="fake_news_all_reports.pdf"

        )





    except Exception as e:


        print(

            "Export Reports Error:",

            e

        )


        return "Unable to export report"









# ==================================================
# EXPORT SPECIFIC USER REPORT (PDF)
# ==================================================


@admin_bp.route("/export-user-report/<int:user_id>")
@admin_required
def export_user_report(user_id):


    try:


        connection=get_db_connection()


        cursor=connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """

            SELECT


            users.full_name,

            prediction_history.news_text,

            prediction_history.prediction,

            prediction_history.confidence,

            prediction_history.created_at



            FROM prediction_history



            JOIN users



            ON prediction_history.user_id = users.id



            WHERE users.id=%s



            ORDER BY prediction_history.created_at DESC


            """,

            (user_id,)

        )



        reports=cursor.fetchall()



        cursor.close()

        connection.close()



        username = reports[0]["full_name"] if reports else "User"



        pdf_buffer = build_reports_pdf(

            reports,

            title=f"{username} — Detection Report"

        )



        return send_file(

            pdf_buffer,

            mimetype="application/pdf",

            as_attachment=True,

            download_name=f"{username}_report.pdf"

        )





    except Exception as e:


        print(

            "User Export Error:",

            e

        )


        return "Unable to export user report"









# ==================================================
# ANALYTICS
# ==================================================


# @admin_bp.route("/analytics")
# @admin_required
# def analytics():


#     return render_template(

#         "analytics.html"

#     )

# ==================================================
# ANALYTICS
# ==================================================


def get_analytics_data():
    """Shared query logic used by both the analytics page and the PDF export."""

    stats = {

        "total":0,

        "fake":0,

        "real":0,

        "fake_percentage":0,

        "real_percentage":0

    }


    daily_labels = []

    daily_counts = []



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            "SELECT COUNT(*) AS total FROM prediction_history"

        )


        stats["total"] = cursor.fetchone()["total"]




        cursor.execute(

            """
            SELECT COUNT(*) AS total
            FROM prediction_history
            WHERE prediction='Fake News'
            """

        )


        stats["fake"] = cursor.fetchone()["total"]




        cursor.execute(

            """
            SELECT COUNT(*) AS total
            FROM prediction_history
            WHERE prediction='Real News'
            """

        )


        stats["real"] = cursor.fetchone()["total"]




        if stats["total"] > 0:


            stats["fake_percentage"] = round(

                (stats["fake"] / stats["total"]) * 100, 1

            )


            stats["real_percentage"] = round(

                (stats["real"] / stats["total"]) * 100, 1

            )




        # Daily predictions for the last 7 days


        cursor.execute(

            """
            SELECT
            DATE(created_at) AS day,
            COUNT(*) AS total
            FROM prediction_history
            WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 6 DAY)
            GROUP BY DATE(created_at)
            ORDER BY day ASC
            """

        )


        rows = cursor.fetchall()



        counts_by_day = {

            str(row["day"]): row["total"] for row in rows

        }



        from datetime import date, timedelta


        today = date.today()



        for i in range(6, -1, -1):


            day = today - timedelta(days=i)

            day_str = str(day)



            daily_labels.append(

                day.strftime("%a %d")

            )


            daily_counts.append(

                counts_by_day.get(day_str, 0)

            )




        cursor.close()

        connection.close()



    except Exception as e:


        print("Analytics Error:", e)



    return stats, daily_labels, daily_counts




@admin_bp.route("/analytics")
@admin_required
def analytics():


    stats, daily_labels, daily_counts = get_analytics_data()   # 👈 must unpack into 3 variables


    return render_template(

        "analytics.html",

        stats=stats,

        daily_labels=json.dumps(daily_labels),

        daily_counts=json.dumps(daily_counts)

    )









# ==================================================
# EXPORT ANALYTICS REPORT (PDF)
# ==================================================


@admin_bp.route("/analytics/export-report")
@admin_required
def export_analytics_report():


    stats, daily_labels, daily_counts = get_analytics_data()



    pdf_buffer = build_analytics_pdf(

        stats,

        daily_labels,

        daily_counts

    )



    return send_file(

        pdf_buffer,

        mimetype="application/pdf",

        as_attachment=True,

        download_name="analytics_report.pdf"

    )


# ==================================================
# ANALYTICS PDF BUILDER HELPER
# ==================================================


def build_analytics_pdf(stats, daily_labels, daily_counts):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = [
        Paragraph("AI Analytics Report", styles["Title"]),
        Paragraph("Summary", styles["Heading2"])
    ]

    summary_data = [
        ["Metric", "Value"],
        ["Total Predictions", str(stats["total"])],
        ["Fake News Detected", f'{stats["fake"]} ({stats["fake_percentage"]}%)'],
        ["Real News Verified", f'{stats["real"]} ({stats["real_percentage"]}%)'],
        ["AI Model Accuracy", "98%"],
    ]

    summary_table = Table(summary_data, colWidths=[220, 220])

    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.append(summary_table)
    elements.append(Paragraph("<br/><br/>Predictions - Last 7 Days", styles["Heading2"]))

    daily_data = [["Date", "Predictions"]]

    for label, count in zip(daily_labels, daily_counts):
        daily_data.append([label, str(count)])

    daily_table = Table(daily_data, colWidths=[220, 220])

    daily_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(daily_table)

    doc.build(elements)

    buffer.seek(0)

    return buffer






# ==================================================
# SETTINGS
# ==================================================


@admin_bp.route("/settings")
@admin_required
def settings():


    return render_template(

        "settings.html"

    )









# ==================================================
# ADMIN PROFILE
# ==================================================


# @admin_bp.route("/profile")
# @admin_required
# def profile():


#     return render_template(

#         "profile.html"

#     )

# ==================================================
# ADMIN PROFILE
# ==================================================


@admin_bp.route("/profile")
@admin_required
def profile():


    user = None



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            """
            SELECT
            id,
            full_name,
            email,
            role,
            created_at
            FROM users
            WHERE id=%s
            """,

            (session.get("user_id"),)

        )


        user = cursor.fetchone()



        cursor.close()

        connection.close()



    except Exception as e:


        print("Admin Profile Error:", e)

        flash("Unable to load profile data", "danger")



    return render_template(

        "admin_profile.html",

        user=user

    )









# ==================================================
# UPDATE ADMIN PROFILE (name / email)
# ==================================================


@admin_bp.route("/profile/update", methods=["POST"])
@admin_required
def update_admin_profile():


    full_name = request.form.get("full_name")

    email = request.form.get("email")

    admin_id = session.get("user_id")



    if not validate_name(full_name):

        flash("Enter a valid name.", "danger")

        return redirect(url_for("admin.profile"))



    if not validate_email(email):

        flash("Enter a valid email.", "danger")

        return redirect(url_for("admin.profile"))



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            "SELECT id FROM users WHERE email=%s AND id!=%s",

            (email, admin_id)

        )



        if cursor.fetchone():

            flash("That email is already used by another account.", "danger")

            cursor.close()

            connection.close()

            return redirect(url_for("admin.profile"))



        cursor.execute(

            """
            UPDATE users
            SET full_name=%s, email=%s
            WHERE id=%s
            """,

            (full_name, email, admin_id)

        )



        connection.commit()

        cursor.close()

        connection.close()



        session["user_name"] = full_name

        session["email"] = email



        flash("Profile updated successfully.", "success")



    except Exception as e:


        print("Update Admin Profile Error:", e)

        flash("Unable to update profile.", "danger")



    return redirect(url_for("admin.profile"))









# ==================================================
# CHANGE ADMIN PASSWORD
# ==================================================


@admin_bp.route("/profile/change-password", methods=["POST"])
@admin_required
def change_admin_password():


    current_password = request.form.get("current_password")

    new_password = request.form.get("new_password")

    confirm_password = request.form.get("confirm_password")

    admin_id = session.get("user_id")



    if not validate_password(new_password):

        flash("New password must be at least 8 characters and contain uppercase, lowercase, and a number.", "danger")

        return redirect(url_for("admin.profile"))



    if not validate_password_match(new_password, confirm_password):

        flash("New password and confirm password do not match.", "danger")

        return redirect(url_for("admin.profile"))



    try:


        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )



        cursor.execute(

            "SELECT password FROM users WHERE id=%s",

            (admin_id,)

        )


        row = cursor.fetchone()



        if not row or row["password"] != current_password:

            flash("Current password is incorrect.", "danger")

            cursor.close()

            connection.close()

            return redirect(url_for("admin.profile"))



        cursor.execute(

            "UPDATE users SET password=%s WHERE id=%s",

            (new_password, admin_id)

        )



        connection.commit()

        cursor.close()

        connection.close()



        flash("Password changed successfully.", "success")



    except Exception as e:


        print("Change Admin Password Error:", e)

        flash("Unable to change password.", "danger")



    return redirect(url_for("admin.profile"))









# ==================================================
# LOGS
# ==================================================


@admin_bp.route("/logs")
@admin_required
def logs():


    return render_template(

        "logs.html"

    )









# ==================================================
# ACTIVITY
# ==================================================


@admin_bp.route("/activity")
@admin_required
def activity():


    activities=[]



    return render_template(

        "activity.html",

        activities=activities,

        total_users=0,

        total_predictions=0,

        total_logins=0

    )









# ==================================================
# ERROR 404
# ==================================================


@admin_bp.app_errorhandler(404)
def admin_404(error):


    return render_template(

        "error404.html"

    ),404