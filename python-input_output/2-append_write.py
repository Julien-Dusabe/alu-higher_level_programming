#!/usr/bin/python3
"""
Module to append a string to a UTF-8 encoded text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8.

    Args:
        filename (str): The path to the file to be appended to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
