# from flask import (
#     Flask,
#     render_template,
#     session
# )

# from dotenv import load_dotenv

# import os



# # =====================================================
# # LOAD ENVIRONMENT VARIABLES
# # =====================================================

# load_dotenv()






# # =====================================================
# # BLUEPRINT IMPORTS
# # =====================================================


# from routes.home import home_bp
# from routes.auth import auth_bp
# from routes.detector import detector_bp
# from routes.profile import profile_bp
# from routes.history import history_bp
# from routes.contact import contact_bp
# from routes.admin import admin_bp







# # =====================================================
# # APP CREATION
# # =====================================================


# app = Flask(__name__)





# # =====================================================
# # CONFIGURATION
# # =====================================================


# app.secret_key = os.getenv(
#     "SECRET_KEY",
#     "fake-news-secret-key"
# )





# # Upload folder

# UPLOAD_FOLDER = os.getenv(
#     "UPLOAD_FOLDER",
#     "uploads"
# )


# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER





# if not os.path.exists(
#     UPLOAD_FOLDER
# ):

#     os.makedirs(
#         UPLOAD_FOLDER
#     )









# # =====================================================
# # REGISTER BLUEPRINTS
# # =====================================================


# # Public Routes

# app.register_blueprint(
#     home_bp
# )


# app.register_blueprint(
#     auth_bp
# )


# app.register_blueprint(
#     detector_bp
# )


# app.register_blueprint(
#     profile_bp
# )


# app.register_blueprint(
#     history_bp
# )


# app.register_blueprint(
#     contact_bp
# )





# # Admin Routes

# app.register_blueprint(
#     admin_bp
# )









# # =====================================================
# # GLOBAL CONTEXT
# # =====================================================


# @app.context_processor
# def inject_user():


#     return {

#         "session":session

#     }









# # =====================================================
# # HOME ERROR HANDLER
# # =====================================================


# @app.errorhandler(404)
# def page_not_found(error):


#     return render_template(

#         "error404.html"

#     ),404





# @app.errorhandler(500)
# def internal_error(error):

#     print("500 ERROR:", error)

#     return str(error), 500




# # =====================================================
# # RUN APPLICATION
# # =====================================================


# if __name__ == "__main__":
#     app.run (
#         host="127.0.0.1",
#         port=5000,
#         debug=False,
#         use_reloader=False
#     )



from flask import Flask, render_template, session
from dotenv import load_dotenv
import os
import traceback

from config import Config

# =====================================================
# LOAD ENVIRONMENT VARIABLES
# =====================================================

load_dotenv()

# =====================================================
# IMPORT BLUEPRINTS
# =====================================================

from routes.home import home_bp
from routes.auth import auth_bp
from routes.detector import detector_bp
from routes.profile import profile_bp
from routes.history import history_bp
from routes.contact import contact_bp
from routes.admin import admin_bp

# =====================================================
# CREATE APP
# =====================================================

app = Flask(__name__)

# =====================================================
# LOAD CONFIG
# =====================================================

app.config.from_object(Config)

app.secret_key = Config.SECRET_KEY

# Upload Folder

os.makedirs(
    Config.UPLOAD_FOLDER,
    exist_ok=True
)

app.config["UPLOAD_FOLDER"] = Config.UPLOAD_FOLDER

# =====================================================
# REGISTER BLUEPRINTS
# =====================================================

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(detector_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(history_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(admin_bp)

# =====================================================
# CONTEXT PROCESSOR
# =====================================================

@app.context_processor
def inject_user():
    return {
        "session": session
    }

# =====================================================
# ERROR HANDLERS
# =====================================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    print("\n" + "=" * 80)
    print("500 INTERNAL SERVER ERROR")
    traceback.print_exc()
    print("=" * 80 + "\n")
    return render_template("error500.html"), 500

# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    try:

        print("=" * 60)
        print("Fake News Detector AI")
        print("Starting Flask Server...")
        print("=" * 60)

        app.run(
            host="127.0.0.1",
            port=5000,
            debug=True,
            use_reloader=False
        )

    except Exception as e:

        print("\n" + "=" * 60)
        print("APPLICATION CRASHED")
        print(type(e).__name__)
        print(e)
        traceback.print_exc()
        print("=" * 60)