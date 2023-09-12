#!/usr/bin/python3
"""file input / output"""
import json


def from_json_string(my_str):
    """returns (Python data structure) represented by a JSON string:"""

    return json.loads(my_str)
