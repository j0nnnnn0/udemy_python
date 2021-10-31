# Python Programming Class - Udemy 31.10.2021

# Dictionaries and Sets - Other methods for Dict
# https://docs.python.org/3/library/stdtypes.html#dict


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv" : "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# # fromkey methods allows to default a value to each key
# https://docs.python.org/3/library/stdtypes.html#dict.fromkeys

# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
# # dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# d. method iterates over the keys of a dict
# https://docs.python.org/3/library/stdtypes.html#dict.values

# keys = d.keys()
# print(keys)

# for item in d.keys():
#     print(item)
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9

# # Update method
# # Update a dict with new key, value pairs
# # https://docs.python.org/3/library/stdtypes.html#dict.update

# d2 = {
#     7 : "lucky seven",
#     10 : "ten",
#     3 : "this is the new three",
# }

# d.update(d2)
# # Updating the value of the key in a dict doesn't change its position
# for key, value in d.items():
#     print(key,value)
# # 0 zero
# # 1 one
# # 2 two
# # 3 this is the new three
# # 4 four
# # 5 five
# # 6 six
# # 7 lucky seven
# # 8 eight
# # 9 nine
# # 10 ten

# cls()

# # Update a dict with a list, enumerate over the list then update with key with value 
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key,value)
# # 0 chicken
# # 1 spam
# # 2 egg
# # 3 bread
# # 4 lemon
# # 5 five
# # 6 six
# # 7 lucky seven
# # 8 eight
# # 9 nine
# # 10 ten

v = d.values()
print(v)
# dict_values(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
# 'seven', 'eight', 'nine'])

# https://docs.python.org/3/library/stdtypes.html#dict-views
d[10] = 'ten'
print(v)
# dict_values(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
# 'seven', 'eight', 'nine', 'ten'])

print("four" in v)
print("eleven" in v)
# True
# False

# transform keys and values into a list in order to find the key from a value
# only finds first occurence of match
keys = list(d.keys())
values = list(v) # => list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")
# four was found with the key 4

print()

#Alternative to above
# finds all occurences of match
for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")
# four was found with the key 4
# four was found with the key iv

# Copy method copy()
# https://docs.python.org/3/library/stdtypes.html#dict.copy
