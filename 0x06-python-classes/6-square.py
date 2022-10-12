#!/usr/bin/python3
"""define class square"""


class Square:
    """defien class square"""

    def __init__(slef, size=0):
        """initialize
        Args:
            size (int): the size of the new square.
            position (int, int): the positionof the new square.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """get the current size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif vaue < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            slef.__position = value

    def area(slef):
        """Return the current area"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, slef.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
