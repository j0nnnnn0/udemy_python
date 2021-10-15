# Python Programming Class - Udemy 11.10.2021

# For loop Challenge 
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# Use a for loop and an if statement to print just the capitals in the quote above.
# https://docs.python.org/3/library/stdtypes.html#string-methods
# check out the string method for one way to test if a character is in upper case
# https://docs.python.org/3/library/stdtypes.html#str.isupper

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for char in quote:
    if char.isupper():
        print(char)
