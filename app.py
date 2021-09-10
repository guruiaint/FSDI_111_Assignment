#1/usr/bin/env python3
#-*- coding: utf8 -*-
"""flask route definitions"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about_me():
    me = {
        "first_name": "Alex",
        "last_name": "Jones",
        "hobbies": "Golf",
        "active": True,
    }
    return me