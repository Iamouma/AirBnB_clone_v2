#!/usr/bin/python3
"""This starts a Flask web applicaton"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root, strict_slashes ensure
    the URL works
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Routing to /hbnb, strict_slashes ensure
    the URL works
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """The Routing to C using Variables"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """The Routing to python with default value using Variables"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_numbet(n):
    """The Routing to n for intergers only"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_numbet_template(n=None):
    """This Renders an HTML page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)