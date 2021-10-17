# Python Programming Class - Udemy 16.10.2021

# Lists -  Nested List -  Challenge
# join

import os
from types import SimpleNamespace
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# print out all the meals in the menu but with spam removed
# You can either:
#   Remove spam from each list, then print the list
#   Print out the items in each list as long as it is not spam

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    # trailing comma is redundent but helps style
]

getoff = "spam"


# Remove spam from each list and print
#Spilt the lists in meal
# Loop each meal from its last index
# delete index of meal if equal to spam
# print meal

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == getoff:
            del meal[index]
    print(", ".join(meal))
        

#   Print out the items in each list as long as it is not spam
# loop meal through the menu
# loop through each meal 
# if items in meal not spam, print
# for meal in menu:
#     for item in meal:
#         if item != getoff:
#             print(item, end = ", ")
#     print()