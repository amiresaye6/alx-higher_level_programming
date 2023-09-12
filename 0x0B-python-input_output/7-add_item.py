#!/usr/bin/python3
"""file input /output"""


from sys import argv
load_from_json = __import__("6-load_from_json_file").load_from_json_file
save_to_json = __import__("5-save_to_json_file").save_to_json_file


fileName = "add_item.json"

try:
    """if the file exists"""
    json_list = load_from_json(fileName)
except FileNotFoundError:
    json_list = []
for arg in argv[1:]:
    json_list.append(arg)

save_to_json(json_list, fileName)
