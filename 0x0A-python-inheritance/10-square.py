#!/usr/bin/python3
"""Import Modules"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square as instance of rectangle"""
    def __init__(self, size):
        """Initialiaze class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
