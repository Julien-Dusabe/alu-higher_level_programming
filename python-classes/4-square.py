#!/usr/bin/python3
"""This module defines a Square class with property access to size."""


class Square:
    """Represents a square with controlled access to size."""

    def __init__(self, size=0):
        """Initialize the square with a validated size."""
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
