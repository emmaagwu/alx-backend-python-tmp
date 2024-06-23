#!/usr/bin/env python3
"""
This module provides a function to convert a
 float number to its string representation.
"""


def to_str(n: float) -> str:
    """
    This function takes a float number as input
      and returns its string representation.

    Parameters:
    n (float): The input float number.

    Returns:
    str: The string representation of the input number.
    """
    return str(n)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./3-to_str.py <float>")
    else:
        try:
            float1 = float(sys.argv[1])
            result = to_str(float1)
            print(result)
        except ValueError:
            print("Please provide a valid float number")
