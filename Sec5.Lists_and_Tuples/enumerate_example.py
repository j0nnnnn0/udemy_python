# Python Programming Class - Udemy 12.10.2021

# Lists - enumerate example

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# --

parts = "abcdefgh"
for index, character in enumerate(parts):
    print(index,character)