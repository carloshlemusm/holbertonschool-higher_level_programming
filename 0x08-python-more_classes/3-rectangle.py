#!/usr/bin/python3
"""This is a rectangle class"""


class Rectangle:
    """Class rectangle"""

    def __init__(self, width=0, height=0):
        """This part define the instance method"""
        self.width = width
        self.height = height

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        return(self.__height)

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return(self.width * self.height)

    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return(0)

        return((2 * self.width) + (2 * self.height))

    def __str__(self):

        rectangle = ''
        if self.height is 0 or self.width is 0:
            return(rectangle)
        for i in range(self.height):
            rectangle += ('#' * self.width)
            if i != self.height - 1:
                rectangle += '\n'
        return(rectangle)
