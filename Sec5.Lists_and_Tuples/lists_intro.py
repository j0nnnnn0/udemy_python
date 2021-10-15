# Python Programming Class - Udemy 12.10.2021

# Lists

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

# for part in computer_parts:
#     print(part)

# print()
# print(computer_parts[2])

# print()
# print(computer_parts[0:3])
# print(computer_parts[-1])


print(computer_parts)

# computer_parts[3]= "track ball" #s[1] = x
print(computer_parts[3:])

computer_parts[3:] = "trackball" # think trackball is a list ie iterable
computer_parts[3:] = ["trackball"] # replace a sec of the list with another part of a list
print(computer_parts)
