# Python Programming Class - Udemy 11.10.2021

# Slice with negative steps

# Index              1         2
#          01234567890123456789012345
letters = 'abcdefghijklmnopqrstuvwxyz'

backwards = letters[25:0:-1] # zyxwvtsrqponmlkjihgfedcb
print(backwards)
backwards = letters[::-1] # zyxwvtsrqponmlkjihgfedcba
print(backwards)
print()

# Challenge
# slice to get qpo
print(letters[16:13:-1])
# slice to get edcba
print(letters[4::-1])
# slice to get last 8char in reverse order
print(letters[25:17:-1])
print(letters[:-9:-1])

print()
#Idoms
print(letters[-4:])
print(letters[-1:])
print(letters[:1])