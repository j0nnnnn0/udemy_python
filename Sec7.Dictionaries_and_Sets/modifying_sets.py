# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - Adding items to a set


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

numbers = set() # declare set function
print(numbers, type(numbers))

#numbers.add(1)
#print(numbers)

#while len(numbers) < 4:
#    next_value = int(input("Please enter your next value: "))
#    numbers.add(next_value)
#print(numbers) 


# Dictionaries and Sets - Using set to remove duplicate values

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# create a set from the list , to remove duplicates

#unique_data = set(data) # unsorted -> output is a set
# {'blue', 'red', 'green', 'white'} 

#unique_data = sorted(set(data)) # sorted -> output is a list
# ['blue', 'green', 'red', 'white']

# Create a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data)) # order is preserved and duplicates are removed -> output is a list

print (unique_data, " - output is type: ",type(unique_data))

print()
print(dict.fromkeys(data)," - output is type: ",type(data))
