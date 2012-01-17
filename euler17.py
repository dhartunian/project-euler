import numpy as np
import scipy as sp

integers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80:'eighty', 90:'ninety'}

def print_number(n):
    if n<=20:
        return integers[n]
    elif n<100:
        tens = int(np.floor(n/10.0)*10)
        ones = int(n - tens)
        tens_txt = integers[tens]
        if ones > 0:
            ones_txt = integers[ones]
            return tens_txt + ' ' + ones_txt
        else:
            return tens_txt
    elif n<1000:
        hundreds = int(np.floor(n/100.0)*100)
        # tens = int(np.floor(int(n - hundreds)/10.0)*10)
        # ones = int(n - hundreds - tens)
        hundreds_txt = integers[hundreds/100] + ' hundred'
        if n - hundreds > 0:
            return hundreds_txt + ' and ' + print_number(n - hundreds)
        else:
            return hundreds_txt
        # if tens > 0:
        #     tens_txt = integers[tens]
        #     if ones > 0:
        #         ones_txt = integers[ones]
        #         return hundreds_txt + ' and ' + tens_txt + ' ' + ones_txt
        #     else:
        #         return hundreds_txt + ' and ' + tens_txt
        # else:
        #     if ones > 0:
        #         ones_txt = integers[ones]
        #         return hundreds_txt + ' and ' + ones_txt
        #     else:
        #         return hundreds_txt
    elif n == 1000:
        return 'one thousand'

def biggest(n):
    total = 0
    for number in range(1,1001):
        number_txt = print_number(number)
        print number_txt
        total = total + len(''.join(number_txt.split(' ')))
    print total
        
