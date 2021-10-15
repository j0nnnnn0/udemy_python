# Python Programming Class - Udemy 12.10.2021

# while in loops - adventure

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---
available_exits = ["north", "south", "east", "west"]

# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction from {}: ".format(available_exits))
# print("aren't you glad to get out of there...")

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction from {}: ".format(available_exits))
    if chosen_exit.casefold() == "quit":
        print("game over")
        break

else:
    print("aren't you glad to get out of there...")


#Exercise

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
# Original code:
# for i in range(0, 100, 7):
#     print (i)

# for i in range(0, 100, 7):
#     print (i)
#     if i > 0 and i % 11 == 0:
#         break

# cls()
# # print out all numbers from 0 to 20 that are NOT divisible by 3 or 5
# for i in range(0,21):
#     if (i % 3 == 0 or i % 5 == 0):
#         continue
#     print(i)
