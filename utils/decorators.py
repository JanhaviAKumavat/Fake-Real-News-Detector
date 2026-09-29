
from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash
)





# ==========================================
# LOGIN REQUIRED DECORATOR
# ==========================================


def login_required(function):


    @wraps(function)
    def wrapper(*args, **kwargs):


        # Check user login


        if "user_id" not in session:


            flash(
                "Please login to access this page.",
                "warning"
            )


            return redirect(
                url_for("auth.login")
            )



        return function(
            *args,
            **kwargs
        )


    return wrapper







# ==========================================
# ADMIN REQUIRED DECORATOR
# ==========================================


def admin_required(function):


    @wraps(function)
    def wrapper(*args, **kwargs):


        # Check login first


        if "user_id" not in session:


            flash(
                "Please login first.",
                "warning"
            )


            return redirect(
                url_for("auth.login")
            )




        # Check admin role


        if session.get("role") != "admin":


            flash(
                "Admin access required.",
                "danger"
            )


            return redirect(
                url_for("home.home")
            )




        return function(
            *args,
            **kwargs
        )


    return wrapper