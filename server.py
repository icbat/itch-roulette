#!/usr/bin/python
from settings import constants
from settings import server_config
from roulette import roulette

from flask import Flask
from flask import render_template
app = Flask(__name__)

api_endpoint = "/api/" + constants["API_VERSION"] + "/"

@app.route("/")
def hello():
    return render_template("landing.html") 

@app.route(api_endpoint + "games-under/<int:dollars>")
def get_games(dollars):
	return roulette.play(dollars) 

if __name__ == "__main__":
    app.run(
    	debug = server_config["DEBUG"],
    	port = server_config["PORT"],
    	)