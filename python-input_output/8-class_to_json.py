#!/usr/bin/python3
"""Module that defines a function to return a dictionary representation of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization."""
    return obj.__dict__

