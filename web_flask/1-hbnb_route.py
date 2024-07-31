#!/usr/bin/python3

"""
Script to start a Flask web application with two routes.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Handles requests to the root URL and returns a greeting message.
    Returns:
        str: The greeting message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnd_route():
    """
    Handles requests to the '/hbnb' URL and returns another message.
    Returns:
        str: The message 'HBNB'
    """
    return 'HBNB'


if __name__ == '__main__':
    """
    Main entry point of the application. 
    Runs the Flask app on all available IP addresses at port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
