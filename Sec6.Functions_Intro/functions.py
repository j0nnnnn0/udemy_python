# Python Programming Class - Udemy 17.10.2021

# Functions

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# Defining a new function:
def multiply(x, y): # Define nameOfFunction(parameters)
    """Multiply two `int` values
    
    The function will return the product of two arguments x and y.
    
    Args:
        x (`int`): first argument
        y (`int`): second argument

    Returns:
        [`int`]: The returned product 
    """
    result = x * y
    return result # need to return the code, if omitted returns 0
# two break lines for function (pep8)


answer = multiply(18,3)
print(answer)

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


# Palindrome
def is_palindrome(string):
    #  backwards = string[::-1] # slice reverses the original string
    #  return backwards == string # evaluate true or false
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome". format(word))
# else:
#     print("'{}' is not a palindrome".format(word))