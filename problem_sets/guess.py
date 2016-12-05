import random

special_number = random.randint(1,1000)
print("I'm thinking of a number between 1 and 1000. Guess what number it is.")
guess = 0 
while guess != special_number:
	guess = int(raw_input())
	if guess > special_number:
		print("Nope, too high! Try again.")
	elif guess < special_number:
		print("Nope, too low! Try again.")
	else:
		print("Congrats, you win!")
		break 
