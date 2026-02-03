#!/usr/bin/env python3
"""Element-wise ops on two 2D lists."""


def _shape_2d(m):
    """Return (rows, cols) on valid 2D list, otherwise None."""
    try:
        cols = len(m[0])
        ok = (
            isinstance(m, list)
            and len(m) > 0
            and isinstance(m[0], list)
            and all(map(lambda r: isinstance(r, list) and len(r) == cols, m))
        )
        return ok and (len(m), cols) or None
    except Exception:
        return None


def _element_ops(mat1, mat2):
    rows = list(
        map(
            lambda r1, r2: (
                list(map(lambda x, y: x + y, r1, r2)),
                list(map(lambda x, y: x - y, r1, r2)),
                list(map(lambda x, y: x * y, r1, r2)),
                list(map(lambda x, y: x / y, r1, r2)),
            ),
            mat1,
            mat2,
        )
    )
    return tuple(map(list, zip(*rows)))


def np_elementwise(mat1, mat2):
    """Return (add, sub, mul, div) on 2D lists, or None."""
    s1 = _shape_2d(mat1)
    s2 = _shape_2d(mat2)
    ok = (s1 is not None) and (s1 == s2)
    return ok and _element_ops(mat1, mat2) or None
