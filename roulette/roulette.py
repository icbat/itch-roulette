import itch_interface
import random

""" 
Builds bundles of games up to the dollar amount sent as an argument.

side-effect:  relies on itch_interface, which (if not mocked) will make HTTP requests 
"""
def play(dollars):
	games = itch_interface.get_games()
	random.shuffle(games)
	current_sum = 0
	games_to_buy = []
	for game in games:
		if float(game.price) + current_sum < dollars:
			games_to_buy.append(game)
			current_sum += float(game.price)


	return games_to_buy