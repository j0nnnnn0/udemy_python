# Python Programming Class - Udemy 19.10.2021

# Functions - Exercise Sum even or odd numbers in a range


import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# Write a function called sum_eo with parameters:
    # n : a postive number
    # t : a str
    # If t has the value 'e', the function should return the sum of all even numbers less than n
    # Else if t has the value 'o', the function should return the sum of all odd numbers less than n
    # for any other values of t return -1


def sum_eo(t, n):
    while True:
        t_temp = input(t)
        if t_temp in ("o","e"):
            return t_temp
        n_temp = input(n)
        if (n_temp.isnumeric() and n_temp > 0):
            return int(n_temp)
        print("{} is not a valid number.".format(n_temp))


t = input("please enter o for odd or e for even: ")
n = input("Please enter a positive number: ")
if sum_eo(n, t):
    print(n, t)



