#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints Hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Prints C <text> """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    """ Prints python <text> """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ Prints number """
    if int(n):
        return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
