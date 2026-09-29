from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    session,
    url_for
)


from database.database import get_db_connection


from utils.validators import (
    validate_email,
    validate_password,
    validate_name
)





# ==================================================
# AUTH BLUEPRINT
# ==================================================


auth_bp = Blueprint(
    "auth",
    __name__
)









# ==================================================
# REGISTER
# ==================================================


@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():



    if session.get("user_id"):


        if session.get("role") == "admin":


            return redirect(
                url_for(
                    "admin.dashboard"
                )
            )


        return redirect(
            url_for(
                "profile.profile"
            )
        )






    if request.method == "POST":



        full_name = request.form.get(
            "full_name"
        )


        email = request.form.get(
            "email"
        )


        password = request.form.get(
            "password"
        )







        # ==============================
        # VALIDATION
        # ==============================


        if not validate_name(full_name):


            flash(
                "Enter valid name.",
                "danger"
            )


            return redirect(
                url_for(
                    "auth.register"
                )
            )





        if not validate_email(email):


            flash(
                "Enter valid email.",
                "danger"
            )


            return redirect(
                url_for(
                    "auth.register"
                )
            )






        if not validate_password(password):


            flash(
                "Password must contain uppercase, lowercase and number.",
                "danger"
            )


            return redirect(
                url_for(
                    "auth.register"
                )
            )









        try:



            connection = get_db_connection()


            cursor = connection.cursor(
                dictionary=True
            )





            # CHECK EMAIL EXISTS


            cursor.execute(

                """
                SELECT id
                FROM users
                WHERE email=%s
                """,

                (email,)

            )


            existing_user = cursor.fetchone()






            if existing_user:



                flash(
                    "Email already registered.",
                    "danger"
                )


                cursor.close()

                connection.close()



                return redirect(
                    url_for(
                        "auth.register"
                    )
                )









            # ==============================
            # DIRECT PASSWORD STORAGE
            # ==============================


            cursor.execute(

                """
                INSERT INTO users

                (
                    full_name,
                    email,
                    password,
                    role
                )

                VALUES

                (%s,%s,%s,%s)

                """,

                (

                    full_name,

                    email,

                    password,

                    "user"

                )

            )






            connection.commit()



            cursor.close()

            connection.close()






            flash(
                "Registration successful. Please login.",
                "success"
            )



            return redirect(

                url_for(
                    "auth.login"
                )

            )







        except Exception as e:


            print(
                "Register Error:",
                e
            )


            flash(
                "Registration failed.",
                "danger"
            )







    return render_template(
        "register.html"
    )














# ==================================================
# LOGIN
# ==================================================


@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():



    if session.get("user_id"):



        if session.get("role") == "admin":


            return redirect(

                url_for(
                    "admin.dashboard"
                )

            )



        return redirect(

            url_for(
                "profile.profile"
            )

        )









    if request.method == "POST":



        email = request.form.get(
            "email"
        )


        password = request.form.get(
            "password"
        )








        try:



            connection = get_db_connection()


            cursor = connection.cursor(
                dictionary=True
            )





            cursor.execute(

                """
                SELECT *
                FROM users
                WHERE email=%s
                """,

                (email,)

            )



            user = cursor.fetchone()





            cursor.close()

            connection.close()









            if user:



                # ==============================
                # DIRECT PASSWORD CHECK
                # ==============================


                if user["password"] == password:




                    session.clear()



                    session["user_id"] = user["id"]

                    session["user_name"] = user["full_name"]

                    session["email"] = user["email"]

                    session["role"] = user["role"]






                    flash(

                        "Login successful.",

                        "success"

                    )








                    # ADMIN LOGIN


                    if user["role"] == "admin":



                        return redirect(

                            url_for(
                                "admin.dashboard"
                            )

                        )







                    # USER LOGIN


                    return redirect(

                        url_for(
                            "profile.profile"
                        )

                    )









            flash(

                "Invalid email or password.",

                "danger"

            )







        except Exception as e:



            print(

                "Login Error:",

                e

            )


            flash(

                "Login failed.",

                "danger"

            )








    return render_template(
        "login.html"
    )












# ==================================================
# LOGOUT
# ==================================================


@auth_bp.route(
    "/logout"
)
def logout():



    session.clear()



    flash(

        "Logged out successfully.",

        "success"

    )



    return redirect(

        url_for(
            "auth.login"
        )

    )