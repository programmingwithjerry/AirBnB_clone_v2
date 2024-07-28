#!/usr/bin/python3
"""
   a script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list_route():
    """
    Display a webpage listing all states.
    Returns:
        html: A template that shows all states sorted alphabetically.
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id_route(id):
    """
    Display a webpage for a specific state by ID.
    Returns:
        html: A template that lists the cities of the state,
       sorted alphabetically.
    """
    state = None
    for s in storage.all("State").values():
        if s.id == id:
            state = s
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_db(exception=None):
    """
    Close the current SQLAlchemy session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
