# Python Programming Class - Udemy 12.10.2021

# Nested Loops

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# -----
cls()
for i in range (1,13):
    for j in range (1,13):
        print ("{0} times {1} is {2}".format(j, i, i * j))
    print ("*" * 80)        
