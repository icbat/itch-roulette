"""Super-basic server that serves a static page and handles requests to generate the 'buy' page """
from settings import constants
from roulette import roulette
import argparse

from flask import Flask
from flask import render_template
app = Flask(__name__)

api_endpoint = "/api/" + constants["API_VERSION"] + "/"

@app.route("/")
def hello():
    return render_template("landing.html") 

@app.route(api_endpoint + "games-under/<int:dollars>")
def get_games(dollars):
	return render_template("buy.html", games=roulette.play(dollars))



parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default="5000")
parser.add_argument('--ip', default="127.0.0.1")
parser.add_argument('--debug', default=False)
args = parser.parse_args()

if __name__ == "__main__":
    app.run(
    	host = args.ip,
    	debug = args.debug,
    	port = args.port,
    	)