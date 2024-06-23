#!/usr/bin/env python3
"""
This module provides a function to calculate
the sum of a list of floats and integers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of floats and integers.

    Args:
        mxd_lst: A list of floats and integers.

    Returns:
        The sum of the mxd_lst as a float.

    """
    return float(sum(mxd_lst))
