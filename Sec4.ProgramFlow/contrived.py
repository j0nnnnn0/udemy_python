# Python Programming Class - Udemy 12.10.2021

# else in loops 

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---
numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("the numbers are unacceptable.")
        break
else:
    print("all those numbers are fine")