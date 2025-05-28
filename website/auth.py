# this file stores the standard routes for user authentication

from flask import Blueprint, render_template

# define that this file is a blueprint for the application, it has routes inside of it

auth = Blueprint("auth", __name__) # setup a blueprint for the flask application

@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def signup():
    return render_template("sign_up.html")

