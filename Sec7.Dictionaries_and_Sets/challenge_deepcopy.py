# Python Programming Class - Udemy 31.10.2021

# Dictionaries and Sets - Challenge Deep Copy
# https://docs.python.org/3/library/stdtypes.html#dict.copy


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
# Create a new empty dict ()
# Iterate over the keys and values of the dict that is being copied (recipes)
# for each key copy value, then add the copy of the value to the new dict
# use copy method

from contents import recipes

def my_deepcopy(d: dict) -> dict:
    """[summary] Copy a dict, creating copies of the `list` or `dict` values

    Args:
        d (dict): [description] dict to copy

    Returns:
        dict: [description] a copy of `d` with the using copies of the original values.
    """
    new_dict = {}
    
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
        
    return new_dict


recipes_copy = my_deepcopy(recipes)

recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])

# Expected output
# 300
# 3