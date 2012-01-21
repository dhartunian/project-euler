def sumstr(a, b):
    if len(a) > len(b):
        b = ('0' * (len(a) - len(b))) + b
    elif len(a) < len(b):
        a = ('0' * (len(b) - len(a))) + a
    sumstr = ''
    carry = 0
    for chars in reversed(zip(a,b)):
        sum = int(chars[0]) + int(chars[1]) + carry
        if sum >= 20:
            carry = 2
            sum = sum - 20
        elif sum >= 10:
            carry = 1
            sum = sum - 10
        else:
            carry = 0
        sumstr = str(sum) + sumstr
    if carry > 0:
        sumstr = str(carry) + sumstr
    return sumstr

data = open('euler_13_data')
rolling_sum = '0'
newline = data.readline()
while newline != '':
    rolling_sum = sumstr(newline[:-1], rolling_sum)
    print rolling_sum
    newline = data.readline()
print rolling_sum

