# Python Programming Class - Udemy 31.10.2021

# Dictionaries and Sets - Challenge Deep Copy
# https://docs.python.org/3/library/stdtypes.html#dict.copy

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()


# ----------

from challenge_deepcopy import my_deepcopy
import copy

original = {
    "Tim" : ["Buchalka", ["Programmer", "Teacher"]],
    "J-P" : ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(f"original: {original}")
print(f"copy_1:   {copy_1}")
print(f"copy_2:   {copy_2}")