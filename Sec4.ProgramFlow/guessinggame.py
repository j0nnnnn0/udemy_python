# Python Programming Class - Udemy 11.10.2021

# More on if, elif and else

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

import random

highest = 1000
answer = random.randint(1, highest)
#print(answer) # TODO: remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
    
guess = ""
while guess != answer:
    guess = int(input())

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