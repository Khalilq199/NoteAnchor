# this file stores standard routes for our website, anywhere users can actually go (Home page etc..)

from flask import Blueprint, render_template

# define that this file is a blueprint for the application, it has routes inside of it

views = Blueprint("views", __name__) # setup a blueprint for the flask application

@views.route("/") # "/" route
# this home function will be called when the "/" route is entered
def home():
    return render_template("home.html")




