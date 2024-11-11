#!/usr/bin/python3
"""
Module to read and print the contents of a UTF-8 encoded text file.
"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
