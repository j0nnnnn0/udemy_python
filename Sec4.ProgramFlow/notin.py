# Python Programming Class - Udemy 11.10.2021

# Not in

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#--- https://docs.python.org/3/library/stdtypes.html

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): #string method to handle upper/lower case
    print("But I want to go to the cinema!!")
else:
    print("ok, let's go to the {}.".format(activity))