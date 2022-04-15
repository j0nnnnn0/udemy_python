
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets -Subsets and Supersets


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
animals = {"Turtle",
           "Horse",
           "Robin",
           "Python",
           "Swallow",
           "Hedgehog",
           "Wren",
           "Aardvark",
           "Cat"
        }

birds = {"Robin", "Swallow", "Wren"}

#using the subset method

print(f"birds is a subset of animals: {birds.issubset(animals)}")
# birds is a subset of animals: True  
print(f"animals is a superset of birds: {animals.issuperset(birds)}")
# animals is a superset of birds: True

print(f"birds is a superset of animals: {birds.issuperset(animals)}")
# birds is a superset of animals: False  
print(f"animals is a subset of birds: {animals.issubset(birds)}")
# animals is a subset of birds: False

# Using operator
print(birds <= animals) #subset
print(birds < animals) # proper subset

# operator vs mehtod
print("*" * 80) 

garden_birds = {"Robin", "Swallow", "Wren"}
print(garden_birds == birds)
# True
print(garden_birds <= birds) # is subset
# True
print(garden_birds < birds) # is proper subset
# False

print("*" * 80) 

more_birds = {"Wren", "Budgie", "Swallow"}
print(garden_birds >= more_birds) # is superset
# False