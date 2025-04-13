# this file stores the standard routes for user authentication

from flask import Blueprint

# define that this file is a blueprint for the application, it has routes inside of it

auth = Blueprint("auth", __name__) # setup a blueprint for the flask application

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def signup():
    return "<p>Sign-up</p>"

