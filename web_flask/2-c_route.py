#!/usr/bin/python3
"""
Script to initiate a Flask web application.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Returns a greeting message 'Hello HBNB!'.

    Returns:
        str: The message 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Returns the message 'HBNB'.

    Returns:
        str: The message 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Returns 'C ' followed by the value of the text variable,
    with underscores replaced by spaces.

    Args:
        text (str): The text to display after 'C '.

    Returns:
        str: The formatted message 'C <text>'.
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    """
    Main entry point of the application.
    Runs the Flask app on all available IP addresses at port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
