
# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - Deleting items from a set : Discard method


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel: ")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    
mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    #travelling by plane, remove restricted items
    for restricted_item in restricted_items:
        # items.discard(restricted_item) # good solution to discard items from our packing list
        # items.remove(restricted_item) # will generate an keyerror
        # items -= restricted_items # using the difference operator
        items.difference_update(restricted_items) # using the difference_update method
print("You need to pack: ")
for item in sorted(items):
    print(item)
