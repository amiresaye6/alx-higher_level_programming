#!/usr/bin/python3
"""
Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """

    # with open("temp.txt", "w", encoding="utf-8") as file_w:
    #     with open(filename, "r", encoding="utf_8") as file_r:
    #         for line in file_r:
    #             file_w.write(line)
    #             if search_string in line:
    #                 file_w.write(new_string)
    # with open("temp.txt", "r", encoding="utf-8") as file_w:
    #     with open(filename, "w", encoding="utf-8") as file_r:
    #         for line in file_w:
    #             file_r.write(line)
    with open(filename, "r", encoding="utf-8") as file_r:
        line_list = []
        for line in file_r:
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, "w", encoding="utf-8") as new_file:
        new_file.writelines(line_list)


append_after("aa.txt", "Python", "\"C is fun!\"\n")
