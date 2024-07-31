#!/usr/bin/python3
"""
Script to start a Flask web application with routes,
including one that displays a variable only if it's an integer.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        Function that returns 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Function that returns 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """
        Function that displays the text variable passed in the URL
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def text_var_python(text="is cool"):
    """
        Function that displays the text variable, defaulting to 'is cool'
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def var_num(n):
    """
        Function that displays a variable if it is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def var_num_template(n):
    """
        Function that displays a number in an HTML page
    """
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
