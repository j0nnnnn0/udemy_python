# Python Programming Class - Udemy 12.10.2021

# Booleans

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#-----

day = "Saturday"
temperature = 30
raining = True

# if day == "Saturday" and temperature > 27 and not raining:
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")
    
#---- 
# https://docs.python.org/3/library/stdtypes.html

if 0:
    print("True")
else:
    print("False")
    
# name = input("Please enter your name: ")
# if name !="":
#     print("Hello, {}".format(name))
# else:
#     print("Are you the man with no name?")