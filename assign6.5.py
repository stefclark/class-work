#10-1 Learning Python
#with open('learning_python.txt') as file_object:
#	contents = file_object.read()
	## or replace read() with rstrip() if you don't want extra whitespace
#	print(contents)
	
#filename = 'learning_python.txt'
#with open(filename) as file_object:
#	for line in file_object:
#		print(line)
		## again you can use rstrip() to get rid of whitespace

#filename = 'learning_python.txt'
#with open(filename) as file_object:
#	lines = file_object.readlines()
	
#for line in lines:
#	print(line.rstrip().replace('Python', 'C'))
		
#10-2 Learning C
	## above

#10-3 Guest
	#skip

#10-4 Guest Book 
#filename = 'guestbook.txt'
#name_inquiry = "Would you like to sign the guest book? Enter your name or type 'no' to quit: "
#name_input = input(name_inquiry)

#while(name_input != 'no'):
#	if(name_input != 'no'):
#		name_input = input(name_inquiry)
#		if(name_input != 'no'):
#			with open(filename, 'a') as file_object:
#				file_object.write(name_input + "\n")
	
#	else:
#		print("Thanks for attending!")
	
#with open('guestbook.txt') as file_object:
#	contents = file_object.read()
#	print(contents)

#10-5 Programming Poll
#filename = 'programmingpoll.txt'
#programming_poll = "What is your favorite thing about programming? Press enter to skip... "
#poll = input(programming_poll)
#with open(filename, 'a') as file_object:
#	file_object.write(poll + "\n")

#while(poll != " "):
#		#poll = input(programming_poll)
#	if(poll != " "):
#		poll = input(programming_poll)
#		file_object.write(poll + "\n")
#	else:
#		print("Bye")
#with open(filename) as file_object:
#	contents = file_object.read()
#	print(contents)

#10-6 Addition
	## buh

#10-7 Addition Calculator
	## repeat of buh 
	
#10-8 Cats and Dogs
#filename = 'cats.txt'

#def read_animals(filename):
#	try:
#		with open(filename) as f_obj:
#			contents = f_obj.read()
#	except FileNotFoundError:
#		message = "Nope"
#		print(message)
#		#pass
#	else:
#		with open(filename) as f_obj:
#			contetns = f_obj.read()
#			print(contents)

#filenames = ['cats.txt', 'dogs.txt']
#for filename in filenames:
#	read_animals(filename)
	
#10-9 Silent Cats and Dogs
	## done
	
#10-10 Common Words
	##skip?

#10-11 Favorite Number
#import json

#fav_number = input("What is your favorite number? ")

#filename = 'favnumber.txt'
#with open(filename, 'w') as f_obj:
#	json.dump(fav_number, f_obj)
#	print("Storing your favorite number as: " + fav_number + ".")	

#10-12 Favorite Number Remembered 
	##seperate file

#10-13 Verify User
##repeat 

#11-1 City, Country 

#11-2 Population 

#11-3 Employee 
