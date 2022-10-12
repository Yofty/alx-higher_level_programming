#!/usr/bin/python3
"""a class square that defines a square"""


class Square:
    """private attribute"""

    def __init__(self, size=0):
        """initiallize
        Args:
            value (int): size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """int: private size.
        Returns:
            private size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets value"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value   #size of the square

    def area(self):
        """returns area
        Returns:
            area.
        """

        return self.__size**2
