#!/usr/bin/env python3
"""Element-wise ops on two 2D lists."""


def _shape_2d(m):
    """Return (rows, cols) if m is a proper 2D list, else None."""
    if not isinstance(m, list) or m == [] or not isinstance(m[0], list):
        return None

    cols = len(m[0])
    ok = all(map(lambda r: isinstance(r, list) and len(r) == cols, m))
    if not ok:
        return None

    return len(m), cols


def np_elementwise(mat1, mat2):
    """Return tuple: (add, sub, mul, div) on 2D lists."""
    s1 = _shape_2d(mat1)
    s2 = _shape_2d(mat2)
    if s1 is None or s2 is None or s1 != s2:
        return None

    add = list(
        map(
            lambda r1, r2: list(map(lambda x, y: x + y, r1, r2)),
            mat1,
            mat2,
        )
    )
    sub = list(
        map(
            lambda r1, r2: list(map(lambda x, y: x - y, r1, r2)),
            mat1,
            mat2,
        )
    )
    mul = list(
        map(
            lambda r1, r2: list(map(lambda x, y: x * y, r1, r2)),
            mat1,
            mat2,
        )
    )
    div = list(
        map(
            lambda r1, r2: list(map(lambda x, y: x / y, r1, r2)),
            mat1,
            mat2,
        )
    )

    return add, sub, mul, div
