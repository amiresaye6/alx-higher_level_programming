#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display the
    id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
"""


if __name__ == '__main__':
    from sys import argv
    import requests
    url = "http://0.0.0.0:5000/search_user"

    if (len(argv) == 1):
        resp = requests.post(url, params={"q": ""})

    else:
        resp = requests.post(url, params={"q": argv[1]})

    try:
        resp_json = resp.json()
        if resp_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp_json.get("id"), resp_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
