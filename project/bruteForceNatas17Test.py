#!/usr/bin/env python3
import requests

password = list("b")
endIndex = 0
usernm = "natas17"
passwd = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
url = "http://natas17.natas.labs.overthewire.org"
session = requests.Session()

print(f"Trying: {"".join(password)}")
res = session.post(url, data={"username":"submit":"Check existence"}, auth = (usernm, passwd))
print(res.text)


