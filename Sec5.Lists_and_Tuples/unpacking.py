# Python Programming Class - Udemy 17.10.2021

# Tuples - Unpacking
# Tuples are "Immutable"
# Tuples can always be unpacked successfully

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

a = b = c = d = e = f = 12 # bind all variables to the same value
print(c)

x, y, z = 1, 2, 42 # this is a tuple
print("x: ",x)
print("y: ",y)
print("z: ", z)
print()

# -- unpacking a tuple
print("Unpacking a tuple")
data = 1, 2, 76 # data represents a tuple
x, y, z = data
print("x: ",x)
print("y: ",y)
print("z: ", z)
print()

# unpacking a list (but because it's mutable 
# this could generate errors if list is changed)
print("Unpacking a list")
data_list = [12, 13, 14]
# data_list.append(15) # this mutates the list and will crash program

p, q, r = data_list
print("p: ", p)
print("q: ", q)
print("r: ", r)

#   File "c:\Users\Jonat\Documents\code\udemy_python\Sec5.Lists_and_Tuples\unpacking.py", line 37, in <module>
#     p, q, r = data_list
# ValueError: too many values to unpack (expected 3)