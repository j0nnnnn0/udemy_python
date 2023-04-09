
# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - Deleting items from a set : Remove method


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

from prescription_data import *

#trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]
trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    presciption = patients[patient]
    if warfarin in presciption:
        presciption.remove(warfarin)
#    presciption.discard(warfarin)
        presciption.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial.")
    print(patient, presciption)

# Denise {('lusinopril', 'High blood pressure'), ('metformin', 'Type 2 diabetes'), ('edoxaban', 'anti-coagulant'), ('amlodipine', 'Blood pressure')}
# Eddie {('amlodipine', 'Blood pressure'), ('propranol', 'Beta blocker'), ('edoxaban', 'anti-coagulant'), ('simvastatin', 'High cholesterol')}   
# Frank {('citalopram', 'Antidepressant'), ('propranol', 'Beta blocker'), ('edoxaban', 'anti-coagulant'), ('buspirone', 'Anxiety disorders')}    
# Georgia {('carbimazole', 'Antithyroid agent'), ('edoxaban', 'anti-coagulant')}
# Patient Kenny is not taking Warfarin. Please remove Kenny from the trial.
# Kenny {('metformin', 'Type 2 diabetes'), ('amlodipine', 'Blood pressure'), ('citalopram', 'Antidepressant')}