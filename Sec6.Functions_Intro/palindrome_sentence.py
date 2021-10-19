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

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum(): # built in method to check if character is alphanumeric
            string += char

    print(string, "|", string[::-1])
    return string[::-1].casefold() == string.casefold()

word = input("Please enter a word to check: ")

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
