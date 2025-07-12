#!/usr/bin/python3
"""Script that adds command-line arguments to a list and saves them in JSON format."""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if the file exists, else start with an empty one
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments (excluding script name)
my_list.extend(sys.argv[1:])

# Save back to JSON file
save_to_json_file(my_list, filename)

