# Python Programming Class - Udemy 12.10.2021

# while in loops

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---

# for i in range(10):
#     print ("i is now {}".format(i))
# cls()

# while loop will finish when condition is false
i = 0
while i < 10:
    print ("i is now {}".format(i))
    i+=1 # i = i +1