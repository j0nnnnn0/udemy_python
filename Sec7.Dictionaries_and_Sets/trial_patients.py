
# Python Programming Class - Udemy 15.04.2022

# Dictionaries and Sets - set intersection in practive


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

# Create two distinct sets
trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

# using the intersection method
check_set = trial_1.intersection(trial_2)
print(check_set)
# {'Georgia', 'Charley'}

# using the operator &
print (trial_1 & trial_2)

# Multiple sets intersection

farm_animals = {"sheep", "hen","cow","horse","goat"}
wild_animals = {"lion","elephant","tiger","goat","panther","horse"}
potential_rides = {"donkey", "horse", "camel"}

# more than two sets are intersected (only horse remains)
# using the operator
intersection = farm_animals & wild_animals & potential_rides
print(intersection)
# {'horse'}

# using the method
mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)
# {'horse'}