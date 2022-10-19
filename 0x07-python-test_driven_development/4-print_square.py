#!/usr/bin/python3
"""
Module 4-print_square.py
"""


def print_square(size):
    """Prints a square with the character '#'

       Args:
       size(int): size length of the square

       Return:
       string: square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must ba an integer")
    if size < 0:
        raise ValueError("size must >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
