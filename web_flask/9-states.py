#!/usr/bin/python3
"""
start Flask web Application
"""

from flask import Flask, render_template, redirect, url_for
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Catch all the States Data"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def statesByID(id):
    myState = None
    unseen = True
    for state in storage.all(State).values():
        if state.id == id:
            myState = state
            unseen = False
            break
    return render_template("9-states.html", id=id,
                           state=myState, notfound=unseen)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
