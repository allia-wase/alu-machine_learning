#!/usr/bin/env python3
"""Performs elementwise operations on two 2D matrices (lists)."""


def np_elementwise(mat1, mat2):
    """Return tuple (sum, difference, product, quotient) of two matrices.

    Returns None if the matrices have mismatched dimensions.
    """
    if mat1 == [] or mat2 == []:
        return None

    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    rows = len(mat1)
    cols = len(mat1[0])

    sum_m = [
        [mat1[i][j] + mat2[i][j] for j in range(cols)]
        for i in range(rows)
    ]
    diff_m = [
        [mat1[i][j] - mat2[i][j] for j in range(cols)]
        for i in range(rows)
    ]
    prod_m = [
        [mat1[i][j] * mat2[i][j] for j in range(cols)]
        for i in range(rows)
    ]
    quot_m = [
        [mat1[i][j] / mat2[i][j] for j in range(cols)]
        for i in range(rows)
    ]

    return sum_m, diff_m, prod_m, quot_m
