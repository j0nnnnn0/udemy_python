# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - Deleting items from a set


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

small_ints = set(range(21))
print(small_ints, type(small_ints))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20} <class 'set'> - sets are unordered

# https://docs.python.org/3/library/stdtypes.html#set

# small_ints.clear() # clear method 
# print(small_ints, type(small_ints))
# # set() <class 'set'>

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20}

small_ints.discard(99)
print(small_ints)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20}

small_ints.remove(99)
print(small_ints)
# KeyError: 99

# Difference between Discard vs Remove
# discard ensures something no longer exists whether it was there or not
# remove must exists as it provides a notification if it doesn't (keyerror above)

# see packing_list.py for Discard example
# see prescription_data.py & prescription_trial.py for Remove example
# see prescription_processing.py for pop example
