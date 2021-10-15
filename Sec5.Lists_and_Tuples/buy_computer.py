# Python Programming Class - Udemy 12.10.2021

# Lists - append, iterate and enumerate

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

available_parts = ["computer", 
                   "monitor",
                   "keyboard",
                   "mouse",
#                   "mouse mat",
                   "hdmi cable",
                   "DVD drive"
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
