# Python Programming Class - Udemy 11.10.2021

#String Replacement Fields

age = 24
print("My age is " +str(age) + "years.") # using str function 

print("My age is {0} years.".format(age)) # using replacement fields

# declare replacement fields and substitute in print statement
print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {0}" 
      .format(31, "Jan", "Mar","May", "Jul", "Aug", "Oct", "Dec")) #there are 31 days in Jan, Mar, May, Jul, Aug, Oct and 31
print()
print(
    """Jan : {0}
    Feb : {1}
    Mar : {0}
    Apr : {2}
    May : {0}
    Jun : {2}
    Jul : {0}
    Aug : {0}
    Sep : {2}
    Oct : {0}
    Nov : {2}
    Dec : {0}
    """.format(31,28,30)
    )


a = 45
b = 15
c = 3
print(a - b / c)
