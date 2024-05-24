#!/usr/bin/env python3
""" Shapes, Interfaces, and Duck Typing
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class representing a shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of a shape.
        This method should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the object.

        Returns:
            The perimeter of the object.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Calculates the area of the circle.
        perimeter(): Calculates the perimeter of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle object with the given radius.

        Args:
            radius (float): The radius of the circle.

        Returns:
            None
        """
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return abs(2 * pi * self.__radius)

class Rectangle(Shape):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.

    Args:
        shape (Shape): The shape object for which to calculate and print the area and perimeter.

    Raises:
        TypeError: If the given shape is not an instance of the Shape class.

    Returns:
        None
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
