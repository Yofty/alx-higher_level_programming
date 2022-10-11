#!/usr/bin/python3
"""a class Square that defines a square"""
class Square:
    """a class Square that defines a square """
    def __init__(self, size=0):
        """initialize"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size mustbe >= 0')
        else:
            self.__size = size #: size of the square

    def area(self):
        """returns the area"
        return self.__size**2
