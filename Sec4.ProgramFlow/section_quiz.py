# value = 8
# answer = 0
 
# for x in range(1, 13):
#     answer = value * x
#     print("{0} times {1} is {2}".format(x, value, answer))
    
    
# for value in range (11):
#     value = value * 2
#     print(value)
    
    
# for x in range(30):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)
    
quote = """
It's not pining. It's passed on. This parrot is no more. It has ceased to be.
It's expired and gone to meet its maker.
This is a late parrot.
It's a stiff. Bereft of life, it rests in peace.
If you hadn't nailed it to the perch, it would be pushing up the daisies.
It's rung down the curtain and joined the choir invisible.
THIS IS AN EX-PARROT.
"""
 
period_count = 0
for char in quote:
    if char == '.':
        period_count += 1
print(period_count)