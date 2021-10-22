# Python Programming Class - Udemy 22.10.2021

# Dictionaries and Sets - Using Dict in a menu


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

# Import the contents (pantry items and recipies from contents.py)
from contents import pantry, recipes

print(pantry)
print()
print(recipes)



