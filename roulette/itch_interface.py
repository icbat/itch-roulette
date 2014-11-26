import urllib2
import xml.etree.ElementTree as ET
from game import Game

prefix_length = len("https://") - 1

def get_games():
	return get_games_from_url("https://itch.io/games/price-500.xml")

def get_games_from_url(url):
	page = urllib2.urlopen(url)
	return parse_xml(page)

def parse_xml(page):
	games_found = []
	raw_xml = page.read()
	root = ET.fromstring(raw_xml)
	for item in root.findall('item'):
		link = parse_one_value(item, "link")
		user = parse_user(link)
		name = parse_game_name(link)
		currency = parse_one_value(item, "currency")
		price = parse_one_value(item, "price")[1:]
		if (currency == 'USD'):
			games_found.append(Game(user, name, currency, price))
	return games_found	

def parse_one_value(element, tag):
	return element.findall(tag)[0].text

def parse_user(url):
	domain_index = url.find(".itch.io")	
	return url[prefix_length:domain_index]

def parse_game_name(url):
	end_of_domain = url[prefix_length:].find("/") + 1
	return url[prefix_length + end_of_domain:]