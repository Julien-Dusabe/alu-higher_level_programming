#!/usr/bin/python3
"""
This module allows appending command-line arguments to a list
stored in a JSON file. If the file doesn't exist, it creates a new file.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def main():
    """
    This script adds command-line arguments to a list and saves the list as a JSON
    representation in a file named 'add_item.json'. If the file doesn't exist, it is created.
    """
    try:
        items = load_from_json_file('add_item.json')
    except (FileNotFoundError, ValueError):
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    main()
