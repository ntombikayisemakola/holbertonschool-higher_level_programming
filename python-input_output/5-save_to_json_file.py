#!/usr/bin/python3
"""Defines a function that writes JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Using JSON representation write an object to a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
