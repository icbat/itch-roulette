import itch_interface

def play(dollars):
	games = itch_interface.get_games()
	string = ""
	for game in games:
		string += str(game.price)
		string += " : "
		string += game.link		
		string += "<br/>"
	return string