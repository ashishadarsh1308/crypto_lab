# write a function nth_root to accept 2 arguments: number and n.
# The function should return the nth root of the number 
# upto 2 decimal places only

import math

def nth_root(number, n):
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot compute an even root of a negative number.")
    
    if number == 0:
        return 0
    
    root = number ** (1 / n)
    return round(root, 2)

print(nth_root(27, 4))
print(nth_root(16, 4))