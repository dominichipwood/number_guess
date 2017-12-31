#guess number between 1 and 100, get hints when wrong.

import random
N=random.randrange(1,101)
n=input("A number between 1 and 100. First guess?")
try:
	while n!=N:
		if n>N:
			print("Your too high")
		else:
			print("Too low")
		n=input("Guess again")
	print("Bravo!!")
except:
	print("That's not a number. You have to start again.")
