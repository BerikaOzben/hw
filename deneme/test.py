first_variable = 30

import collections
first_variable = collections.Counter([1,1,2,2,3,4,4,4])
print(type(first_variable))
print(first_variable)

# constants
MY_CONSTANT = 15  # screaming snake

# Functions
def add_two_number(x1, x2): 
    total = x1 + x2
    print(total)

add_two_number(3, 5)

add_two_number

# redundant code istenmez bu nedenle DRY

# stringler uniquedir

text = "bıktık ya"
text.upper()

import math
math.pow(2,4)

import this  # The Zen of Python, by Tim Peters

# Docstring

def my_pow(x1, x2):
    """
    Raise a number to a arbitrary power
    
    parameters
    x1: int base number
    x2: int power to raise
    return: int - number raised to power of second number
    """
    result = x1 ** x2    
    return result

print(my_pow.__doc__)  # dokumantasyona erişir

print(str.__doc__)

