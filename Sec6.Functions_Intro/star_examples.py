# Python Programming Class - Udemy 20.10.2021

# Functions - *args

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")

# print(*numbers, sep=";") # * unpacks individual values and passes to function(print)
# # above is to below
# print(0,1,2,3,4,5, sep=";")

def test_star(*args): #represents an unpacked tuple
    print(args)
    for x in args: 
        print(x)

test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
