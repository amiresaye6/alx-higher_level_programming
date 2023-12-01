#!/usr/bin/python3
"""notes for 0x11-python-network_1 task"""


"""
urllib packadge
request:        open URLs
response:       used internally
error:          request exceptions
parse:          usful URL functions
robotparser:    robots.txt files

import urllib
from urllib import request
resp = request.urloen("https://google.com")

resp.code >> 200
resp.length >> 7522
resp.peak() >> bytes opject thing
data = resp.read()
html = data.decode("UTF-8)
if you try to read the resp again, nothing will happesn
becaue python colsses the connection after reading.

resp = request.urlopen("https://www.youtube.com/watch?v=LosIGgon_KM")

from urllib imprt parse
params = {"v": "Ecsi34", "t": "3534s"}
querystring = parse.urlencode(params)
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
resp.isclosed() >> False
resp.code >> 200
html = resp.read().decode("UTF-8")
the result is html string :)
"""
