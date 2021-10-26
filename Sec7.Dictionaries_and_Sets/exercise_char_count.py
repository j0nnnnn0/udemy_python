# Python Programming Class - Udemy 26.10.2021

# Dictionaries and Sets - Exercise Character count

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
# Count the number of times each char occurs in a given text (ignoring case)

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# iterate over char 
for char in text.casefold():
    if char.isalnum():
        word_count[char] = word_count.setdefault(char,0) +1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)