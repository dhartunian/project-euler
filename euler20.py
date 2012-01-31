import numpy as np

def factorial(n):
    if n == 1:
        return 1;
    else:
        return n * factorial(n-1)

print sum(int(char) for char in str(factorial(100)))
