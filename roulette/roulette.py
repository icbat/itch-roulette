import itch_interface
import random

def play(dollars):
	games = itch_interface.get_games()
	random.shuffle(games)
	return convert_for_display(games)

""" Takes a list of games and formats it for web display """
def convert_for_display(games):
	string = ""
	for game in games:
		string += str(game.price)
		string += " : "
		string += game.link		
		string += "<br/>"
	return string
