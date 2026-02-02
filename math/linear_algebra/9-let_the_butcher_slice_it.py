#!/usr/bin/env python3
"""Matrix slicing helper functions (no numpy)"""
def get_middle_rows(m):  # noqa
    return [] if not m else [row[:] for row in m[1:3]]

def get_middle_columns(m):  # noqa
    return [] if not m else [[r[2], r[3]] for r in m]

def get_bottom_right(m, size=3):  # noqa
    return [] if not m else [r[-size:] for r in m[-size:]]
