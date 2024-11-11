#!/usr/bin/python3
"""
Module to write a string to a UTF-8 encoded text file.
"""


def write_file(filename="", text=""):
    """
    A string to a text file (UTF8),returns the number of characters written.

    Args:
        filename (str): The path to the file to be written to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
