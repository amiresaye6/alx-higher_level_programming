#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""


if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    params = {"email": argv[2]}
    queriedstring = parse.urlencode(params).encode("ascii")

    url = request.Request(argv[1], queriedstring)

    with request.urlopen(url) as resp:
        val = resp.read().decode("UTF-8")
        print(val)
