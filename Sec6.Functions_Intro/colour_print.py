# Python Programming Class - Udemy 20.10.2021

# Functions - printing in colours

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# print(RED, "This will be in red")
# print("and so is this")

def colour_print(text: str, effect: str) -> None:
    """Print text using the ANSI sequences to change colour, etc.

    Args:
        text (`str`): The Text to print
        effect (`str`): The effect we want. One of the contants defined in this module
    """
    output_string = "{}{}{}".format(effect,text, RESET)
    print(output_string)

colour_print("Hello, Red", RED)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)