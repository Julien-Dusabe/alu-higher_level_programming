#!/usr/bin/python3
"""
Module to convert a Python object to a JSON string representation.
"""


import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to convert to JSON.

    Returns:
        str: JSON string representation of `my_obj`.
    """
    return json.dumps(my_obj)
