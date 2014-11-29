
""" Basic data-object representing a game """
class Game:

	def __init__(self, user, name, currency, price, display_name, image_url):
		self.user = user
		self.name = name
		self.currency = currency
		self.price = price
		self.display_name = display_name
		self.image_url = image_url
