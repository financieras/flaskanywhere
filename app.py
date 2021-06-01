#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request
import git

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('.')
        origin = repo.remotes.origin
        #repo.create_head('master',origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/')
def hello():
    return '<h1>hello there from PythonAnywhere!</h1><p>Continuous Deployment of a <b>Python</b> Flask Application.</p>'
if __name__ == '__main__':
    app.run(debug=True)