import numpy as np
# import scipy as sp

# mygrid = np.zeros((5,5))

# def visit(row, col):
#     if row == 0 and col == 0:
#         mygrid[row,col] = mygrid[row,col] + 1
#     if row > 0:
#         visit(row - 1, col)
#     if col > 0:
#         visit(row, col - 1)

# def visit2(row, col):
#     global mycounter
#     if row == 0 and col == 0:
#         mycounter = mycounter + 1
#     if row > 0:
#         visit2(row - 1, col)
#     if col > 0:
#         visit2(row, col - 1)

def init(agrid):
    s = agrid.shape
    agrid[s[0] - 1] = 1
    agrid[:,s[0] - 1] = 1

def colsums(agrid, level):
    for row in range(level-1,-1,-1):
        agrid[row, level] = agrid[row + 1, level] + agrid[row, level + 1]

def rowsums(agrid, level):
    for col in range(level-1,-1,-1):
        agrid[level, col] = agrid[level, col + 1] + agrid[level + 1, col]

def cornersum(agrid, level):
    agrid[level, level] = agrid[level + 1, level] + agrid[level, level + 1]

size = 21
mygrid = np.zeros((size,size))
init(mygrid)
for level in range(size-2,-1,-1):
    cornersum(mygrid, level)
    if level > 0:
        rowsums(mygrid, level)
        colsums(mygrid, level)

print mygrid[0,0]
