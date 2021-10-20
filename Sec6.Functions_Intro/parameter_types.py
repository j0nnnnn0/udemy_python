# Python Programming Class - Udemy 20.10.2021

# Functions - Defining parameter types

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2)) 
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword (*kwargs):...{}".format(kwargs))
    
    
func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)

"""
positional-or-keyword:...1, 2
var-positional (*args):..(3, 4, 5, 9) # creates a tuple with values up to keyword
keyword:.................6
var-keyword (*kwargs):...{'key1': 7, 'key2': 8}
"""