# Python Programming Class - Udemy 19.10.2021

# Functions - Challenge

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# https://docs.python.org/3/library/stdtypes.html#str.isalnum -> String method
    # str.isalnum()
        # Return True if all characters in the string are alphanumeric 
        # and there is at least one character, False otherwise. 
        # A character c is alphanumeric if one of the following returns True: 
        #   c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().

# Evaluate if a sentence is a palindrome, considers only alphanumeric characters

# Tests: 
# Was it a car, or a cat, I saw?
# Do gess see god?
# Desnes not far, Rafton sensed.
from functions import is_palindrome


def palindrome_sentence(sentence:str) -> bool: # function
    """Return a `boolean` if sentence is a palindrome (same letters forward and backwards)
    The function ignores whitespace, capitalisation and punctuation.

    Args:
        string (`string`): The sentence that the user will be prompted to enter.

    Returns:
        [`boolean`]: True if `sentence`is a palindrome, else False
    """
    string = "" # declare an empty string
    for char in sentence:
        if char.isalnum(): # built in method to check if character is alphanumeric
            string += char

#    print(string, "|", string[::-1]) # check output 
    return is_palindrome(string) # calling a function in a function
#    return string[::-1].casefold() == string.casefold()

word = input("Please enter a word to check: ")

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


#Fibonacci
def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number for positive integer `n`

    Args:
        n (`int`): the number that the user will be prompted to enter 
    """
    if 0 <= n <=1:
        return n
    
    n_minus1, n_minus2 = 1, 0
    
    result = None
    for f in range (n -1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    
    return result


number = int(input("Please enter a postive number: "))
for i in range(number):
    print ("{}: {}".format(i +1, fibonacci(i)))
    

w = is_palindrome()
p = palindrome_sentence(242)