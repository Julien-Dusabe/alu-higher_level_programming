#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list and saves
them to a file named 'add_item.json' as a JSON representation. If the file
does not exist, it creates the file and initializes it.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        # Load the existing list from 'add_item.json'
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file does not exist, initialize an empty list
        items = []

    # Add the command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to 'add_item.json'
    save_to_json_file(items,
