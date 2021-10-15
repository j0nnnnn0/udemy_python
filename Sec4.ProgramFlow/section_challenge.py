# Python Programming Class - Udemy 12.10.2021

# Section Challenge 

from io import BufferedIOBase
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# -----

# Print a number of options and allow user to select an option from the list
# Options should be numbered from 1 to 9
# Continue looping, allowing the user to choose of option each time round
# Loop terminates only when user chooses 0 (exit)
# if valid choice, print message with value typed
# Menu is printed again if choice is invalid

# Please choose your option from the list below:
#     1. Learn Python
#     2. Learn Java
#     3. Go swimming
#     4. Have dinner
#     5. Go to bed 
#     0. exit

cls()

choice = None

while True:
    print("Please choose your option from the list below: ")
    print ("1.\tLearn Python")
    print ("2.\tLearn Java")
    print ("3.\tGo swimming")
    print ("4.\tHave dinner")
    print ("5.\tGo to bed")
    print ("0.\texit")
    choice = input("Your Option : ")
    
    if choice == '0':
        break

    elif choice in "12345":
        print("your choice {}".format(choice))



# # Solution but not great lookin
# print("Please choose your option from the list below: ")
# print ("1.\tLearn Python")
# print ("2.\tLearn Java")
# print ("3.\tGo swimming")
# print ("4.\tHave dinner")
# print ("5.\tGo to bed")
# print ("0.\texit")
    
# while True:
#     choice = input("Your Option : ")

#     if choice == '0':
#         break

#     elif choice in "12345":
#         print("your choice {}".format(choice))
#     else:
#         print("Please choose your option from the list below: ")
#         print ("1.\tLearn Python")
#         print ("2.\tLearn Java")
#         print ("3.\tGo swimming")
#         print ("4.\tHave dinner")
#         print ("5.\tGo to bed")
#         print ("0.\texit")
