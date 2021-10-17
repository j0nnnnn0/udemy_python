# Python Programming Class - Udemy 17.10.2021

# Split method

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

# ---

panagram = """The quick brown
fox jumps \tover
the lazy dog"""

words = panagram.split()
# when the split method argument is empty, defaults to space, tab
print(words)
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))
# ['9', '223', '372', '036', '854', '775', '807']

print()
# ----
generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7',    
]

values = "".join(generated_list)
print("joined list: {}".format(values))
# joined list: 9 223 372 036 854 775 807

values_list = values.split()
print("split lists: {}".format(values_list))
# split lists: ['9', '223', '372', '036', '854', '775', '807']

# Challenge
# Use a for loop to produce a list of ints rather than strings
# Either modify the contents of the values_lists 
# or create a new list of ints

# replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)
# [9, 223, 372, 36, 854, 775, 807]

# create a new list of ints
int_values = []
for value in values_list:
    int_values.append(int(value))
print(int_values)
# [9, 223, 372, 36, 854, 775, 807]