import urllib2 as url
import xml.etree.ElementTree as ET
from game import Game

def get_games():
	page = url.urlopen('https://itch.io/games/price-500.xml')
	games_found = []
	raw_xml = page.read()
	root = ET.fromstring(raw_xml)
	for item in root.findall('item'):
		link = parse_one_value(item, "link")
		currency = parse_one_value(item, "currency")
		price = parse_one_value(item, "price")[1:]

		# Had trouble w/ the GPB and Euro symbol being unicode and not parsing
		if (currency == 'USD'):
			games_found.append(Game(link, currency, price))
	return games_found

def parse_one_value(element, tag):
	return element.findall(tag)[0].text
