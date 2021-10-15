# Python Programming Class - Udemy 11.10.2021

# For Loops

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#-----

# parrot = "Norwegian Blue"

# for character in parrot:
#     print(character)

# --- https://docs.python.org/3/library/functions.html Built-in functions

#number = "9,223;372 036|854,775-807"
number = input("Please enter a series of numbers, using any seperators you like: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val)for val in values])
print(sum([int(val)for val in values])) # sum of the values in iterable values

