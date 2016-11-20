print("Welcome to Asael's quest!")

print("What is the name of your character?")
character_name = raw_input()
print("Enter the strength of your character from 1-10")
strength = raw_input()
print("Enter the health of your character from 1-10")
health = raw_input()
print("Enter the luck of your character from 1-10")
luck = raw_input()
total = strength + health + luck 
sum = int(luck) + int(strength) + int(health)
if sum > 15:
	strength = 5
	health = 5
	luck = 5
	print("You have given your character too many points! Default values have been assigned, ") 
	
	print("Your health is:" + str(health) + "your strength is:" + str(strength) + "your luck is:" + str(luck))
if sum <= 15:
	print("Your character name is " + character_name + " your strength is " + str(strength) + " your health is " + str(health) + " your luck is " + str(luck))
print(str(character_name) + " has come across a fork in the road! Do you want to go left or right? Enter 'left' or 'right'. ")
direction = raw_input()

if direction == 'left' and strength < 4:
	print("It seems that you aren't strong enough to carry you and your backpack up this hill!")
elif direction == 'left' and strength > 4:
	print("Nice! You are strong enough to get over the hill!")
if direction == 'left' and health < 4: 
	print("You are not healthy enough to get through this weather! Sorry.")
elif direction == 'left' and health > 4:
	print("You are healthy enough to survive this weather. Keep going!")
if direction == 'left' and luck < 4:
	print("Sorry, you are unlucky because a bear appeared and ate you.")
elif direction == 'left' and luck > 4:
	print("You are so lucky! A bear appeared but decided to go for the other player who did not have luck on his side today.")

if direction == 'right' and strength < 4:
	print("Sorry, you aren't strong enough to get through this wind. It's pushing you back!")
elif direction == 'right' and strength > 4:
	print("Yay! You have enough leg stength! The wind can't hold you back!Keep going!")
if direction == 'right' and health < 4:
	print("Sorry, the dust from the wind got your lungs and couldn't handle it. You are not healthy enough to keep going. You lose.")
elif direction == 'right' and health > 4:
	print("Thanks to your health, you can handle the dust and it isn't affetcing you. Keep moving forward!")
if direction == 'right' and luck < 4:
	print("Sorry, you were unlucky and a mob of lions attacked you! You lose.")
elif direction == 'right' and luck > 4:
	print("A group of people with weapons were on their way up the hill and helped you escape the mob of lions! You got lucky, keep going!")


