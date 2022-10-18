#!/usr/bin/python3
"""defines rectangle"""


class Rectangle:
    """defines rectangle"""

    def __init__(self, height=0, width=0):
        """initialize"""
        self.width =width
        self.height = height

    @property
    def width(self):
        return slef.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return arae"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) (self.__height * 2))

    def __str__(self):
        """return printable represantation"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range((self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return the string"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
