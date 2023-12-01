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


"""
requests packadge.
test url https://xkcd.com/688/
"""
import requests

r = requests.get("https://xkcd.com/688/")

# print(r)
# print(dir(r)) # will show all attributes available
# print(help(r)) # will show it in more details

"""
r.content >> in bytes, you may use it for downloading images, videos and so on
r.text    >> in unicode, you can use it for text, html code, etc
"""
# print(r.text)
"""
lets download a photo from the internet and put it in photo.png
"""
# new_image = requests.get("https://imgs.xkcd.com/comics/grownups.png")
# with open ("photo.png", "wb") as f:
#     f.write(new_image.content)

"""
this part is to check status
2XX >> every thing is ok
3XX >> redirect
4XX >> client error
5XX >> server error
"""
print(r.status_code)

print(r.ok) # returns true for all status codes under 400

"""
if you want to see all headers withen the response use the r.headers
"""
headers_dict = r.headers
headers_dict["Content-Type"]

"""
try to pass parameters
"""
payload = {"page": 3, "count": 345}
r = requests.get("url example", params=payload)
print(r.url) # will return the new url with the params attached to it

"""
try to post some data to the url
"""

r = requests.post('url example', data=payload)

"""
if we type r.json() this will creat a json dict from our response
we can caputr it in a var
"""

resp_dict = r.json()

"""
authontication withen the url
note that the usrname and password must be passed withen the url
and be the same at the auth to authonticate
"""
r = requests.get("authontication url", auth=('username', 'password'))


"""
if we want to delay the response for time out
if the resposne is over the time out it will through a ReadTimeout exception

"""
r = requests.get("url example", timeout=3)
