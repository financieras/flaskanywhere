#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request
from flask.wrappers import Response
import git

app = Flask(__name__)

#Con este codigo el webhook de GitHub no da error
@app.route('/update_server', methods=['POST'])
def update_server():
    print(request.json)
    return Response(status=200)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./flaskanywhere')
    origin = repo.remotes.origin
    repo.create_head('main', 
    origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def hello():
    return '<h1>Hello there from PythonAnywhere using Flask!</h1><p>Continuous Deployment of a Python Flask Application.</p>'
