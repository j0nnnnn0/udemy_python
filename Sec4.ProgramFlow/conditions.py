# Python Programming Class - Udemy 11.10.2021

# Conditions

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#-----

#Are you of working age between 16 and 65


age = int(input("how old are you?"))

# minage = 16
# maxage = 65
# if age < minage or age > maxage:
#     print("You are not of working age")
# else:
#     print("You are of working age")

# if age >= 16 and age <= 65: 
if 16 <= age <=65: # as an Alternative
    print("Have a good day at work")
else:
    print("Happy chilling out")
    
print ("-" * 80)

if age < 16 or age > 65: # as an Alternative
    print("Happy chilling out")
else:
    print("Have a good day at work")