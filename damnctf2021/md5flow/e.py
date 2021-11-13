from pwn import *


# nc dev-rcds-toxicz.damctf.xyz 31656

# p = remote("dev-rcds-toxicz.damctf.xyz",31656)
p = process('./md5flow')

print("first recv: ", p.recv(), '\n')

option = b'0'
p.sendline(option)

print("second recv: ", p.recv(), '\n')
# print("3rd recv: ", p.recv(), '\n')

# send another buffer

p.interactive()
