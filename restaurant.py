class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name + " is a plain building that smells like " + self.cuisine_type + ".")
	
	def open_restaurant(self):
		print(self.restaurant_name + " is closed. They went bankrupt.")
		