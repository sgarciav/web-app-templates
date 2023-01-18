#!/usr/bin/env python3

import argparse
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """User home page."""
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return render_template('index.html', fahrenheit=fahrenheit)

## Example of how to add another URL route to access directly from the browser
# @app.route("/<int:celsius>")
# def fahrenheit_from(celsius):
#     """Convert Celsius to Fahrenheit degrees."""
#     fahrenheit = float(celsius) * 9 / 5 + 32
#     fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
#     return str(fahrenheit)

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


# ---------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run max reps tracker server.')
    parser.add_argument('-i', '--ip_addr', type=str, help='IP address of the host.', default='192.168.1.70')
    parser.add_argument('-p', '--port', type=int, help='Port of the host.', default=5000)

    args = parser.parse_args()

    # Run main application
    app.run(host=args.ip_addr, port=args.port, threaded=True)
