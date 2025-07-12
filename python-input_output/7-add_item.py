#!/usr/bin/python3
"""Script that adds arguments to a list and saves them to a JSON file."""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with an empty list
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Extend list with command-line arguments
my_list.extend(sys.argv[1:])

# Save updated list to JSON file
save_to_json_file(my_list, filename)

