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

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print()
print(computer_parts[0:3])
print(computer_parts[-1])
