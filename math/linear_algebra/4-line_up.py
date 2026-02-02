#!/usr/bin/env python3
""" implements the add array method
"""


def add_arrays(arr1, arr2):
<<<<<<< HEAD
    """ adds two arrays elementwise
    """
    if len(arr1) != len(arr2):
        return None
=======
        """ adds two arrays elementwise
            """
                if len(arr1) != len(arr2):
                            return None
>>>>>>> e76e855950a5c5c700b4722dc04788199c6002c1

                            result = []

                                for num1, num2 in zip(arr1, arr2):
                                            result.append(num1 + num2)


