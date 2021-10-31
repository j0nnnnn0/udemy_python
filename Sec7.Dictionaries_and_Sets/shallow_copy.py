# Python Programming Class - Udemy 31.10.2021

# Dictionaries and Sets - Other methods for Dict - Copy
# https://docs.python.org/3/library/stdtypes.html#dict.copy


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

# # imutable as values are part of dict
# animals = {
#     "lion" : "scary",
#     "elephant" : "big",
#     "teddy" : "cuddly",
# }

# things = animals
# animals["teddy"] = "toy"
# print(things["teddy"])
# # toy

# things = animals.copy() # create a copy of original dict
# animals["teddy"] = "toy"
# print(things["teddy"])
# print(animals["teddy"])
# # cuddly
# # toy 

# --- 
import copy

# mutable as each value in dict is a list
animals = {
    "lion" : ["scary", "big", "cat" ], 
    "elephant" : ["big", "grey", "wrinkled"],
    "teddy" : ["cuddly", "stuffed"],
}

# Perform a "shallow" copy of original dict
things = animals.copy() 

# Perform a "deep" copy of the original dict
# things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])
# ['cuddly', 'stuffed']       
# ['cuddly', 'stuffed']   
print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
# Shallow copy both dict are updated
# ['cuddly', 'stuffed', 'toy']
# ['cuddly', 'stuffed', 'toy']

# Deep copy, only animals is updated with new value
# ['cuddly', 'stuffed', 'toy']
# ['cuddly', 'stuffed']   

# Using shallow copy, both dict are the same
# 2220420422272 ['cuddly', 'stuffed']
# 2220420422272 ['cuddly', 'stuffed']

# Using deep copy, the two dicts have different IDs so are distinct
# 2582497676160 ['cuddly', 'stuffed', 'toy']
# 2582497581504 ['cuddly', 'stuffed']     