# number 2
# this prints "Welcome to the convenience store and "Enter your age". Then it tells you to input your age
print("Welcome to the convenience store!")
print("Enter your age:")
age = input()
# This turns your age into an integer
age = int(age)
# This says if you are greater than or equal to to the age of 18, then it will ask if you want to buy a lottery ticket
if age >= 18:
  print("Would you like to buy a lottery ticket?")
# This one tells you that if your age is less than 6, then it will ask you if you want to buy a lollipop
if age < 6:
  print("Would you like to buy a lollipop?")
