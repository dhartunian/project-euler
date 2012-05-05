import numpy as np
import math

remainder = 999999

# Use the multipliers to remove the given indexed number from the
# [0,1,2,3,4,5,6,7,8,9] sequence and you'll get the number. (since 0
# is the first one, we ask for the 999,999th)

for i in reversed(np.arange(1,10)):
    fact = math.factorial(i)
    multiplier = math.floor(remainder / fact)
    print 'Mult: ' + str(multiplier) + ' Remainder: ' + str(remainder)
    remainder = remainder - fact * multiplier
