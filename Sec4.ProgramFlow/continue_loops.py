# Python Programming Class - Udemy 12.10.2021

# Continue in loops

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# -----

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for i in shopping_list:
#     if i !='spam':
#         print("Buy " + i)

for i in shopping_list:
    if i == "spam":
        continue # causes all remaining code in block to be skipped
    print("Buy " + i)