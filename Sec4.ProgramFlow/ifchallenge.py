# Python Programming Class - Udemy 11.10.2021

# If Challenge

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#----
print("Welcome to the 18-30 Holiday checker")
name = input("Please enter your name? ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("{0}, welcome to the holiday".format(name))
else:
    print("Sorry {0}, you are not eligible for this holiday".format(name))