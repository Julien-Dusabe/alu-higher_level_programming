#!/usr/bin/python3
"""Script that adds arguments to a list, then saves it to a JSON file."""

import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if the file exists, else start fresh
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments to the list (excluding script name)
my_list.extend(sys.argv[1:])

# Save the updated list
save_to_json_file(my_list, filename)

