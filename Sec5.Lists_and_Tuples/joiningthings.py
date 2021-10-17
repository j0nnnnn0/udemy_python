# Python Programming Class - Udemy 17.10.2021

# join method

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

flowers = [
    "Daffodil",
    "Evening Primose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

for flower in flowers:
    print(flower)
print()

# join is a sting method
# seperator is a string
# join iterates over the list so no need for a loop
seperator = " | "
output = seperator.join(flowers)
print(output)