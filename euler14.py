import numpy as np
import scipy as sp

def iterator(x):
    if x % 2 == 0:
        return x / 2
    else:
        return (3 * x) + 1

def doIteration(start, solution_dictionary):
    current_value = start
    current_len = 1
    while current_value != 1:
        if solution_dictionary.has_key(current_value):
            current_len = current_len + solution_dictionary[current_value]
            break
        current_value = iterator(current_value)
        current_len = current_len + 1
    solution_dictionary[start] = current_len
    return current_len

def problem14(n):
    max_len = 0
    max_len_seed = 0
    solution_dictionary = {}
    for i in range(1,n):
        current_len = doIteration(i, solution_dictionary)
        if current_len > max_len:
            max_len = current_len
            max_len_seed = i
        # print '---'
        # print i
        # print current_len
    print max_len
    print max_len_seed
    
if __name__ == '__main__':
    problem14(1000000)
