# Python Programming Class - Udemy 17.10.2021

# Functions

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

def multiply(x, y): # Define nameOfFunction(parameters)
    result = x * y
    return result # need to retun the code
# two break lines for function (pep8)


def is_palindrome(string):
    #  backwards = string[::-1] # slice reverses the original string
    #  return backwards == string # evaluate true or false
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome". format(word))
else:
    print("'{}' is not a palindrome".format(word))





# answer = multiply(10.5, 4) # matches the parameter in the function
# print(answer)
# # 42.0

# fourty_two = multiply(6,7)
# print(fourty_two)
# # 42

# # functions can be used in a loop
# for val in range(1, 5): 
#     two_times = multiply(2, val)
#     print(two_times)
# # 2   
# # 4   
# # 6   
# # 8