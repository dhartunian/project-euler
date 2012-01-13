import math
import numpy as np

def sum_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i)
    return sum


def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum*sum

def is_prime(x):
    return prime_helper(x,int(math.sqrt(x)))

def prime_helper(x,divisor):
    if divisor == 1:
        return True
    if (x % divisor) == 0:
        return False
    else:
        return prime_helper(x, divisor-1)

def prime_helper2(x, divisor):
    for divisor in range(divisor,int(math.sqrt(x))):
        if (x % divisor) == 0:
            return False
    return True

def is_prime2(x):
    return prime_helper2(x,2)

def nth_prime(n):
    i = 0
    counter = 1
    latest_prime = 0
    while (i < n):
        if is_prime(counter):
            i = i + 1
            latest_prime = counter
        counter = counter + 1
    return latest_prime

def read_file_into_string(filename):
    f = open(filename, 'r')
    x = f.readline()
    return x

def find_largest_sequence(mystr):
    largest_sum = 0
    for i in range(0,len(mystr)-5):
        mysum = int(mystr[i]) * int(mystr[i+1]) * int(mystr[i+2]) * int(mystr[i+3]) * int(mystr[i+4])
        if mysum > largest_sum:
            largest_sum = mysum
    return largest_sum
    

def find_pythagorean_triplet(n):
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            c = n-a-b
            if math.sqrt(a*a + b*b) == c:
                return a,b,c

def test_prime_list(prime_list, number):
    #division = number % prime_list
    division = np.remainder(number, prime_list)
    return np.any(division == 0)

def find_sum_of_primes_helper(prime_list,sum_so_far,m,n):
    if m >= n:
        return sum_so_far
    elif test_prime_list(m, prime_list):
        return find_sum_of_primes_helper(prime_list, sum_so_far,m+1,n)
    else:
        return find_sum_of_primes_helper(np.append(prime_list, m),
                                  sum_so_far + m,
                                  m+1,
                                  n)

def find_sum_of_primes_below(n):
    prime_list = np.array([])
    sum_so_far = 0
#    for m in range(2,n+1):
    for m in np.arange(1,n,2):
        if is_prime2(m):
#        if not test_prime_list(prime_list, m):
            sum_so_far = sum_so_far + m
#            prime_list = np.append(prime_list, m)
    return sum_so_far
