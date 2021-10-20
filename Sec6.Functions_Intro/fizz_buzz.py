# Python Programming Class - Udemy 20.10.2021

# Functions - Challenge fizz_buzz

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# Write a function called fizz_buzz that returns the next answer
# Start counting in turn
# If number is divisible by 3, say "fizz" instead
# If number is divisible by 5, say "buzz" instead
# If divisble by 3 or 5, say "fizz buzz"

# Function will return a string.
# When you return a number, convert to string first

# Annotate function and include a Docstring

# Include a foor loop to test function for value 1 to 100 incl.

def fizz_buzz(number:int) -> str:
    """Return different strings dependend on input
    If input is divisable by 3, return fizz
    if input is divisable by 5, return buzz
    if input is divisable by 3 or 5 which is 15, return fizz buzz
    else return int as str

    Args:
        number (`int`): A positive number between 1 and 100 inclusive

    Returns:
        `str`: Return a string based on user input
    """
    if number % 15 == 0:
        return "fizz buzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# Test that the function works works
# LOW = 1
# HIGH = 100
# for i in range(LOW, HIGH +1):
#     print("{}: {}".format(i, fizz_buzz(i)))

# 

input("FIZZ BUZZ :\n"
      "Rule:\n"
      "If next number is divisable by \n" 
      "- 3 then type fizz\n"
      "- 5 then type buzz\n"
      "- 3 or 5 then type fizz buzz\n"
      "Else type the number\n"
      "Press ENTER to Start: ")
#input("Please press ENTER to Start: ")
print()

count = 0 #Initialise the count
while count < 15:
    # Computer's turn
    count +=1 # increase count by 1
    print(fizz_buzz(count))
    # Human's turn
    count +=1 # increase count by 1
    answer = input("Your Turn: ") # get an input as answer 
    correct_answer = fizz_buzz(count) # get the correct answer
    if answer != fizz_buzz(count):
        print("You're a Loooooser, correct answer was {}, you entered {}".format(correct_answer, answer))
        break
else :
        print("Winner Winner Chicken Dinner - You Da BEEEEST !!! ")