#!/usr/bin/env pyhthon

# from pwn import *

# p = process('./impossible_password.bin')


# print(p.recvline().strip())
# p.send('SuperSeKretKey')

# print(p.recvline().strip())
key = 'A]Kr=9k0=0o0;k1?k81t'
flag = ''

for l in key:
    flag += chr(ord(l) ^ 9)

print(flag)