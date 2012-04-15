"""
Exercise 0: Raising a number to a given power using recursion.
"""

def exponent(n, exp):
    if(exp == 0):
        return 1
    else:
        return n * exponent(n, exp - 1)

print exponent(2,38)