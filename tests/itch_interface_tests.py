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

def test_parse_xml_happy():
	xml = """
<rss version="2.0">
<item>
<link>https://a_user.itch.io/game-name/</link>
<currency>USD</currency>
<plainTitle>a game as Displayed like this</plainTitle>
<imageurl>a url</imageurl>
<price>$12314</price>
</item>
</rss>
		"""

	games_found = itch_interface.parse_xml(xml)

	assert len(games_found) == 1

def test_parse_xml_only_accepts_USD():
	xml = """
<rss version="2.0">
<item>
<link>https://a_user.itch.io/game-name/</link>
<currency>a strange and exotic currency</currency>
<plainTitle>a game as Displayed like this</plainTitle>
<imageurl>a url</imageurl>
<price>$12314</price>
</item>
</rss>
		"""

	games_found = itch_interface.parse_xml(xml)

	assert len(games_found) == 0

def test_parse_xml_no_items_returned():
	xml = """<rss version="2.0"/>"""

	games_found = itch_interface.parse_xml(xml)

	assert len(games_found) == 0