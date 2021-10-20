# Python Programming Class - Udemy 19.10.2021

# Functions - Handling invalid arguments
# Including Built in exceptions https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/glossary.html#term-parameter
# Docstrings https://www.python.org/dev/peps/pep-0257/
# https://www.python.org/dev/peps/pep-0008/ PEP 8  annotation for default values

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()


# ----

def banner_text(text: str = " ", screen_width: int = 80) -> None: # =80 is the defined parameter value (default value)
    """Print a string centred, with ** on either side.
    This function defines whether the text provided fits within the screen width
    
    Args:
        text (`str` , optional): . Defaults to " ".
        screen_width (`int` , optional): The overall width to print (incl. 4 *). Defaults to 80.

    Raises:
        ValueError: if the supplied string is too long to fit the selected screen width
    """
    if len(text) > screen_width -4:
        raise ValueError("String '{0}' is larger than specified width {1}"
                         .format(text, screen_width))
        
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width -4))
        print(output_string)


banner_text("*",60)
banner_text("Always look on the bright side of life...",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten!",60)
banner_text("And that's to laugh and smile and dance and sing,",60)
banner_text(screen_width=60) #uses the function's default value of " " or declare the function's keyword argument
banner_text("When you're feeling in the dumps,",60)
banner_text("Don't be silly chumps,",60)
banner_text("Just purse your lips and whistle - that's the thing!",60)
banner_text("And... always look on the bright side of life...",60)
banner_text("*",60)

# result = banner_text("Nothing is returned")
# print(result) # returns none
