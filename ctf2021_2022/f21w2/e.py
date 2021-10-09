# NAME: ultrasecure
# CATEGORY: rev
# POINTS: 200
# DOWNLOAD LINK: http://chal.ctf-league.osusec.org:1337/static/ultrasecure
# ACCESS: nc chal.ctf-league.osusec.org 4545
# DESCRIPTION: Use pwntools and ghidra to reverse engineer and break into the ultrasecure(tm) vault!


from pwn import *

# p = process("./ultrasecure") # local

c = remote("chal.ctf-league.osusec.org", 4545) # remote
context.log_level = "debug"
# 

s1 = c.recv() # receive first line

correct_random_num = s1.split(b':')[1].strip()
# print("check: " + correct_random_num)
c.sendline(correct_random_num)

s2 = c.recv()
print(s2)

deadbeef = -559041729    #0xdeadb33f

c.sendline(str(deadbeef).encode('utf-8'))

# s3 = c.recv()
# print(s3)

c.interactive()