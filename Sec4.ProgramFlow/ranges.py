# Python Programming Class - Udemy 12.10.2021

# Iterating over a range

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#-----

for i in range (10,21):
    print("i is now {}".format(i))
    
# Challenge    
for i in range (0,10):
    print(i)
    
# ----

cls()
for i in range (10): # default is to start at zero
    print("i is now {}".format(i))
    
cls()
for i in range (10, 2): # from ten up to 2 with steps of 1
    print("i is now {}".format(i))
# nothing

cls()
for i in range (0, 10, 2): # from zero up to ten with steps of 2
    print("i is now {}".format(i))
# i is now 0
# i is now 2
# i is now 4
# i is now 6
# i is now 8

cls()
for i in range (10, 0, -2): # from ten up to zero with steps of -2
    print("i is now {}".format(i))

cls()
age = int(input("how old are you?"))
# if 16 <= age <=65: # curing conditions 
if age in range (16, 66): # Alternative using range
    print("Have a good day at work")
else:
    print("Happy chilling out")
print ("-" * 80)
if age < 16 or age > 65: # as an Alternative
    print("Happy chilling out")
else:
    print("Have a good day at work")
    
# Exercise

# Write a program to print out all numbers from 0 to 100 that are divisible by 7
# Zero is divisable so should be included
cls()
for i in range (0,101,7): # uses step values
    print(i)
    
for i in range(101)[::7]: # uses a slice
    print(i)    
