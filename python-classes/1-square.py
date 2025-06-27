#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (no validation for now).
        """
        self.__size = size
