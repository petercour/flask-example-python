#!/usr/bin/python3
# -*- coding: utf-8 -*
from flask import Flask
from flask import request
from flask import make_response
 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/browser')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
 
if __name__ == '__main__':
    app.run()
