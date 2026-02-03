#!/usr/bin/env python3
"""Element-wise numpy ops."""

import numpy as np


def np_elementwise(mat1, mat2):
    """Compute element-wise sum, difference, product, quotient.

    Returns:
        tuple: (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
        None: if inputs are not 2D or shapes differ
    """
    a = np.array(mat1)
    b = np.array(mat2)

    if a.ndim != 2 or b.ndim != 2:
        return None
    if a.shape != b.shape:
        return None

    return a + b, a - b, a * b, a / b
