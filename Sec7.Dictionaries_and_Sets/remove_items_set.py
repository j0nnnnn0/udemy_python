# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - Deleting items from a set


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

small_ints = set(range(21))
print(small_ints, type(small_ints))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20} <class 'set'> - sets are unordered

# https://docs.python.org/3/library/stdtypes.html#set