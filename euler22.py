import numpy as np
from pandas import read_csv

alpha_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
                'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                'M': 13, 'N': 14, 'O':15, 'P': 16, 'Q': 17, 'R':18, 
                'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
                'Y': 25, 'Z': 26}

def nameValue(name):
    value = 0
    for char in name:
        value = value + alpha_values[char]
    return value

myfile = open('euler_22_data')
namelist = myfile.readline()
names = namelist.split(',')
for i in range(0,len(names)):
    names[i] = names[i][1:-1]
names.sort()
sum_scores = 0
for i in range(0,len(names)):
    sum_scores = sum_scores + ((i+1) * nameValue(names[i]))
