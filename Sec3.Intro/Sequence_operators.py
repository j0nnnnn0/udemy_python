# Python Programming Class - Udemy 11.10.2021

#Sequence_operators
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
# same output but not really used
print("he's " "probably " "pining " "for the " "fjords")
print("Hello " *5) # repeat the sequence
print("Hello " *(5+4)) # Hello Hello Hello Hello Hello Hello Hello Hello Hello
print("Hello " *5 +"4") # Hello Hello Hello Hello Hello 4


today = "friday"
print ("day" in today)      #true
print ("fri" in today)      #true
print ("thrus" in today)    #false
print("parrot" in "fjord")  #false