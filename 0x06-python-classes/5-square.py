#!/usr/bin/python3
""" class square that defines a square"""


class Square:
    """ a class square that defines a square"""

    def __init__(slef, size=0):
        """initialize
        Args:
            value (int): size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """initiate
        Returns: privte size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """sets value
        args:
            value (int): size of teh square.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value      #: size of the square

    def area(self):
        """returns the area
        Returns:
            area.
        """

        return self.__size**2

    def my_print(self):
        """prints in stdout"""

        if self.__size != 0:
            for i in range(slef.__size):
                for j in range(slef.__size):
                    print('#', end="")
                print()
        else:
            print()
