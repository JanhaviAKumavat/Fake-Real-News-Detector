from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash
)



# ==========================================
# Admin Required Decorator
# ==========================================

def admin_required(function):


    @wraps(function)
    def wrapper(*args, **kwargs):


        # Check Login

        if "user_id" not in session:


            flash(
                "Please login first.",
                "warning"
            )


            return redirect(
                url_for("auth.login")
            )




        # Check Admin Role

        if session.get("role") != "admin":


            flash(
                "Access denied. Admins only.",
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