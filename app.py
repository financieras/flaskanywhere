#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request
from flask.wrappers import Response

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def update_server():
    print(request.json)
    return Response(status=200)

@app.route('/')
def hello():
    return '<h1>Hello there from PythonAnywhere!</h1><p>Continuous Deployment of a Python Flask Application.</p>'
