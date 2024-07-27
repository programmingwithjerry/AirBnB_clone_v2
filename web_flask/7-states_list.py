#!/usr/bin/python3
"""
Script to start a Flask web application with routes for different functionalities.
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False  # Disables strict slashes for route URLs


if __name__ == '__main__':
    """
    Main entry point of the application.
    Runs the Flask app on all available IP addresses at port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
    # Starts the Flask web server, making the app accessible
    #on all network interfaces at port 5000.
