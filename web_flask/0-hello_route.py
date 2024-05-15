#!/usr/bin/python3
"""This starts Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root, strict_slashes ensure
    the url works
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
