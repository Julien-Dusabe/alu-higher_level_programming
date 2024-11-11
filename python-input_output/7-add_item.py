#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main():
    """
    This script adds command-line arguments to a list and saves the list as a JSON
    representation in a file named 'add_item.json'. If the file doesn't exist, it is created.
    """
    # Load existing items from the JSON file, if the file exists
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file does not exist, initialize an empty list
        items = []

    # Add command-line arguments (excluding the script name) to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to the 'add_item.json' file
    save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    main()
