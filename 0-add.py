#!/usr/bin/env python3
"""
This module provides a function to add two float numbers.
"""
import sys


def add(a: float, b: float) -> float:
    """
    This function takes two float numbers as input and returns their sum.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of the two numbers.
    """

    return a + b


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./0-add.py <float1> <float2>")
    else:
        try:
            float1 = float(sys.argv[1])
            float2 = float(sys.argv[2])
            result = float1 + float2
            print(f"The sum of {float1} and {float2} is {result}.")
        except ValueError:
            print("Please provide valid float number")
