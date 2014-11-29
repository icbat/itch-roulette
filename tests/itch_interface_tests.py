# Run all tests from basedir with `nosetests`. Don't run locally, imports fail
from roulette.game import Game
import roulette.itch_interface as itch_interface

def test_remove_duplicates_happy():
	games = []
	first_game = Game("icbat", "pressing", "some currency", "1234", "display_name", "image url")
	second_game = Game("icbat", "pressing", "some currency", "1234", "display_name", "image url")
	games.append(first_game)
	games.append(second_game)
	assert len(games) == 2

	trimmed = itch_interface.remove_duplicates(games)

	# assert no side-effects
	assert len(games) == 2
	assert len(trimmed) == 1
	assert trimmed[0].user == "icbat"

def test_remove_duplicates_no_work():
	games = []
	first_game = Game("icbat", "pressing", "some currency", "1234", "display_name", "image url")
	second_game = Game("someone else", "a better game", "a different currency", "4567", "disp", "url")
	games.append(first_game)
	games.append(second_game)
	assert len(games) == 2

	trimmed = itch_interface.remove_duplicates(games)

	# assert no side-effects
	assert len(games) == 2
	assert len(trimmed) == 2
	assert trimmed[0].user == "icbat"
	assert trimmed[1].user == "someone else"
