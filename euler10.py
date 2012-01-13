import numpy as np
from scipy import random
import pdb

def is_prime(pn):
    for m in range(1,100):
        random_int = random.randint(1,pn)
        if not (pow(random_int, int(pn-1), int(pn)) == 1):
            return False
    return True
        
def find_sum_of_primes_below(n):
    sum_so_far = 0
    for m in np.arange(2,n):
        if is_prime(m):
            sum_so_far = sum_so_far + m
    return sum_so_far
