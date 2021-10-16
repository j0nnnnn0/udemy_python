# Python Programming Class - Udemy 16.10.2021

# Lists - removing items from a list backwards

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---

data = [104, 101, 4, 105, 308, 103, 5, 
        107, 100, 306, 106, 102, 108]

min_val = 100
max_val = 200

print("Start")
print("Remove items if outside of expected range {} to {}"
      "\nFrom list {}".format(min_val, max_val, data))


# for loop starting at end of list
# for index in range(len(data) -1, -1, -1): # start from end and work backwards
#     if data[index] < min_val or data[index] > max_val:
#         print("Removing Index {} from {}.".format(index, data))
#         del data[index]
#         print("Updated list is now {}".format(data))

#Reversed function
top_index = len(data) -1 # 13-1 = 12 

for index, value in enumerate(reversed(data)):
    print("len of data: {}, top_index: {}, index: {}, reversed_index: {}, value: {}"
          .format(len(data),top_index, index, top_index - index, value)) # 11-12 = -1

    if value < min_val or value > max_val:
        print("Removing Index {} with value {} from {}.".format(index, value, data))
        del data[top_index -index]
        print("Updated list is now {}".format(data))
        print()

    else:
        print("Leaving untouched Index {} with value {} from {}.".format(index, value, data))

print(data)
print("End")