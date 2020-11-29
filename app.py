#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:03:24 2020

@author: shayyyyyy
"""
from flask import Flask
from predictor import *

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    x = "shay"
    pred('./positive.jpg')
    return pred('./positive.jpg')

@app.route('/b', methods=['GET'])
def bye():
    x = "shay"
    x = pred('./positive.jpg')
    return x



if __name__ == '__main__':
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='localhost', port=8080, debug=True)