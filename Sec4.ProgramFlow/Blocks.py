# Python Programming Class - Udemy 11.10.2021

# Blocks and Statements

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# # Last print is part of Block so runs iteratively as part of for looop
# for i in range(1,13):
#     print("No. {} square is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)

# # Different output as last print is not part of block so runs once after for loop
# for i in range(1,13):
#     print("No. {} square is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
# print("*" * 80)


cls()
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print("{0}, you are {1} years old".format(name,age))

# Conditions
# if age >= 18:
#     print("{0}, you are old enough to vote".format(name))
#     print("Please put an X in the box.")
# else:
#     print("{0}, please come back in {1} year(s) to vote".format(name, 18 - age))

# same conditions but the other way round
if age < 18:
    print("{0}, please come back in {1} year(s) to vote".format(name, 18 - age))
elif age == 900:
    print("Sorry, {0}, you die in Return of the Jedi".format(name))
else:    
    print("{0}, you are old enough to vote".format(name))
    print("Please put an X in the box.")