#!/usr/bin/python3
"""This module defines a Square class that computes its area."""


class Square:
    """Represents a square with size and an area calculator."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square, must be >= 0.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
