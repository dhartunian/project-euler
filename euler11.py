import numpy as np
from pandas import read_csv

data = read_csv('euler_11_data', header = None)
dm = data.as_matrix()

def prod_up(data, row, column):
    if row > 3 and column < 20:
        return data[(row-4):row,column].prod()
    else:
        return 1
def prod_left(data, row, column):
    if column > 3 and row < 20:
        return data[row,(column-4):column].prod()
    else:
        return 1
def prod_right(data, row, column):
    if column < 17 and row < 20:
        return data[row,column:(column+4)].prod()
    else:
        return 1
def prod_down(data, row, column):
    if row < 17 and column < 20:
        return data[row:(row+4),column].prod()
    else:
        return 1
def prod_diag_right_up(data, row, column):
    if column < 16 and row > 3:
        return (data[(row-1),(column)] *
                data[(row-2),(column+1)] *
                data[(row-3),(column+2)] *
                data[(row-4),(column+3)])
    else:
        return 1
def prod_diag_left_up(data, row, column):
    if row > 3 and column > 3:
        return (data[(row-1),(column-1)] *
                data[(row-2),(column-2)] *
                data[(row-3),(column-3)] *
                data[(row-4),(column-4)])
    else:
        return 1

max_prod = 1
for row in range(0,21):
    for column in range(0,21):
        print (row, column)
        up = prod_up(dm, row, column)
        down = prod_down(dm, row, column)
        left = prod_left(dm, row, column)
        right = prod_right(dm, row, column)
        diag_right = prod_diag_right_up(dm, row, column)
        diag_left = prod_diag_left_up(dm, row, column)
        max_prod = max(max_prod,
                       up,
                       down,
                       left,
                       right,
                       diag_right,
                       diag_left)

print max_prod
