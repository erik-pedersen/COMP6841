#!/usr/bin/env python3
import os

password = list("a")
endIndex = 0

def increment(password, endIndex):
    if (password[endIndex] == "z"):
        password[endIndex] = "A"
    elif (password[endIndex] == "Z"):
        print("Uhoh")
    else:
        password[endIndex] = chr(ord(password[endIndex]) + 1)

while (endIndex < 1):
    print(f'Trying: {"".join(password)}')
    if (password[endIndex] == "G"):
        print("yay")
        password.append("a")
        endIndex += 1
    else:
        print("nay")
        increment(password, endIndex)
print("".join(password))
