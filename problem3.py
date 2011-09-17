import math

def is_prime(x):
    return prime_helper(x,int(math.sqrt(x)))

def prime_helper(x,divisor):
    if divisor == 1:
        return True
    if (x % divisor) == 0:
        return False
    else:
        return prime_helper(x, divisor-1)


def factor(x):
    factor_helper(x,int(math.sqrt(x)))

def factor_helper(x,divisor):
    if divisor == 1:
        print 1
    elif (x % divisor) == 0:
        print divisor
        factor_helper(x,x/divisor)
    else:
        factor_helper(x,divisor-1)

def divides(x, divisor):
    return (x % divisor == 0)

def smallest_divisor(x):
    return find_divisor(x,2)

def find_divisor(x, test_divisor):
    if (test_divisor * test_divisor) > x:
        return x
    if divides(x, test_divisor):
        return test_divisor
    else:
        return find_divisor(x, test_divisor + 1)

def largest_divisor(x, test_divisor):
    if (test_divisor * test_divisor) > x:
        return x
    if divides(x, test_divisor):
        if is_prime(test_divisor):
            return (test_divisor, x/test_divisor)
        else:
            return largest_divisor(test_divisor, round(math.sqrt(test_divisor))-1)
    else:
        return largest_divisor(x, test_divisor-1)

def largest_divisor_blah(x):
    return largest_divisor(x, round(math.sqrt(x))-1)

