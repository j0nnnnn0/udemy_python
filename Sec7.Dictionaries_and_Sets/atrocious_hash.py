# Python Programming Class - Udemy 31.10.2021

# Dictionaries and Sets - Hash , a bad example

import os
from typing import ValuesView

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()


# ----------

data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# print(ord("a"))
# print(ord("b"))
# print(ord("a"))
# print(ord("4"))
# print(ord("_"))

def simple_hash(s: str) -> int:
    """[summary] A ridiculous simple hash function

    Args:
        s (str): [description] input a string

    Returns:
        int: [description] output an int betw 0 and 9
    """
    basic_hash = ord(s[0])
    return basic_hash % 10


for key, value in data:
    h = hash(key) # python buildd-in hash function
    print(key, h)
    # Python hashing function  
    # orange -3338097763250883852
    # apple 8737112910325991482  
    # lemon 7405836599848562996  
    # grape -4407472485428989117 
    # melon 1931814110581799179
    
for key, value in data:
    h = simple_hash(key) # our hash function
    print(key, h) 
    # our hash function
    # orange 1
    # apple 7 
    # lemon 8 
    # grape 3 
    # melon 9 