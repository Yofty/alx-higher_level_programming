#!/usr/bin/python3
"""a class Square that defines a square"""


def __init__(self, size=0):
    """initializes the size variable"""

    self.__size = size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
