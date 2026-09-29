from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
)

from database.database import get_db_connection

from utils.validators import (
    validate_name,
    validate_email,
    validate_required
)


contact_bp = Blueprint(
    "contact",
    __name__
)


# ==================================================
# CONTACT PAGE
# ==================================================

@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # ----------------------------
        # Validation
        # ----------------------------

        if not validate_required(
            name,
            email,
            message
        ):

            flash(
                "All fields are required.",
                "danger"
            )

            return redirect(
                url_for("contact.contact")
            )



        if not validate_name(name):

            flash(
                "Please enter a valid name.",
                "danger"
            )

            return redirect(
                url_for("contact.contact")
            )



        if not validate_email(email):

            flash(
                "Please enter a valid email address.",
                "danger"
            )

            return redirect(
                url_for("contact.contact")
            )



        # ----------------------------
        # Save Message
        # ----------------------------

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT INTO contact_messages
            (
                name,
                email,
                message
            )

            VALUES
            (%s,%s,%s)
            """,

            (
                name,
                email,
                message
            )

        )

        connection.commit()

        cursor.close()
        connection.close()



        flash(
            "Thank you! Your message has been sent successfully.",
            "success"
        )

        return redirect(
            url_for("contact.contact")
        )



    return render_template(
        "contact.html"
    )