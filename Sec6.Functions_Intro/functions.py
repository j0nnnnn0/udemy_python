# Python Programming Class - Udemy 17.10.2021

# Functions

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

def multiply(): # Define nameOfFunction(parameters)
    result = 10.5 * 4
    return result # need to retun the code
# two break lines for function (pep8)


answer = multiply()
print(answer)
