# Python Programming Class - Udemy 02.11.2021

# Dictionaries and Sets - Sets

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()


# ----------

# sets are unordered
farm_aminals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_aminals)
# {'sheep', 'horse', 'cow', 'goat', 'hen'}
for animal in farm_aminals:
    print(animal)
# sheep
# horse
# cow
# goat
# hen

print()
print("indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)
# indexing a sequence
# goat

# # Cannot index in set
# print("indexing a set is not possible")
# goat = farm_aminals[3]
# print(goat)
# # TypeError: 'set' object is not subscriptable

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_aminals:
    print("the sets are equal")
else:
    print("the sets are different")
# the sets are equal