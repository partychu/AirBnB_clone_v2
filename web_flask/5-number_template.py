#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Prints number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_t(n):
    """ Display a HTML page if <n> is int """
    return render_template('5-number.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
