#!/usr/bin/env python3
"""
This module provides a function to calculate the floor
 value of a given float number.
"""
import sys
import math


def floor(n: float) -> int:
    """
    Calculate the floor value of a given float number.

    Args:
        n (float): The input float number.

    Returns:
        int: The floor value of the input number.
    """
    return math.floor(n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-floor.py <float>")
    else:
        try:
            float1 = float(sys.argv[1])
            result = floor(float1)
            print(result)
        except ValueError:
            print("Please provide a valid float number")
