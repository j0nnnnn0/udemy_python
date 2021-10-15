# Python Programming Class - Udemy 12.10.2021

# Lists - mutable

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---

shopping_list = ["milk", 
                 "pasta", 
                 "eggs", 
                 "spam", 
                 "bread", 
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
#print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(another_list))
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
# 1279757695616
# 1279757695616

a = b = c = d = e = f = another_list
print(a)

print ("Adding cream")
b.append("cream")
print(c)
print (d)
print(shopping_list)

