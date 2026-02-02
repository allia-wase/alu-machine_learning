#!/usr/bin/env python3
"""Implements the np_shape function without numpy."""


def np_shape(matrix):
    """Return the shape of `matrix` as a tuple (rows, cols).

    For an empty matrix ([]) return (0,).
    """
    if matrix == []:
        return (0,)
    return (len(matrix), len(matrix[0]))
