import json

fav_number = input("What is your favorite number? ")

filename = 'favnumber.json'
with open(filename, 'w') as f_obj:
	json.dump(fav_number, f_obj)
	print("Storing your favorite number as: " + fav_number + ".")
	
with open(filename) as f_obj:
	fav_number = json.load(f_obj)
	print("I know your favorite number it's " + fav_number + "!")