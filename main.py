# this file runs the flask application

from website import create_app

app = create_app()

if __name__ == '__main__': # only run main.py if it is run directly not if it is imported
    app.run(debug=True) # run the flask application, start a web server, debug=True will rerun the web server after any code changes

