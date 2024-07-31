#!/usr/bin/python3
"""
    a script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


def handle_teardown(self):
    """
        Function to manage application teardown
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters_list():
    """
        Function to render the HTML page 6-index.html
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
