#Chapter 5 & 6 'Try it Yourself' Exercises

#5-1 Conditional Tests
#animal = 'Bat' 
#print("Is the animal a == 'bat'? I predict True.")
#print(animal.lower() == 'bat')

#print("\nIs the animal == 'owl'? I predict False.")
#print(animal == 'owl')
 

#5-2 More Conditional Tests
	#That's gonna take up a lot of space and time and... NAH
#number = '1.1'
#print("is number == '1.1'?")
#print(number < '1.11')


#5-3 Alien Colors 1
#alien_color = 'yellow'
#if(alien_color == 'green'):
#	print('You have earned 5 points!')
#else:
#	print('The alien is ' + alien_color + '.')


#5-4 Alien Colors 2
#alien_color = 'red'
#if(alien_color == 'green'):
#	print('You have earned 5 points for defeating the alien!')
#else:
#	print('The alien is ' + alien_color + '. You have earned 10 points!')

#5-5 Alien Colors 3
#alien_color = 'green'
#if(alien_color == 'green'):
#	print('You have earned 5 points for defeating the alien!')
#elif(alien_color == 'yellow'):
#	print('You have earned 10 points for defeating the alien!')
#elif(alien_color == 'red'):
#	print('You have earned 15 points for defeating the alien!')
#else:
#	print('The alien is ' + alien_color + '. You have earned 0 points.')


#5-6 Stages of Life
#age = 24
#if age < 2:
#	print("You are a baby.")
#elif age >= 2 and age < 4:
#	print("You are a toddler.")
#elif age >= 4 and age < 13:
#	print("you are a kid.")
#elif age >= 13 and age < 20:
#	print("You are a teenager.")
#elif age >= 20 and age < 65:
#	print("You are an adult.")
#elif age >= 65:
#	print("You are an elder.")


#5-7 Favorite Fruit
#favorite_fruits = ['kiwi', 'grape', 'melon']
#for favorite_fruit in favorite_fruits:
#	if(favorite_fruit == 'kiwi'):
#		print("Something catchy about kiwis.")
#	elif(favorite_fruit == 'grape'):
#		print("But what kind of grape?")
#	elif(favorite_fruit == 'melon'):
#		print("But not honeydew...")


#5-8 Hello Admin 
#usernameList = ['Clark', 'Admin', 'Bruce', 'Alfred']
#for username in usernameList:
#	if username == 'Admin':
#		print("Welcome back Admin.")
#	else:
#		print("Hello, " + username + ".")


#5-9 No Users
#usernameList = ['Clark', 'Admin', 'Bruce', 'Alfred']
#for username in usernameList:
#	if username == 'Admin':
#		print("Welcome back Admin.")
#	elif usernameList == ' ':
#		print('Error.')
#	else:
#		print("Hello, " + username + ".")


#5-10 Checking Usernames
#current_users = ['Clark']
#new_users = ['Barry']


#5-11 Ordinal Numbers 
#numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#for number in numberList:
#	if number == '1':
#		print("\n" + number + "st")
#	elif number == '2':
#		print("\n" + number + "nd")
#	elif number == '3':
#		print("\n" + number + "rd")
#	elif number >= '5':
#		print("\n" + number + "th")


#5-12 Styling if Statements
	#in word doc

	
#5-13 Your Ideas
	#in word doc
	

#6-1 Person
#person_information = {'first_name': 'Bruce', 'last_name' : 'Wayne', 'age' : 'unknown', 'city' : 'Gotham'} 
#print(person_information)
 

#6-2 Favorite Numbers
#favorite_numbers = {'Clark' : '13', 'Squirrel' : '6', 'Blue' : '11', 'Blair' : '13', 'Belle' : '8'} 
#print(favorite_numbers)

#6-3 Glossary 
#glossary = {
#	'sorted()' : 'lets you display your list in a particular order but doesn’t affect the actual order of the list.',
#	'type error' : 'Python can’t recognize the kind of information you’re using.',
#	'list comprehension' : 'allows you to generate this same list in just one line of code.',
#	'immutable' : 'values that cannot change', 
#	'elif' : 'stands for else if'
#	}
#print("Glossary term: Sorted()" + "\n" + glossary['sorted()'] + "")
#print("Glossary term: List Comprehension" + "\n" + glossary['list comprehension'] + "")
#print("Glossary term: Type Error" + "\n" + glossary['type error'] + "")
#print("Glossary term: Immutable" + "\n" + glossary['immutable'] + "")	
#print("Glossary term: Elif" + "\n" + glossary['elif'] + "")

#6-4 Glossary 2
#UGHHHHHH soo much text

#6-5 Rivers
#rivers = {
#	'Sepik':'New Guinea', 
#	'Volga':'Russia', 
#	'Ganges':'India', 
#	'Yangtze':'China'
#	}

#for countries in rivers.values():
#	print(countries)
	
#for river in rivers.keys():
#	print(river)

#6-6 Polling
#favorite_languages = {
#	'jen': ['python', 'ruby'],
#	'sarah': ['c'],
#	'edward': ['ruby', 'go'],
#	'phil': ['python', 'haskell'],
#	}
#Also... fight me 

#6-7 People
#person1_information = {'first_name' : 'Bruce', 'last_name' : 'Wayne', 'age' : 'unknown', 'city' : 'Gotham'} 
#person2_information = {'first_name' : 'Barry', 'last_name' : 'Allen', 'age' : 'variable', 'city' : 'Central City'}
#person3_information = {'first_name' : 'Ollie', 'last_name' : 'Queen', 'age' : 'changing', 'city' : 'Star City'} 

#for secondary_information in person1_information.values():
#		print(secondary_information)	

#uhhh, it prints randomly?


#6-8 Pets
#pet1 = {
#	'name' : 'JinJin',
#	'species' : 'cat',
#	'color' : 'orange' }
#pet2 = {
#	'name' : 'Bear', 
#	'species' : 'dog',
#	'color' : 'brown' }
#pet3 = { 
#	'name' : 'Dolittle',
#	'species' : 'cat', 
#	'color' : 'grey and white' }
#pet4 = {
#	'name' : 'Daisy',
#	'species' : 'dog',
#	'color' : 'chocolate' }

#for informaiton in pet1.values():
#	print(informaiton)


#6-9 Favorite Places
#favorite_places = {
#	'Squirrel' : ['A tree near their house that is hollow because it was struck by lightning'], 
#	'Avery' : ['Near the people they care about'], 
#	'Blair' : ['Jewelbox Cafe','The Dreaming'],
#	}
#for name, places in favorite_places.items():
#	print(name + "'s favorite place(s) is/are: ")
#	for place in places:
#		print("\t" + place)


#6-10 Favorite Numbers
#favorite_numbers = {
#	'Clark' : ['13, 1010'], 
#	'Squirrel' : ['6, 856'], 
#	'Blue' : ['11'], 
#	'Blair' : ['13, 3'], 
#	'Belle' : ['8, 5']} 
#for name, numbers in favorite_numbers.items():
#	print("\n" + name + "'s favorite numbers are:")
#	for number in numbers:
#		print("\t" + number)
		

#6-11 Cities


#6-12 Extensions 