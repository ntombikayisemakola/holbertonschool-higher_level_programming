#!/usr/bin/python3
"""
Contains the "save_to_json_file" function
"""

import json

def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(my_obj, f)
    except PermissionError as e:
        print(f"[PermissionError] {e}")

# Example usage with set data type
data = {1, 2, 3}
data_list = list(data)

# Attempt to save to a file with permissions
try:
    save_to_json_file(data_list, 'file_7')
except TypeError as e:
    print(f"[TypeError] {e}")

# Attempt to save to a file in a directory without permissions
try:
    save_to_json_file(data_list, 'no_perm/file_7')
except PermissionError as e:
    print(f"[PermissionError] {e}")
