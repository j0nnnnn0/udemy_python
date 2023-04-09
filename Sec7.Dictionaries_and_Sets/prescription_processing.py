
# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - Deleting items from a set : pop method


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
from prescription_data import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prespriction = patients[patient]
    print(prespriction)