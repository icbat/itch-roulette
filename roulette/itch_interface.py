import urllib2 as url
import xml.etree.ElementTree as ET
import game

def get_games():
	page = url.urlopen('https://itch.io/games/price-500.xml')
	raw_xml = page.read()
	root = ET.fromstring(raw_xml)
	for item in root.findall('item'):
		print item
		print parse_one_value(item, "link")
	return "games. I promise"

def parse_one_value(element, tag):
	return element.findall(tag)[0].text
