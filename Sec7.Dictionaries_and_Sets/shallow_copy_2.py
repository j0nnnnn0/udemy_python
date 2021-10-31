# Python Programming Class - Udemy 31.10.2021

# Dictionaries and Sets - Other methods for Dict - Copy
# https://docs.python.org/3/library/stdtypes.html#dict.copy


# A shallow copy copies references. 
# It doesn't make a copy of the things that are being referred to.

# For a deep copy see https://docs.python.org/3/library/copy.html

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

# Python creates a list object in memory and links the lists object
# to the key in the dict equivalent to :

lion_list = ["scary", "big", "cat" ]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

# values are mutable as each value is a list
animals = {
    "lion" : lion_list, 
    "elephant" : elephant_list,
    "teddy" : teddy_list,
}

things = animals.copy() # create a copy of original dict
# # the copy method is equivalent to creating a new dict things with value of our lists
# things = {
#     "lion" : lion_list, 
#     "elephant" : elephant_list,
#     "teddy" : teddy_list,
# }

print(things["teddy"])
print(animals["teddy"])
# ['cuddly', 'stuffed']       
# ['cuddly', 'stuffed']   
print()

# things["teddy"].append("toy")
# above is equivalent to appending the teddy_list 
teddy_list.append("toy")

# appending values to the value lists
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")

print(things["teddy"])
print(animals["teddy"])
# Both dict are updated
# ['cuddly', 'stuffed', 'toy']
# ['cuddly', 'stuffed', 'toy']
print(teddy_list)
# ['cuddly', 'stuffed', 'toy', 'added via `animals`', 'added via `things`']
# ['cuddly', 'stuffed', 'toy', 'added via `animals`', 'added via `things`']
# ['cuddly', 'stuffed', 'toy', 'added via `animals`', 'added via `things`']