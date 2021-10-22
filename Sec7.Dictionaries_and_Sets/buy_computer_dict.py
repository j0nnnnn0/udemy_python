# Python Programming Class - Udemy 21.10.2021

# Dictionaries and Sets - Using Dict in a menu

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

available_parts = {
                    "1" : "computer",
                    "2" : "monitor",
                    "3" : "keyboard",
                    "4" : "mouse",
                    "5" : "hdmi cable",
                    "6" : "dvd drive",
                    }

current_choice = None
computer_parts = {} # create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            # Adding to chosen part
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains {computer_parts}")
    else:
        print("Please select options from the list")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("0: to finish")
    current_choice = input("> ")
print("bye bye")


