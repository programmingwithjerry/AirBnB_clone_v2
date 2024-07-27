#!/usr/bin/python3
"""
Script to start a Flask web application with routes,
including one that displays a variable only if it's an integer.
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Returns a greeting message.
    
    Returns:
        str: The message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Returns a different greeting message.
    
    Returns:
        str: The message 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
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
        text (str): The text to display after 'Python '. Defaults to 'is cool'.
    
    Returns:
        str: The formatted message 'Python <text>'.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def cool_number(n):
    """
    Returns a message only if the provided variable is an integer.
    
    Args:
        n (int): The integer to display in the message.
    
    Returns:
        str: The message '<n> is a number'.
    """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    """
    Main entry point of the application.
    Runs the Flask app on all available IP addresses at port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
