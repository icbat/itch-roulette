#!/usr/bin/python
from settings import constants
from settings import serverConfig
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("landing.html")

if __name__ == "__main__":
    app.run(
    	debug = serverConfig["DEBUG"],
    	port = serverConfig["PORT"],
    	)