
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets -set symmetric difference (opposite of intersection)


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

# Using sets
morning = {"Java", "C", "Ruby", "Lisp","C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

# symmetric difference as an Operator
possible_courses = morning ^ afternoon
print(possible_courses)
# {'Python', 'Lisp'}

# Using lists
morning = ["Java", "C", "Ruby", "Lisp","C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

#Symmetric Difference as a method
possible_courses = set(morning).symmetric_difference(afternoon)
print (possible_courses)