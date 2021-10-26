# Python Programming Class - Udemy 22.10.2021

# Dictionaries and Sets - Using Dict in a menu


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----

# Import contents (pantry and recipes from contents.py)
from contents import pantry, recipes

def add_shopping_item(data:dict, item: str, amount = int) -> None:
    """Add a tuple containing `items` and `amount`to data dict.
    Args:
        data (dict): [description]
        item (str): [description]
        amount ([type], optional): [description]. Defaults to int.
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount
    # setdefault returns the key of the dict if it exists, else create a new entry and sets default value

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# Create a new dictionary to display the available recipes.
display_dict ={} 
# enumerate dict recipes into tubles
for index, key in enumerate(recipes):
        # print(f" recipes enumeration: {index}, {key}")
    # setting the index of display_dict
    # as a string (was int) and equal to key of recipe dict
    display_dict[str(index +1)] = key
    # print(f" display_dict: {display_dict}")
        #  recipes enumeration: 0, Butter chicken
        #  display_dict: {'1': 'Butter chicken'}
        #  recipes enumeration: 1, Chicken and chips
        #  display_dict: {'1': 'Butter chicken', '2': 'Chicken and chips'}
        #  recipes enumeration: 2, Pizza
        #  display_dict: {'1': 'Butter chicken', '2': 'Chicken and chips', '3': 'Pizza'}
        #  recipes enumeration: 3, Egg sandwich
        #  display_dict: {'1': 'Butter chicken', '2': 'Chicken and chips', '3': 'Pizza', '4': 'Egg sandwich'}
        #  recipes enumeration: 4, Beans on toast
        #  display_dict: {'1': 'Butter chicken', '2': 'Chicken and chips', '3': 'Pizza', '4': 'Egg sandwich', '5': 'Beans on toast'}
        #  recipes enumeration: 5, Spam a la tin
        #  display_dict: {'1': 'Butter chicken', '2': 'Chicken and chips', '3': 'Pizza', '4': 'Egg sandwich', '5': 'Beans on toast', '6': 'Spam a la tin'}

# Create a new dictionary as a shopping_list
shopping_list = {}

while True:
    #Display menu of recipes we know how to cook
    print("Please choose your recipe:")
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    print ("0 - Quit")
        # 1 - Butter chicken
        # 2 - Chicken and chips
        # 3 - Pizza
        # 4 - Egg sandwich
        # 5 - Beans on toast
        # 6 - Spam a la tin
        # 0 - Quit
        
    choice = input (": ")
    
    if choice == "0":
        print("Bye")
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients: ")
        ingredients = recipes[selected_item] # equivalent to recipes[key] where key is the recipe name (ie Egg sandwich)
        print(ingredients)
        print("checking ingredients against pantry...")
        # enumerate the food items and required quantity in ingredients
        for food_item, required_quantity in ingredients.items():
            quantity_in_panty = pantry.get(food_item, 0) # default to 0 if not found
            # match the ingredient to the keys in pantry
            if required_quantity <= quantity_in_panty:
                print(f"{food_item} is in pantry")
            else:
                quantity_to_buy = required_quantity - quantity_in_panty
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                # Adding to shopping list
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
    print("--------------------------")        
    
for things in shopping_list.items():
    print(things)
