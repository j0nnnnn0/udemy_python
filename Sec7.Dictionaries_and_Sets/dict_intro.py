# Python Programming Class - Udemy 21.10.2021

# Dictionaries and Sets - Intro

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---
# key is the index

vehicles = {
    'dream' : 'Honda 250T',
    'er5' : 'Kawasaki ER5',
    'can-am' : 'Bombardier Can-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha XT650',
    'jimny' : 'Suzuki Jimny 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4',
    'roadster' : 'Triumph Street Triple',
}

# Using key indexing (faster)
my_car = vehicles['fiesta'] # use brackets to retrieve value
print(my_car)

# keys are sensitive so a wrong key will generate an error
# my_car = vehicles['Fiesta']
# print(my_car)
# # KeyError: 'Fiesta'

commuter = vehicles['virago']
print(commuter)

# Dictionaries have a get method
learner = vehicles.get("er5")
print(learner)

# Dictionaries have a get method - if key is incorrect, returns None
learner = vehicles.get("ER5")
print(learner)
# None

cls()
# Iterating over keys

# for loop to iterate (less effiiient)
# for key in vehicles:
#     print(key, vehicles[key], sep = ", ")

# Adding to a dict
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Lear Jet 75"
vehicles["toy"] = "Glider Paper-A4"

# Upgrade the virago (updating a value for a key)
vehicles["virago"] = "Yamaha XV535"

# Deleting a value
del vehicles["starfighter"]
# Issue with using del method is that it may crash program
# del vehicles["f1"]
# # KeyError: 'f1'

# pop operation allows you to search for the item and return "None" or  a string" if not found (rather than crash)
result = vehicles.pop("f1", "You wish, Sell the lear jet and you might be able to affort a racing car")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()


# interate using dot(items) as a tuple which is then unpacked (more efficient)
for key, value in vehicles.items():
    print(key, value, sep=", ")



