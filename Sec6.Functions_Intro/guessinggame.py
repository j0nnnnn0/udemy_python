# Python Programming Class - Udemy 19.10.2021

# Functions - Returning values

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()


# ----

import random


# Using a function to ensure the input is an int
def get_integer(prompt): # built in prompt
    """Get an integer from Standard Input (stdIn).
    
    The function will continue looping and prompting
    the user, until a valid `int` is entered.

    Args:
        prompt (`string`): The String that the user will see when 
        they are prompted to enter the value.

    Returns:
        `int`: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
#        else:
        print("{} is not a valid number.".format(temp))


help(get_integer)
# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
    
guess = ""
while guess != answer:
    guess = get_integer(": ")

    if guess == answer:
        print("well done, that's the answer")
        break
    elif guess == 0:
        print("Ok, bye")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print ("Please guess lower")


# Exercise
# tree1 = 'Pine tree'
# tree2 = 'Apple tree'

# if tree1 == tree2:
#     print("The Trees are the same.")
# else:
#     print("The trees are different.")

# x = 5
# y = 7

# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")



# if guess < answer:
#     print("{0} is too low. Please try again: ".format(guess))
#     guess = int(input())
#     if guess == answer:
#         print("Well Done, you guess it")
#     else:
#         print("Sorry. Still incorrect")
# elif guess > answer:
#     print("{0} is too high. Please try again".format(guess))
#     guess = int(input())
#     if guess == answer:
#         print("Well Done, you guess it")
#     else:
#         print("Sorry. Still incorrect")
# else:
#     print("First try - well done, {0} is the correct answer".format(guess))

# # A smarter way
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print ("Well done, you guessed right")
#     else:
#         print("Sorry, you haven't guessed correctly")
# else:
#     print ("well done, you got it first time")