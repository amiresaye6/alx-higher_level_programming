#!/usr/bin/python3
"""
0. What's my status? #0
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following
example (tabulation before -)
You must use a with statement
"""


if __name__ == '__main__':
    from urllib import request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        val = resp.read()
        encoded_val = val.decode("UTF-8")
        print("Body response:")
        print("\t- type: {}".format(type(val)))
        print("\t- content: {}".format(val))
        print("\t- utf8 content: {}".format(encoded_val))
