# Python Programming Class - Udemy 12.10.2021

# Lists - enumerate example
# Tuples - enumerate example

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# -- list
# parts = "abcdefgh"
# for index, character in enumerate(parts):
#     print(index,character)
# print()

for index, character in enumerate("abcdefg"):
    print(index, character)

# -- unpacking a Tuple
for t in enumerate("abcdefg"):
    index, character = t
    print(index, character)
    
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
print()

index, character = (0, 'a')
print(index)
print(character)