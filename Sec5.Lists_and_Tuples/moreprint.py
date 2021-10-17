# Python Programming Class - Udemy 17.10.2021

# Print - Revisited

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# ---
name = "Jonathan"
age = 10

print(name, age, "Python", 2020)
# Jonathan 10 Python 2020

# sep is seperator (only work if more than one value)
print(name, age, "Python", 2020, sep=", ")
# Jonathan, 10, Python, 2020
