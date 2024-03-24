#!/usr/bin/python3
"""Starts a Flask web application.
listens on 0.0.0.0, port 5000.
displaying states and cities from a database.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Renders HTML page with states and related cities.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Closes database connection.
    Main point of entry"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")