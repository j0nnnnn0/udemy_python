
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets -set difference


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
from primes_and_squares import squares_generator, primes_generator

evens = set(range(0,50,2))
odds = set(range(1,50,2))

print (odds)
print (evens)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

# odds that are primes

# using the method
print(odds.difference(primes))
# {1, 33, 35, 39, 9, 45, 15, 49, 21, 25, 27}

#using the operator
print(odds - primes)
# {1, 33, 35, 39, 9, 45, 15, 49, 21, 25, 27}