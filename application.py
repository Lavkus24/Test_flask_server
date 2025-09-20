# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
# from helper.temp import print_name
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
from routes import register_routes
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

register_routes(app)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0", port=5001, debug=True)
