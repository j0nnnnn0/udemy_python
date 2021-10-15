# Python Programming Class - Udemy 12.10.2021

# Lists - Deleting items in a list


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----
data = [4, 5, 104, 105, 110, 120, 120, 120, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_val = 100
max_val = 200

# # ISSUE: using for loop we have an issue as once index 0 is deleted and the list is re-iterated, the old Index 1 is now Index 0
# for index, value in enumerate(data):
#     if (value < min_val) or (value > max_val):
#         del data[index]
#         print(data)

#Process low value in list
stop = 0
for index, value in enumerate(data):
    if value >= min_val:
        stop = index
        break
print (stop)
del data[:stop]
print(data)

# 2
# [104, 105, 110, 120, 120, 120, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

#Process high value in list
stop = 0
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_val: 
        # We have the index of the last item to keep
        # Set "start" to the position of the first
        # item to delete, which is 1 after the index
        start = index + 1 
        break

print(start) # for debugging
del data[start:]
print(data)

# 14
# [104, 105, 110, 120, 120, 120, 150, 160, 170, 183, 185, 187, 188, 191]