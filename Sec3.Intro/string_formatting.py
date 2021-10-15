# Python Programming Class - Udemy 11.10.2021

#String Replacement Fields

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

print(os.name)

for i in range(1, 13):
    print("No. {0:2} square is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
print()

#left aligned
for i in range(1, 13):
    print("No. {0:2} square is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
print()

#centered aligned
for i in range(1, 13):
    print("No. {0:2} square is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()

#centered aligned
for i in range(1, 13):
    print("No. {0:2} square is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()

# precions and field width
print("Pi is approximately {0:12}".format(22 / 7)) # standard 15 decimals points
print("Pi is approximately {0:12f}".format(22 / 7)) # f declares float so we get 6 decimal points
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.54f}".format(22 / 7)) # adds padding of 000

# Pi is approximately 3.142857142857143
# Pi is approximately     3.142857
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately           3.14285714285714279370154144999105483293533325195312
# Pi is approximately                 3.142857142857142793701541449991054832935333251953125000


# f-strings
cls()
pi = 22/7
print(f"pi is apprx. {pi:12.50f}") #f strings available from python 3.6 onwards
#   Also called “formatted string literals,” f-strings are string literals that have an f at the beginning 
#   and curly braces containing expressions that will be replaced with their values
name = "j0nnnnn0"
age = 47
print(f"Hello, {name}. You are {age}.")

#String Interpolation in Python2
# %d is decimal
# %d is float
# %s is string
# %h for hexidecimal
# %o for octo
# %e for scientific notation

cls()
age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print ("PI is approx. %f" % (22/7))
print ("PI is approx. %60.50f" % (22/7)) # with precision and width