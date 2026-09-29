from flask import Blueprint, render_template

home_bp = Blueprint(
    "home",
    __name__
)


# ==========================================
# HOME PAGE
# ==========================================

@home_bp.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================
# ABOUT PAGE
# ==========================================

@home_bp.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ==========================================
# SERVICES PAGE
# ==========================================

@home_bp.route("/services")
def services():

    return render_template(
        "services.html"
    )