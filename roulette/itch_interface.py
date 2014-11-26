import urllib2

def get_games():
	page = urllib2.urlopen('https://itch.io/games/price-500.xml')
	raw_xml = page.read()
	return "games. I promise"