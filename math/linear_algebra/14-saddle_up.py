#!/usr/bin/env python3
"""Matrix multiplication without numpy."""


def np_matmul(mat1, mat2):
    """Return the matrix product of two 2D lists, or None on mismatch."""
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
