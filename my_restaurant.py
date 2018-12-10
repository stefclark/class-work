from restaurant import Restaurant

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		
	def flavor_options(self):
		flavors = []
		flavors = ['vanilla', 'mint', 'chocolate']
		print(self.restaurant_name + " serves " + self.cuisine_type + ". The flavors available are: ")
		for items in flavors:
			print(items)

my_iceCream = IceCreamStand('Helado', 'ice cream')
my_iceCream.flavor_options()