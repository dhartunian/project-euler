import numpy as np

def proper_divisors(n):
    divisor_list = np.array([])
    for divisor in range(1,int(n)):
        if n % divisor == 0:
            divisor_list = np.append(divisor_list, 
                                     divisor)
    return divisor_list

def sum_proper_divisors(n):
    return sum(proper_divisors(n))

def has_pair(n):
    sp = sum_proper_divisors(n)
    sp2 = sum_proper_divisors(sp)
    if int(n) == int(sp2):
        return (sp,sp2)
    else:
        return False

def get_pairs_below(n):
    for num in range(1,n):
        pair = has_pair(num)
        if pair != False:
            print pair

