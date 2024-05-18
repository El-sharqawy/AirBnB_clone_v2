#!/usr/bin/python3
"""
start Flask web Application
"""

from flask import Flask, render_template
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
def cisfun(text):
    """Display "C " Followed by the given text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyiscool(text='is cool'):
    """Display "Python " followed by given text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def nisnumber(n):
    """Display {n} is a number only if n is integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    """Displays a HTML Page when n is Integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def nisoddoreven(n):
    """Displays a HTML Page when n is Integer"""
    string = ''
    if n % 2 == 0:
        string = '{:d} is even'.format(n)
    else:
        string = '{:d} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', string=string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
