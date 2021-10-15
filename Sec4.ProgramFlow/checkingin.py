# Python Programming Class - Udemy 12.10.2021

# in and not in

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#---

parrot = "Norwegian Blue"

letter=input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't need that letter")