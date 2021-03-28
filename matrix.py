"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math
import copy as cp

# print the matrix such that it looks like
# the template in the top comment
def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(f"{el} ", end="")
        print()


# turn the paramter matrix into an identity matrix
# you may assume matrix is square
def ident(matrix):
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if j == i:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0


# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2
def matrix_mult(m1, m2):

    copy = cp.deepcopy(m2)

    m1Row, m2Row = len(m1), len(copy)
    m1Col, m2Col = len(m1[0]), len(copy[0])

    if m1Col == m2Row:
        m2 = new_matrix(m2Col, m1Row)

        for i, row in enumerate(m1):
            for j in range(m2Col):
                colArr = getColumn(j, copy)
                m2[i][j] = dotProduct(row, colArr)


def dotProduct(arr1, arr2):
    result = 0
    for el1, el2 in zip(arr1, arr2):
        result += el1 * el2
    return result


def getColumn(colNumber, arr):
    if isinstance(arr[0], list):
        col = []
        for row in arr:
            col.append(row[colNumber])
        return col
    return


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m

