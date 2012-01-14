import numpy as np
import math

def num_divisors(n):
    count = 0
    for divisor in range(1,int(math.sqrt(n))):
        if n % divisor == 0:
            count = count + 2
    return count+1

if __name__ == '__main__':
    triangle_num = 1
    counter = 1
    num_d = 1
    while num_d <= 501:
        counter = counter + 1
        triangle_num = triangle_num + counter
        num_d = num_divisors(triangle_num)
        # print '--'
        # print counter
        # print triangle_num
        # print num_d
    print triangle_num
