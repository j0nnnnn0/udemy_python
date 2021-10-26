# Python Programming Class - Udemy 23.10.2021

# Dictionaries and Sets - Using default values

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

from contents import pantry

#setdefault returns the value of a key, if the key exists
# Furthermore, it adds the key if it doesn't exist.
chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

# Get returns the key from the list but does NOT add the key to the dict.
ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("`pantry` now contains....")

for key, value in sorted(pantry.items()):
    print(key, value)