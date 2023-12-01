#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task
in less than 15 minutes.
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    resp = requests.get(url)
    resp_json = resp.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                resp_json[i].get("sha"),
                resp_json[i].get("commit").get("author").get("name")
                ))
    except IndexError:
        pass
