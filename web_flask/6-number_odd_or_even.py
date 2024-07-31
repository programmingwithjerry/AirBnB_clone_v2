#!/usr/bin/python3
"""
Script to start a Flask web application with multiple routes,
including one that displays an HTML page if the variable is an integer.
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Returns a greeting message.

    Returns:
        str: The message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """
    Returns a different greeting message.

    Returns:
        str: The message 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun_text(text):
    """
    Returns 'C ' followed by the value of the text variable,
    with underscores replaced by spaces.

    Args:
        text (str): The text to display after 'C '.

    Returns:
        str: The formatted message 'C <text>'.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """
    Returns 'Python ' followed by the value of the text variable,
    with a default value if not provided.

    Args:
        text (str): The text to display after 'Python '.
        Defaults to 'is cool'.

    Returns:
        str: The formatted message 'Python <text>'.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def integr_number(n):
    """
    Returns a message only if the provided variable is an integer.

    Args:
        n (int): The integer to display in the message.

    Returns:
        str: The message '<n> is a number'.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_html(n):
    """
    Renders an HTML page if the provided variable is an integer.

    Args:
        n (int): The integer to display on the HTML page.

    Returns:
        str: The rendered HTML template with the integer.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Renders a different HTML page depending on whether the
    provided integer is odd or even.

    Args:
        n (int): The integer to evaluate and display on the HTML page.

    Returns:
        str: The rendered HTML template indicating if the
        integer is odd or even.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """
    Main entry point of the application.
    Runs the Flask app on all available IP addresses at port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
