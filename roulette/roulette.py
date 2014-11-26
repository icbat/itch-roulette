import itch_interface
import random

def play(dollars):
	games = itch_interface.get_games()
	random.shuffle(games)
	current_sum = 0
	games_to_buy = []
	for game in games:
		if float(game.price) + current_sum < dollars:
			games_to_buy.append(game)
			current_sum += float(game.price)


	return convert_for_display(games_to_buy)

""" Takes a list of games and formats it for web display """
def convert_for_display(games):
	string = ""
	for game in games:
		string += str(game.price)
		string += " : "
		string += game.user		
		string += "<br/>"
	return string
