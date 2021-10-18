# Python Programming Class - Udemy 15.10.2021

# Lists - append, iterate and enumerate

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

# Additional Tasks:
    # Add more items 
    # Change Available_parts list to store tuples
    # Each tuple to include name and price
    # Display price and total price
# ----


available_parts = [
    ("computer", "HP",
        [
            ("name", "HP-001"),
            ("price", 800),
        ]
    ),
    ("monitor", "Dell",
        [
            ("name", "Dell-002"),
            ("price", 300),
        ]
    ),
    ("keyboard", "Logitech",
        [
            ("name", "G815 (Tactical)"),
            ("price", 150),
        ]
    ),
    ("mouse", "Logitech",
        [
            ("name", "Pro Wireless X"),
            ("price", 99.99),
        ]
    ),
    ("hdmi cable", "ACME Distribution",
        [
            ("name", "Pro HDMI 2.0 braded"),
            ("price", 34.59),
        ]
    ),
    ("printer", "EPSON",
        [
            ("name", "Epson Office Pro A3"),
            ("price", 478),
        ]
    )
                ]

valid_choices = []
# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
print("valid choices are : ",valid_choices)

current_choice = "-" # initialise the variable
computer_parts = [] # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) -1 # substract 1 from each current_choice to match indexing of available_parts
        chosen_part = available_parts[index] # chosen_part is the index of available_parts
        if chosen_part in computer_parts:
            #Already in so Remove
            print("Removing {}.".format(current_choice))
            computer_parts.remove(chosen_part)
            print("You list now contains: {}".format(computer_parts))
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part) # add the chosen_part (itself the index of available parts) to the computer_parts list
            print("You list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below, Press 0 to end: ")
        for number, part in enumerate(available_parts): # using enumeration
            print("{}: {}".format(number + 1, part))
   
    current_choice = input("Make your selection: ")

print("You have selected {} items: {}".format(len(computer_parts), computer_parts))
