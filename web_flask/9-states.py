#!/usr/bin/python3
"""Starts a Flask web application.
displaying state info from a database.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Renders HTML page with list of states.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Renders HTML page with details of a specific state.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """
    Closes database connection.
    """
    storage.close()

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host="0.0.0.0")
>>>>>>> 371a3db70389cca8ed8f5412117574ab86462a9d
