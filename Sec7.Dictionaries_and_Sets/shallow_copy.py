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

# mutable as each value in dict is a list
animals = {
    "lion" : ["scary", "big", "cat" ], 
    "elephant" : ["big", "grey", "wrinkled"],
    "teddy" : ["cuddly", "stuffed"],
}

things = animals.copy() # create a copy of original dict
print(things["teddy"])
print(animals["teddy"])
# ['cuddly', 'stuffed']       
# ['cuddly', 'stuffed']   
print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
# Both dict are updated, but why?
# ['cuddly', 'stuffed', 'toy']
# ['cuddly', 'stuffed', 'toy']