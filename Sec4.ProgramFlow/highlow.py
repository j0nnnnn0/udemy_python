# Python Programming Class - Udemy 12.10.2021

# Binary Search

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

low = 1
high = 10

print("Please think of a number between {} and {}.".format(low,high))
input("Press Enter to start. ")

#guess = 1
guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess is correct : "
                    .format(guess)).casefold()
    
    if high_low == "h":
        #Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1 
    elif high_low == "l":
        #Guess lower. the high end of the range becomes 1 smaller than the guess
        high = guess - 1
    elif high_low == "c":
        print("Yeah, I'm so smart, I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")
        
    guesses += 1
else: # no break / completed
    print("You thought of the number {}.".format(low))
    print("I got it in {} guesses.".format(guesses))
