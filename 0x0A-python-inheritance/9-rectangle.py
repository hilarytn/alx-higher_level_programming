#!/usr/bin/python3i
"""Import module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Class that defines Rectangle and inherits from BaseGeometry"""
    def __init__(self, width, height):
	"""Initialize instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
	"""Define area"""
        return self.__width * self.__height

    def __str__(self):
        """String method for printing"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
