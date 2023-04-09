
# Python Programming Class - Udemy 11.03.2022

# Dictionaries and Sets - union exercise


from cgitb import small
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}


things_that_bite = snakes | vespas
print ("I bite: ", sorted(things_that_bite))

things_that_sting = scorpions | spiders
print ("I sting: ", sorted(things_that_sting))

arachnids = scorpions | spiders
print("I am an arachnid: ", sorted(arachnids))



