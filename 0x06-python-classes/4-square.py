#!/usr/bin/python3
"""This is the square class"""


class Square:
    """A class that define the size"""
    def __init__(self, size=0):
        """Initialize the size"""
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
