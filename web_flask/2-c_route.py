#!/usr/bin/python3
"""
start Flask web Application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints Only HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(input_text):
    """Display "C" Followed by the given text"""
    return 'C ' + input_text.replace('_', '')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
