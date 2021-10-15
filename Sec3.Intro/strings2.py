# Python Programming Class - Udemy 11.10.2021

parrot = 'Norwegian Blue'
# Positive Indexing
#         012345678901234
# Negative Indexing
#  -      43210987654321

# Slicing with steps

print(parrot[0:6:2]) #Nre with steps of 2
print(parrot[0:6:3]) #Nw with steps of 2

number = "9,223;372 036|854,775-807"
# Start at Index1, # to the end, # in Steps of 4
print(number[1::4]) # ,223,372,036,854,775,807 > ,,,,,,
# Make use of these Slices by Step
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val)for val in values])


# # Slicing - last char is not included in the Slice -- "up to but not including"

# print(parrot[0:6]) # Norweg
# print(parrot[-14:-8]) #Norweg using neg strings
# print()
# print(parrot[3:5]) # we
# print(parrot[0:9]) # Norwegian
# print(parrot[:9]) # Norwegian -- defaults to start of sequence
# print(parrot[10:]) #Blue
# print()
# print(parrot[:6] + parrot[6:]) #Norwegian Blue
# print(parrot[:]) 

# letters = 'abcdefghijklmnopqrstvwxyz'
# print()
# print(letters[2:4]) 

# print(parrot)

# # Positive Indexing
# print()
# print (parrot[3])
# print (parrot[4])
# print (parrot[9])
# print (parrot[3])
# print (parrot[6])
# print (parrot[8])


# # Negative Indexing
# print()
# print (parrot[-11])
# print (parrot[-1])
# print (parrot[-5])
# print (parrot[-11])
# print (parrot[-8])
# print (parrot[-6])

# #or
# print()
# print (parrot[3-14])
# print (parrot[4-14])
# print (parrot[9-14])
# print (parrot[3-14])
# print (parrot[6-14])
# print (parrot[8-14])

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5]) # True starts at 1 , to the end and step 5
print(data[1:5]) # False starts at :
print(data[0:-1:5]) # True starts at 1, to the end and step 5
print(data[:-1:5]) # False starts at 1, to the end and step 5


flower = "blue violet"
