# Python Programming Class - Udemy 16.10.2021

# Lists -  Nested List

# Style Guide : https://www.python.org/dev/peps/pep-0008/ (search for list)
# The closing brace/bracket/parenthesis on multiline constructs may either
# line up under the first non-whitespace character of the last line of list, as in:
# my_list = [
#     1, 2, 3,
#     4, 5, 6,
#     ]
# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f',
#     )

# Google Python Style Guide : https://google.github.io/styleguide/pyguide.html

# %%
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# ---- Use format Document (Shift+Alt+F in VSCode)
# %%
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    # trailing comma is redundent but helps style
]

# %%
# Processing the list
for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))
