#!/usr/bin/python3
"""
    a script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states_route():
    """
    Display a webpage with a list of cities by state.
    Returns:
        html: A template listing all states sorted alphabetically.
    """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(exception=None):
    """
    Close the current SQLAlchemy session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
