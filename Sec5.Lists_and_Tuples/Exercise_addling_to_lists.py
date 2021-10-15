data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# populate two lists with the appropriate plants from data

for plant in data:
    if "Flower" in plant:
        smallf = plant.replace(" - Flower","")
        flowers.append(smallf)
        print("Adding {} to list {}".format(plant, flowers))
    elif "Shrub" in plant:
        smalls = plant.replace(" - Shrub", "")
        shrubs.append(smalls)
print()
print(flowers)
print(shrubs)