available_parts = [
    ("computer", "HP",
        [
            ("name", "HP-001"),
            ("price", 800),
        ]
    ),
    ("monitor", "Dell",
        [
            ("name", "Dell-002"),
            ("price", 300),
        ]
    ),
    ("keyboard", "Logitech",
        [
            ("name", "G815 (Tactical)"),
            ("price", 150),
        ]
    ),
    ("mouse", "Logitech",
        [
            ("name", "Pro Wireless X"),
            ("price", 99.99),
        ]
    ),
    ("hdmi cable", "ACME Distribution",
        [
            ("name", "Pro HDMI 2.0 braded"),
            ("price", 34.59),
        ]
    ),
    ("printer", "EPSON",
        [
            ("name", "Epson Office Pro A3"),
            ("price", 478),
        ]
    )
                ]

# Additional Tasks:
    # Add more items 
    # Change Available_parts list to store tuples
    # Each tuple to include name and price
    # Display price and total price
# ----

for type, brand, (model, price) in available_parts:
    print("type: {}, brand: {}, model: {}, price: {}"
          .format(type, brand, model[1], price[1]))
print()

valid_choices = []
# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
print("valid choices are : ",valid_choices)

current_choice = "-" # initialise the variable
computer_parts = [] # create an empty list
bill = [] # Initiate an emply Bill list
PART_DETAIL_INDEX = 1
BILL_DETAIL_INDEX = 1
DETAILS_INDEX = 2
PRICE_INDEX = 1
tax = 0.075

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) -1 # substract 1 from each current_choice to match indexing of available_parts
        chosen_part = available_parts[index] # chosen_part is the index of available_parts
        cost = available_parts[index][DETAILS_INDEX][PRICE_INDEX][PRICE_INDEX]
        if chosen_part in computer_parts:
            #Already in so Remove
            print("Removing {}.".format(current_choice))
            computer_parts.remove(chosen_part)
            print("Your list now contains: {}".format(computer_parts))
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part) # add the chosen_part (itself the index of available parts) to the computer_parts list
            print("You list now contains: {}".format(computer_parts))
            bill.append(cost) # adds cost to the bill
    else:
        print("Please select options from the list below, Press 0 to end: ")
        for number, (type, brand, (name, price)) in enumerate(available_parts):
            print("{}. Type: {}, Brand: {}, Name: {}, Price: CHF{}"
                    .format(number + 1, type, brand, name[PART_DETAIL_INDEX], price[PART_DETAIL_INDEX]))
   
    current_choice = input("Make your selection: ")

print("You have selected {} items: ".format(len(computer_parts)))

# for i in range(index(computer_parts) + 1):
#     for index, (type, brand, (name, price)) in enumerate(computer_parts):
#         print("{}. Type: {}, Brand: {}, Name: {}, Price: CHF{}"
#               .format(index, type, brand, name , price))

for number, (type, brand, (name, price)) in enumerate(computer_parts):
    print ("{}: A {} by {} named {} costing CHF {}".format(number +1, type, brand, name[PART_DETAIL_INDEX], price[PART_DETAIL_INDEX]))

res = sum(list(bill))
print("Itemised bill is CHF {}".format(res))
print("Your TOTAL bill (incl. tax) is CHF {}".format(res + res * tax))
print("Your TOTAL bill (incl. tax) is CHF {}".format(round(res + res * tax), 2))

