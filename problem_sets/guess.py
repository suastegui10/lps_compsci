# this tells the computer to choose a random number so that the player can guess it during the game
import random
# this will tell the player to choose a number between one and a thousand
special_number = random.randint(1,1000)
print("I'm thinking of a number between 1 and 1000. Guess what number it is.")
guess = 0 
while guess != special_number:
	guess = int(raw_input())
# what this is going to do is that if the number the player guesses is greater than the special number, it will print that it is too high and try again
	if guess > special_number:
		print("Nope, too high! Try again.")
# this is going to tell the player that the number is too low so they have to try again because the number they guessed was lower than the number it actually is
	elif guess < special_number:
		print("Nope, too low! Try again.")
# if the player guesses the right number, then it will let the player know they won
	else:
		print("Congrats, you win!")
		break 
