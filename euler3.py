import math
from math import floor, sqrt

#### Problem 3

def is_prime(x):
    return prime_helper(x,floor(sqrt(x)))

def prime_helper(x,divisor):
    if divisor == 1:
        return True
    if (x % divisor) == 0:
        return False
    else:
        return prime_helper(x, divisor-1)

##def factor(x):
##    factor_helper(x,int(math.sqrt(x)))
##
##def factor_helper(x,divisor):
##    if divisor == 1:
##        print(1)
##    elif (x % divisor) == 0:
##        print(divisor)
##        factor_helper(x,x/divisor)
##    else:
##        factor_helper(x,divisor-1)

def divides(x, divisor):
    return (x % divisor == 0)
##
##def smallest_divisor(x):
##    return find_divisor(x,2)
##
##def find_divisor(x, test_divisor):
##    if (test_divisor * test_divisor) > x:
##        return x
##    if divides(x, test_divisor):
##        return test_divisor
##    else:
##        return find_divisor(x, test_divisor + 1)
##
##def largest_divisor_helper(x, test_divisor):
##    if (test_divisor * test_divisor) > x:
##        return x
##    if divides(x, test_divisor):
##        if is_prime(test_divisor):
##            return (test_divisor, x/test_divisor)
##        else:
##            return largest_divisor_helper(test_divisor, floor(sqrt(test_divisor)))
##    else:
##        return largest_divisor_helper(x, test_divisor-1)
##
##def largest_divisor(x):
##    return largest_divisor(x, floor(sqrt(x)))


def largest_prime(x, start_prime):
    for div in range(start_prime, floor(sqrt(x))):
        if divides(x,div) and is_prime(div):
            print((div, x / div))

#### Problem 4

def is_palindrome(x):
    xstr = str(x)
    return xstr == xstr[::-1]

##        return xstr[0:int((lenstr/2))] == xstr[int((lenstr/2)):lenstr][::-1]
##    else:
##        return xstr[0:int((lenstr-1)/2)] == xstr[int(((lenstr-1)/2)+1):lenstr][::-1]

def three_digit_palindromes():
    largest = 0
    for first in range(100,1000):
        for second in range(100,1000):
            if (first*second)>largest and is_palindrome(first * second):
                largest = first*second
                print(first,second,first*second)

#### Problem 5

def product_of_primes(n):
    product_of_primes = 1
    for k in range(1,n+1):
        if is_prime(k):
            product_of_primes = product_of_primes * k
    return product_of_primes

def smallest_divisible(n):
    increment = product_of_primes(n)
    i = increment
    while(True):
        divisible = True
        for j in range(1,n+1):
            if not divides(i,j):
                divisible = False
                break
        if divisible == True:
            print(i)
            return
        else:
            i = i + increment
            
def problem5():
    smallest_divisible(20)
