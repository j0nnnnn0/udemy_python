# Python Programming Class - Udemy 17.10.2021

# Functions
# https://docs.python.org/3/library/typing.html Typing - support for type hints
# https://www.python.org/dev/peps/pep-3107/ Function Annotation
# https://www.python.org/dev/peps/pep-0008/ PEP 8  annotation for default values

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# Defining a new function:
def multiply(x: float, y: float) -> float: # Define nameOfFunction(parameters)
    """Multiply two `float` values
    
    The function will return the product of two arguments x and y.
    
    Args:
        x (`float`): first argument
        y (`float`): second argument

    Returns:
        [`float`]: The returned product 
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
def is_palindrome(string:str) -> bool:
    """Return a `boolean` if argument is a palindrome (same letters forward and backwards)

    Args:
        string (`string`): The string that the user will be prompted to enter

    Returns:
        [`boolean`]: True or False
    """
    #  backwards = string[::-1] # slice reverses the original string
    #  return backwards == string # evaluate true or false
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome". format(word))
else:
    print("'{}' is not a palindrome".format(word))
    
p = is_palindrome()