"""
- Write a function to calculate the sum of all numbers passed by its arguments
- Function is called sum_numbers
- Define a single variable argument (star arguments)
- Function must have a Docstring

test
1, 2, 3 -> 60
8, 20, 2 -> 30 
12.5, 3.147, 98.1 -> 113.747

var-positional (*args):..(3, 4, 5, 9) # creates a tuple with values up to keyword
    """
    
def sum_numbers(*args: float) -> float:
    """Return the sum of all numbers from argument

    Returns:
        float: sum as a `float`
    """
    print(args)
    sum = 0
    for index, (args) in enumerate(args):
        sum += args
    return sum

print(sum_numbers(10, 20.5, 60.6660, 1, 0, 88.77))
