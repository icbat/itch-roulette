import itch_interface
import random

def play(dollars):
	games = itch_interface.get_games()
	random.shuffle(games)
	string = ""
	for game in games:
		string += str(game.price)
		string += " : "
		string += game.link		
		string += "<br/>"
	return string