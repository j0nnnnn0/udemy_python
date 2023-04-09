
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets -set intersection


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

print(odds.intersection(squares))
print(evens & squares)

#pass an iterable to the method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)