# Python Programming Class - Udemy 20.10.2021

# Functions - Exercise - Factorial Function

"""
Write a function called factorial that returns 
the factorial number passed by its argument
Use a for loop to call the function to print out the first x factorial
where x is a user entered positive integer (0 incl. to say 36)
"""

def factorial(n:int) -> int:
    """Return the factorial of `n` (or n!)\n
    0! is equal to 1

    Args:
        n (int): user generated positive value

    Returns:
        int: the factorial of `n`
    """
    if n <= 1:
        return 1

    result = 2
    for x in range(3, n+1):
        result *= x
    
    return result


for i in range (36):
    answer = factorial(i)
    print(i, answer)
