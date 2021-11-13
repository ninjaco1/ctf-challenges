# maldiant

First you need to extract the file the quarterly_report.pdf using pyinstxtractor.
Then you will see a file called `not_odysseus.pyc`. Then you use the python uncomplier to get the code for the file.


## 
```py
# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
# [GCC 9.3.0]
# Embedded file name: not_odysseus.py
from itertools import *
import os
# if 'yes_please_remove_guardrail_friendo' not in os.environ.keys():
#     print('GUARDRAIL TRIPPED: This is probably a good thing!!!!!!!')
#     exit(1)

def encrypt_and_destroy(filename):
    try:
        with open(filename, 'rb') as (f):
            raw = f.read()
        magic_bytes = raw[:8]
        print(magic_bytes)
        enc = [a ^ b for a, b in zip(raw, cycle(magic_bytes))]
        with open(f"{filename}.MALD", 'wb+') as (enc_f):
            enc_f.write(bytes(enc))
        os.remove(filename)
    except FileNotFoundError:
        print('Bad file, please try again!')


encrypt_and_destroy('flag.png.MALD')
# okay decompiling not_odysseus.pyc


```


## python exploit
```py
from itertools import *
import os

def encrypt_and_destroy(filename):
    try:
        with open(filename, 'rb') as (f):
            raw = f.read()
        magic_bytes = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'#raw[:8]
        print(magic_bytes)
        enc = [a ^ b for a, b in zip(raw, cycle(magic_bytes))]
        with open(f"{filename}", 'wb+') as (enc_f):
            enc_f.write(bytes(enc))
        # os.remove(filename)
    except FileNotFoundError:
        print('Bad file, please try again!')


encrypt_and_destroy('flag.png.MALD')

```

After running this script you can open the `flag.png` file and the flag will be on the image of the file.

## flag 

`osu{M@G1C_ByT3S_AR3_N3At}`