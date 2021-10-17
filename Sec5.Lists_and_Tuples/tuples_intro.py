# Python Programming Class - Udemy 17.10.2021

# Tuples - Intro
# Tuples are "Immutable"

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---
# t = ("a", "b", "c")
# print(t)
# output is in parentheses (tuble) rather than brackets (list)

# ---
# name = "Jonathan"
# age = 10

# print((name, age, "Python", 2020)) 
# # adding parentheses means we prints a tuble
# # ('Jonathan', 10, 'Python', 2020)

# ---
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
mettalica = "Ride the Lightning", "Metallica", 1984

print(mettalica)
# ('Ride the lightning', 'Metallica', 1984) prints a tuble

print(mettalica[0])
print(mettalica[1])
print(mettalica[2])
# still use brackets to access the index of a tuple

# Tuples are immutable so cannot change them
# mettalica[0] = "Master of Puppets"

#   File "c:\Users\Jonat\Documents\code\udemy_python\Sec5.Lists_and_Tuples\tuples_intro.py", line 40, in <module>
#     mettalica[0] = "Master of Puppets"
# TypeError: 'tuple' object does not support item assignment

# if we want to change a tuple, we have to transform it to a list
mettalica2 = list(mettalica) # list function transforms it to a list
print(mettalica2)
mettalica2[0] = "Master of Puppets"
print(mettalica2)