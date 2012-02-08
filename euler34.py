import numpy as np
import math

collection_of_numbers = np.array([])

for i in range(0,2540160):
    if sum([math.factorial(int(s)) for s in str(i)]) == i:
        print i
        np.append(collection_of_numbers, i)
