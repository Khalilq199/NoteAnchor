# This is a flask application
# This webiste folder is a python package because it has the __init__.py file inside it
# everything in the __init__.py file will automatically be ran when website is imported
# this file buils and returns the app instance

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SWE"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
