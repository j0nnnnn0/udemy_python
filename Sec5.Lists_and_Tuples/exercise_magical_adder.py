# Python Programming Class - Udemy 17.10.2021

# Exercise - Magical Adder

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---
# Prompt user to enter 3 ints seperated by ","
# Calculate output using "a + b - c"

list = [] #initate list
list = input("Please enter 3 numbers seperated by a comma: ")
# print("Your input: {}".format(list))

#Split list on comma
split_list = list.split(",")
# print("Splitting the list:",format(split_list))

# Replace values from str to int
for index in range(len(split_list)):
    split_list[index] = int(split_list[index])
# print("Replace str with int: {}".format(split_list))

# Calculate output from a + b -c
calc = split_list[0] + split_list[1] -split_list[2]
# print("The answer is: {}".format(calc))
print(calc)

# Their solution

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)