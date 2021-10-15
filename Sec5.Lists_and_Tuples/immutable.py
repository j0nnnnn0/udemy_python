# Python Programming Class - Udemy 12.10.2021

# Lists - immutable

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ---
# https://docs.python.org/3/library/functions.html#id 


result = True
another_result = result
print(id(result))
print(id(another_result))

# The IDs are bound to True
# 140731353655400
# 140731353655400

result = False
print(id(result))

# The ID changes now as result is bound to False
# 140731353655400
# 140731353655400
# 140731353655432

print()
result = "Correct"
another_result = result
print(id(result))
print(id(another_result))
print()
result +="ish"
print(id(result))

# correctish has a new ID
# 2335685392112  
# 2335685392112  

# 2335685400560  