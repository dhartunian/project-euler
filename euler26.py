import numpy as np
import pdb


denom_length = {}

for denom in np.arange(3,1001):
#    pdb.set_trace()
    remainder = 1
    remainder_list = {}
    cycle_length = 0
    while remainder > 0 and not (remainder in remainder_list.keys()):
        remainder_list[remainder] = cycle_length;
        remainder = np.remainder(remainder * 10, denom)
        cycle_length = cycle_length + 1;
    if remainder > 0:
        denom_length[denom] = len(remainder_list) - remainder_list[remainder]

for key,value in denom_length.iteritems():
    if value == max(denom_length.values()):
        print 'denominator: ', key
        print 'length of recurring cycle: ', value

