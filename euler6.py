import math

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
            
def nth_prime
