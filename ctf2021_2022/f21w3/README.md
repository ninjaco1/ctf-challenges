# secure-encryptor 


First connect to the port that the server is connected to. Then recieve lines from the program until the new line character is reach. When finding r xor each byte with 42 then xor with b[i] index. Then do the same thing with g but backwards. Then join g into a byte string. 

## python script

```py
# Skeleton pwntools script
from base64 import b64decode,b64encode
from pwn import *

# Open connection
conn = remote("chal.ctf-league.osusec.org", 4646)

##conn = process("secure-encryptor")
# Send & Receive commands
# Receives until pattern
print(conn.recvuntil(b"...\n"))
a = conn.recvuntil(b"==").strip().replace(b'\n', b'')
#print(a)
##a = int.from_bytes(b64decode(a),"big")
##print(a)
conn.recvuntil(b"u: ")
conn.sendline(b"00"*1024)
#print(b"00"*1024)
conn.recvuntil(b"!\n")
b = conn.recvuntil(b"==").strip().replace(b'\n', b'')
#print(b)


a=b64decode(a)
b=b64decode(b)
##b = int(b64decode(b))
c = b"0"*1024
r = []
for i ,item in enumerate(c):
    
    f = item ^ 42
    f = f ^ b[i]
    
    r.append(f)

g = []
for i ,item in enumerate(a):
    f = item ^ r[i]
    f = f ^ 42
    f = f.to_bytes(1,"big")
    g.append(f)

print(b"".join(g))

```

## flag
`osu{d0n7_u5e_4_1_71m3_p4d_m0r3_th4n_0nc3}`
