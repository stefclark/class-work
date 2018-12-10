#7-1 Rental Car
#rentalCar = input("What rental car you want? ")
#print("Lemmie see if I can find you a " + rentalCar)

#7-2 Restrurant Seating 
#tableOf = input("How many people are in your dinner party? ")
#tableOf = int(tableOf)
#if(tableOf > 8):
#	print("Due to the size of your party, there will be a delay for a table.")
#else:
#	print("Your table is ready.")

#7-3 Multiples of Ten
#numberRequest = input("Gimmie a number: ")
#numberRequest = int(numberRequest)
#if(numberRequest % 10 == 0):
#	print("This number is divisible by 10!")
#else:
#	print("Nope. Not divisible by 10")

#7-4 Pizza Toppings
#pizzaToppingsQuestion = "\nWhat do you want on your pizza? "
#pizzaToppingsQuestion += "\nInput 'quit' to end your order. "
#pizzaToppings = ""

#while(pizzaToppings != 'quit'):
#	pizzaToppings = input(pizzaToppingsQuestion)
	
#	if(pizzaToppings != 'quit'):
#		print("I will add " + pizzaToppings + " to your pizza.")
		
#	else:
#		print("I will have the chef start on your pizza.")

#7-5 Movie Tickets 
##bullshitting

#7-6 Three Exits 
## more bullshitting

#7-7 Infinity 
##NO

#7-8 Deli
#sandwich_orders = ['ham and cheese', 'BLT', 'philly cheesesteak', 'meatball sub']
#finished_sandwiches = []

#sandwichOrderQuestion = "\nWhat sandwich would you like to order? "
#sandwich = ""

#7-9 No Pastrami 
##more bullshitting

#7-10 Dream Vacation 
#dreamVacation = {}
#pollingActive = True

#while(pollingActive):
#	name = input("\nWhat is your name? ")
#	response =  input("\nIf you could visit anywhere, where would you go? ")
#	dreamVacation[name] = response
#	moreResponses = input("\nWould anyone else like to submit to the poll? (yes/no) ")
#	if(moreResponses == 'no'):
#		pollingActive = False

#print("\n ------ Poll Results ------")
#for name, response in dreamVacation.items():
#	print(name + " would like to visit " + response + ".")

#8-1 Message
def display_message():
	print("Hello, world.")
	
#display_message()

#8-2 Favorite Book 
def favorite_book():
	title = "Fahrenheit 451"
	print("My favorite book is " + title + ".")
	
#favorite_book()

#8-3 T-Shirt
def t_shirt(size, text):
	print("Your shirt is size " + size +  " and it will say " + text)
	
#t_shirt('small', 'hello world')

#8-4 Large Shirts
##more bullshitting

#8-5 Cities 
##more bullshitting

#8-6 City Names
def city_country(city,country):
	print("___________________________" + "\n" + city + ", " + country + "\n___________________________")

#city_country("Tokyo", "Japan")	

#8-7 Album
#album = {}

#def make_album(name, title):
#add = input("\nWould you like to add an album to the dictionary? (yes/no)")
#while(add == 'yes'):
#	artistName = input("\nWhat is the name of the artist? ")
#	albumTitle = input("\nWhat is the title of the album? ")
#	album = {artistName, albumTitle}
	
#	return album 
#print(album) 

#make_album(artistName, albumTitle)	

##hella broken, infinite loop
		
#8-8 User Albums 
##more bullshitting

#8-9 Magicians 
#def show_magician(names):
#	for name in names:
#		magicianPrint = "Welcome to the stage the Great Magician " + name + "!"
#		print(magicianPrint)

#magicians = ['houdini', 'zatanna', 'zatarra']	
#show_magician(magicians)

#8-10 Great Magicians 
##stop repeating

#8-11 Unchanged Magicians
##stop repeating

#8-12 Sandwiches
def makeSandwich(*ingredients):
	print("Your sandwich will have: ")
	for ingredient in ingredients:
		print("- " + ingredient)
	
#makeSandwich('ham', 'cheese')
#makeSandwich('peanut butter')

#8-13 User Profile
##more bullshitting

#8-14 Cars


#8-15 Printing Models 

#8-16 Imports 

#8-17 Styling Functions 
##NAH
