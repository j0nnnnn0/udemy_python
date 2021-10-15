# Python Programming Class - Udemy 12.10.2021

# Lists - sorting

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

unique_letters = sorted(set(pangram)) # set means unique
print(unique_letters)


numbers = [2.3, 2.4, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(id(sorted_numbers))
print(id(numbers))

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham", "John", "terry", "eric", "Terry","michael"]
names.sort(key=str.casefold) #sort ignoring case
print(names)

