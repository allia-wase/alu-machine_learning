#!/usr/bin/env python3
'''
    This script has a function def np_transpose(matrix)
    that transposes matrix:
'''


def np_transpose(matrix):
    '''
        A function def np_transpose(matrix)
        that transposes matrix:
    '''
    # Return empty list for empty matrix
    if matrix == []:
        return []

    # Transpose the matrix (works for rectangular matrices)
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
