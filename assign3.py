#Chapters 3 and $ 'Try it Yourself' Exercises 

#3-1 Names
#names = ['clark', 'bruce', 'barry', 'diana']
#print(names[0])
#print(names[2])
#print(names[1])
#print(names[3])
#print(names)

#3-2 Greetings
#greeting = "Hello, " + names[1].title() + " I hope you're enjoying your day."
#print(greeting)

#3-3 Your Own List
#transport = ['rocketship', 'shinkansen', 'dragon', 'teleportation', 'walking']
#avpmQuote = "Not all of us inherited enough money to buy out NASA... Look at this!" + transport[0].title() + " Potter! Starkid Potter!" 
#trainMessage = "When I went to Japan, I rode on the " + transport[1].title() + ". It was awesome."
#dragon = "I would like to own a " + transport[2] + "."
#teleport = "The easiest way to get anywhere is though " + transport[3] + "."
#transport.append('car')
#actualTransportation = "My preferred mode of transportation is " + transport[4] + ", but I'm lazy so I usually just use my " + transport[5] + "."
#print(actualTransportation)

#3-4 Guest list
#partyList = ['Blair', 'Erin', 'Blue', 'Nick', 'Fatima']
#inviteMessage = "Hey " + partyList[2] + "! You're invited to my party!" 
#print(inviteMessage)

#3-5 Changing Guest List
#partyDitch = "Hey " +partyList[1] + ", sorry you can't make it to the party. You'll me missed."
#print(partyDitch)
#partyList[1] = 'Jose'
#print(partyList)
#inviteMessage = "Hey " + partyList[1] + "! You're invited to my party!"
#print(inviteMessage)
#print(partyList)

#3-6 More Guests 
#partyList.insert(0, 'Squirrel')
#partyList.insert(3, 'Kelsey')
#partyList.append('Robbie')
#print(partyList)
#inviteMessage = "Hey " + partyList[7] + "! You're invited to my party!"
#print(inviteMessage)

#3-7 Shrinking Guest List 
#partyListPopped = partyList.pop()
#smallTable = "Sorry " + partyListPopped + ", there was an issue and I have to shrink the guest list..."
#print(smallTable)
#partyListPopped = partyList.pop()
#smallTable = "Sorry " + partyListPopped + ", there was an issue and I have to shrink the guest list..."
#print(smallTable)
#partyListPopped = partyList.pop()
#smallTable = "Sorry " + partyListPopped + ", there was an issue and I have to shrink the guest list..."
#print(smallTable)
#partyListPopped = partyList.pop(3)
#smallTable = "Sorry " + partyListPopped + ", there was an issue and I have to shrink the guest list..."
#print(smallTable)
#partyListPopped = partyList.pop(2)
#smallTable = "Sorry " + partyListPopped + ", there was an issue and I have to shrink the guest list..."
#print(smallTable)
#partyListPopped = partyList.pop(0)
#smallTable = "Sorry " + partyListPopped + ", there was an issue and I have to shrink the guest list..."
#print(smallTable)
#print(partyList)
#del partyList[0]
#del partyList[0]
#print(partyList)

#3-8 Seeing the World
#worldList = ['Japan', 'England', 'New Zealand', 'Canada', 'New Jersey']
#print(worldList)
#print(sorted(worldList))
#print(worldList)
#worldList.reverse()
#print(worldList)
#worldList.reverse()
#print(worldList)
	# everything below was not tested
#reverse(worldList)
#print(worldList)
#print(reverse(worldList))
#sort(worldList)
#print(worldList)
#sort(reverse(worldList))
#reverse(worldList)
#print(worldList)

#3-9 Dinner Guests
#print(len(partyList))
#print(partyList)

#3-10 Every Function 
	#UGHHHHHHHH. NO.

#3-11
	#No. I've seen too many errors in my time... I don't need those flashbacks...

#4-1 Pizzas
pizzaList = ['cheese', 'pepperoni', 'canadian bacon', 'feta']
#for pizza in pizzaList:
#	print("I like " + pizza + " pizza.")
#print("However, due to my food allergy, not all pizza likes me.")

#4-2 Animals
#animalList = ['stingray', 'dumbo octopus', 'basking shark']
#for animal in animalList:
#	print("I would like to pet a " + animal + ".")
#print("However, it would be difficult to have any of these as a pet.")

#4-3 Counting to Twenty
#numbersList = list(range(1,21))
#print(numbersList)

#4-4 One Million
#longNumbersList = list(range(1, 100001))
#print(longNumbersList)

#4-5 Summing a Million 
#print(min(longNumbersList))
#print(max(longNumbersList))
#print(sum(longNumbersList))

#4-6 Odd Numbers
#oddTwentylList = list(range(1, 21, 2))
#print(oddTwentylList)
#for number in oddTwentylList:
#	print(number)

#4-7 Threes
#multiplesThreeList = list(range(3, 31, 3))
#for number in multiplesThreeList:
#	print(number)

#4-8 Cubes
#cubes = [value**3 for value in range(1,11)]
#print(cubes)
#for number in cubes:
#	print(number)

#4-9 Cube Comprehension 
	#this was done above

#4-10 Slices
#slice = pizzaList[0:3]
#for piece in slice:
#	print("The first three items in the list are: " + piece)

#4-11 My Pizzas, Your Pizzas


#4-12 More Loops


#4-13 Buffet


#4-14 and 4-15
	#I didn't want to change the settings of my IDE but for the most part little would change







	











#Part B
halloweenList = ['bats', 'skulls', 'pumpkins', 'ghosts','spoop','spooky scary scary skeletons']
print(halloweenList)
halloweenInput = input("What is your favorite thing about Halloween? ")
halloweenList.append(halloweenInput)
for spoop in halloweenList:
	print(spoop.title())