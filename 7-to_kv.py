#!/usr/bin/env python3
"""
This module provides a function to calculate the square of an int or float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and an int or float as arguments
    and returns a tuple. The first element of the tuple is the
    string argument and the second element is the square of the
    int or float argument.

    Args:
        k: A string.
        v: An int or float.

    Returns:
        A tuple containing the string k and the square of v.

    """
    return (k, v ** 2)
