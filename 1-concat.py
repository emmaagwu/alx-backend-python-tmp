#!/usr/bin/env python3
"""
This module provides a function to concatenate two strings.
"""
import sys


def concat(str1: str, str2: str) -> str:
    """
    This function takes two strings as input and returns their concatenation.

    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenation of the two strings.
    """

    return str1 + str2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./1-concat.py <string1> <string2>")
    else:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
        result = str1 + str2
        print(f"{str1} + {str2} = {result}")
