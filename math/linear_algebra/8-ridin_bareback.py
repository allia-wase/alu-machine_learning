#!/usr/bin/env python3
'''
    This script has a function def mat_mul(mat1, mat2)
    that performs matrix multiplication
'''


def mat_mul(mat1, mat2):
    '''
        The function def mat_mul(mat1, mat2)
        performs matrix multiplication
    '''
    # Validate inputs: non-empty and compatible dimensions
    if mat1 == [] or mat2 == []:
        return None

    if len(mat1[0]) != len(mat2):
        return None

    rows = len(mat1)
    cols = len(mat2[0])
    common = len(mat2)

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            s = 0
            for k in range(common):
                s += mat1[i][k] * mat2[k][j]
            row.append(s)
        result.append(row)

    return result
