from itertools import *
import os

# if 'yes_please_remove_guardrail_friendo' not in os.environ.keys():
#     print('GUARDRAIL TRIPPED: This is probably a good thing!!!!!!!')
#     exit(1)

filename = 'flag.png'
with open(f"{filename}.MALD", 'rb') as (enc_f):
    enc_f_content = enc_f.read()


    # [137, 80, 78, 71, 13, 10, 26, 10]
    magic_bytes = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
    print(magic_bytes)

    enc = [a ^ b for a, b in zip(enc_f_content, cycle(magic_bytes))]
    with open(f"{filename}", 'wb+') as f:
        f.write(bytes(enc))
    # enc = [a ^ b for a, b in zip(, cycle(magic_bytes))]
    