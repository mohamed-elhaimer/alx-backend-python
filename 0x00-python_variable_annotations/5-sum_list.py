#!/usr/bin/env python3
""" type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of the element of list as a float"""
    sum = 0
    for num in input_list:
        sum += num
    return sum
