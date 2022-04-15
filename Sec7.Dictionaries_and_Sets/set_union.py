
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets -set union


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
# union in sets
# https://docs.python.org/3/library/stdtypes.html#frozenset.union

# farm_animals = {"sheep", "hen","cow","horse","goat"}
# wild_animals = {"lion","elephant","tiger","goat","panther","horse"}

# # union as a method
# all_animals_1 = farm_animals.union(wild_animals)
# print (all_animals_1)
# # {'horse', 'hen', 'cow', 'goat', 'sheep', 'tiger', 'panther', 'elephant', 'lion'}

# all_animals_2 = wild_animals.union(farm_animals)
# print (all_animals_2)
# # {'horse', 'hen', 'cow', 'goat', 'sheep', 'tiger', 'panther', 'elephant', 'lion'}

# # union as an operator (pipe)
# all_animals_3 = farm_animals | wild_animals
# print(all_animals_3)

from prescription_data import adverse_interactions

# create an empty set
meds_to_watch = set()

# for interaction in adverse_interactions:
# #    meds_to_watch = meds_to_watch.union(interaction) #union as a method
# #    meds_to_watch = meds_to_watch | interaction #union as an operator
# #    meds_to_watch.update(interaction) # union as update method (doesn't create a new set)
#     meds_to_watch |= interaction # union as update operator (doesn't crearte a new set)

# updating the target set by unpacking the source set (can only be done using the method)
meds_to_watch.update(*adverse_interactions)

print (sorted(meds_to_watch))
# [('amlodipine', 'Blood pressure'), ('buspirone', 'Anxiety disorders'), ('citalopram', 'Antidepressant'), ('edoxaban', 'anti-coagulant'), ('erythromycin', 'Antibiotic'), ('metformin', 'Type 2 diabetes'), ('simvastatin', 'High cholesterol'), ('warfarin', 'anti-coagulant')]

#print each output on a new line by unpacking the list using sep function
print(*sorted(meds_to_watch), sep='\n')
# ('amlodipine', 'Blood pressure')
# ('buspirone', 'Anxiety disorders')
# ('citalopram', 'Antidepressant')
# ('edoxaban', 'anti-coagulant')
# ('erythromycin', 'Antibiotic')
# ('metformin', 'Type 2 diabetes')
# ('simvastatin', 'High cholesterol')
# ('warfarin', 'anti-coagulant')