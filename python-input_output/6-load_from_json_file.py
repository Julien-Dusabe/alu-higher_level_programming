#!/usr/bin/python3
"""
Module to create an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object parsed from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
