#!/usr/bin/env python3
"""Matrix slicing helper functions (no numpy)"""


def get_middle_rows(matrix):
    """Return the middle two rows of a 4xN matrix as a list of lists.

    Example: for a 4x6 matrix, returns rows 1 and 2 (0-indexed).
    """
    if matrix == []:
        return []
    return matrix[1:3]


def get_middle_columns(matrix):
    """Return the middle two columns (columns 2 and 3) as a list of rows.

    Each returned row is a list containing the selected columns.
    """
    if matrix == []:
        return []
    return [[row[i] for i in range(2, 4)] for row in matrix]


def get_bottom_right(matrix, size=3):
    """Return the bottom-right `size x size` submatrix as list of lists."""
    if matrix == []:
        return []
    return [row[-size:] for row in matrix[-size:]]
