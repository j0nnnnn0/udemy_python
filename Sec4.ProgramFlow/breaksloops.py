# Python Programming Class - Udemy 12.10.2021

# Break in loops

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# -----

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for i in shopping_list:
#     if i == "spam":
#         break # causes the loop to stop if true 
#     print("Buy " + i)
    
cls()

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
print(shopping_list)

item_to_find = input("Enter an item: ")
found_at = None # constant that represents "nothing"

# # for index in range(6):
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break


# Better alternative
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("{0} found at position {1} out of {2} in the shopping list.".format(item_to_find, found_at, len(shopping_list)))
else:
    print ("{} is not in the shopping list".format(item_to_find))
