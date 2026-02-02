#!/usr/bin/env python3
"""Concatenate two 2D matrices (lists) along the given axis (no numpy)."""


def np_cat(mat1, mat2, axis=0):
    """Concatenate `mat1` and `mat2` along axis 0 (rows) or axis 1 (cols).

    Returns None if dimensions are incompatible.
    """
    if axis == 0:
        # number of columns must match
        if mat1 == [] and mat2 == []:
            return []
        if mat1 == []:
            return mat2.copy()
        if mat2 == []:
            return mat1.copy()
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1.copy() + mat2.copy()
    elif axis == 1:
        # number of rows must match
        if len(mat1) != len(mat2):
            return None
        return [r1 + r2 for r1, r2 in zip(mat1, mat2)]
    else:
        return None
