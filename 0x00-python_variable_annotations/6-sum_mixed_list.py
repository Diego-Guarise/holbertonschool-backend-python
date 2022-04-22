#!/usr/bin/env python3

"""
Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list of floats
    """
    all: float = 0
    for ele in range(0, len(mxd_lst)):
        all = all + mxd_lst[ele]

    return all
