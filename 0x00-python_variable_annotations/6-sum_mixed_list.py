#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """list mxd_lst of integers and floats and returns their sum as a float"""
    sum = 0
    for element in mxd_lst:
        sum += element
    return sum
