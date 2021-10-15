# Python Programming Class - Udemy 12.10.2021

# Lists - sequence Operations

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# -- I like to clear my terminal

empty_list = [] # creates an empty list
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = list("89786430")
print(digits)

# more_numbers = list(numbers) # creates a new list using list function
# more_numbers = numbers[:] # creates a new list using slice
more_numbers = numbers.copy() # creates a new list using copy method
print(more_numbers)

print(numbers is more_numbers) # checks if numbers is the same list as more_numbers(ie same id)
print(numbers == more_numbers) # checks if the values of each list is equal

# https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-why-is-this-and-how-can-i-prevent-it/43220129#43220129
# tell us impact of features to 

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))

# print()
# print(len(even))
# print(len(odd))

# print()
# word = "mississipi"
# ask = "s"
# print("there are {} '{}' in {}.".format(word.count(ask), ask, word))

# even.extend(odd)
# print(even)
# even.sort()
# print(even)
# even.sort(reverse=True)
# print(even)