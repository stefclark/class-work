#9-1 Restaurant 
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name + " is a plain building that smells like " + self.cuisine_type + ".")
	
	def open_restaurant(self):
		print(self.restaurant_name + " is closed. They went bankrupt.")
	
#my_restaurant = Restaurant('BEEFTOWN', 'beef')
#print("My restaurant is named " + my_restaurant.restaurant_name + ".")
#print("The resturant sells " + my_restaurant.cuisine_type + ".")
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

#9-2 Three Restaurants

#my_restaurant = Restaurant('Here is a name', 'food')
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()
#my_restaurant = Restaurant('Here is another name', 'more food')
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()
#my_restaurant = Restaurant('Another restaurant?', 'no food, only aesthetic')
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

#9-3 Users
#class User():
#	def __init__(self, first_name, last_name):
#		self.first_name = first_name
#		self.last_name = last_name
		#now create hella attributes
#	def describe_user(self):
		#now print a summary of that info
#	def greet_user(self):
		#now print a personalized greeting 
	
#my_user = User('Blue', 'Acevedo')

#9-4 Numbers Served
#class Restaurant():
#	def __init__(self, restaurant_name, cuisine_type, number_served = 0):
#		self.restaurant_name = restaurant_name
#		self.cuisine_type = cuisine_type
#		self.number_served = number_served
	
#	def describe_restaurant(self):
#		print(self.restaurant_name + " is a plain building that smells like " + self.cuisine_type + ".")
	
#	def open_restaurant(self):
#		print(self.restaurant_name + " is closed. They went bankrupt.")
		
#	def set_number_served(self):
#		print(self.restaurant_name + " has served " + self.number_served + " customers.")

#my_restaurant = Restaurant('BEEFTOWN', 'beef', '42')
#my_restaurant.set_number_served()

#9-5 Login Attempts
	#basically just adding for loops and whatnot

#9-6 Ice Cream Stand
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		
	def flavor_options(self):
		flavors = []
		flavors = ['vanilla', 'mint', 'chocolate']
		print(self.restaurant_name + " serves " + self.cuisine_type + ". The flavors available are: ")
		for items in flavors:
			print(items)

#my_iceCream = IceCreamStand('Helado', 'ice cream')
#my_iceCream.flavor_options()

#9-7 Admin
	##holy fuck repeating shit

#9-8 Privileges 
	##more repeating... 

#9-9 Battery Upgrade 
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
class Battery()	:
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kwh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approx " + str(range)
		message += " miles on a full charge."
		print(message)
		
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
		
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
	
#my_car = ElectricCar('anything but a tesla', 'model not a tesla', '2018')
#my_car.battery.get_range()

#9-10 Imported Restaurant
	## used other files cause that's how it worked

#9-11 Imported Admin
	##I STG 

#9-12 Multiple Modules 
	## NO

#9-13 OrderedDict Rewrite
	## p 186
##how about no

#9-14 Dice


#9-15 Python Module of the Week
	##### Dying
