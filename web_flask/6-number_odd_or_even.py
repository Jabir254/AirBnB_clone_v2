#!/usr/bin/python3
"""Odd or Even"""


from flask import Flask, render_template
from . import templates

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number_template.html', number=n)
    else:
        return 'Invalid input. Please provide an integer.'


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        number_type = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html',
                               number=n, number_type=number_type)
    else:
        return 'Invalid input. Please provide an integer.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
