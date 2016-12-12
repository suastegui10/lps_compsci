print("Welcome to PumaPix!")
#this is going to ask the person to input their top five favorite shows
print("Enter your 5 favorite TV shows")
shows = 0
favs = []
#this is going to put the shows in a list and not allow for more than five to be put down
while shows < 5:
	print("Enter your show name:")
	tv = raw_input()
	favs.append(tv)
	shows = shows + 1
#this will show them what they put and will also print that they added some better shows
print("Ok, here's what you entered:" + str(favs))
print("We added some shows that are better")
#this will set the variable better_shows to Spongebob and Fuller House 
better_shows = ["Spongebob" , "Fuller House"]
together = favs + better_shows
#this will sort the shows and then put them in order in a list
together.sort()
y = 0
for x in together:
	y = y + 1
	print(str(y) + "." + x)

