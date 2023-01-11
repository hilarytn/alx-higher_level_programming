#!/usr/bin/python3
"""Import modules"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define instance of rectangle as Square"""
    def __init__(self, size):
        """Initialize the instance of Rectangle"""
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String method for strings"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
