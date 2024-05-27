#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json
import os


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.

    Args:
        my_obj: Object to write to text file.
        filename (str): name of the file.
    """
    # Convert set to list for JSON serialization
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    try:
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(my_obj, f)
    except PermissionError as e:
        print(f"[PermissionError] {e}")

# Example usage
data = {1, 2, 3}
save_to_json_file(data, 'file_7')
