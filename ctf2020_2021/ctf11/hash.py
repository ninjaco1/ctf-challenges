#!/usr/bin/env python3
from pwn import *
import binascii

from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# Evenly split 'data' into 'n' parts
def split_str(data: bytes, n: int):
    if len(data) % n != 0:
        print(f"Length of 'data' must be a multiple of {n}")
        raise ValueError

    section_len = len(data) // n
    return (data[i * section_len : (i + 1) * section_len] for i in range(n))

def sha(data: bytes):
    algo = SHA256.new(data)
    return algo.digest()

def xor(a: bytes, b: bytes):
    return bytes([x ^ y for x, y in zip(a, b)])

def secure_hash_tm(data: bytes):
    a, b, c = split_str(data, 3)
    w = xor(b, xor(sha(a), sha(c)))
    return xor(sha(w), a) + sha(c)

p = remote("ctf-league.osusec.org", 31312)
# get 2 lines 
print(p.recvline().decode())
print(p.recvline().decode())
p.sendline() # press enter

# get the next two lines
og_hash = p.recvline().decode() # get the new line
x = og_hash.split() # split string by spaces
y = binascii.unhexlify(x[4])
# print(y)
print(secure_hash_tm(y))
print(p.recvline().decode())
print(p.recvline().decode())
print(p.recvline().decode())

a, b, c = split_str(y, 3) # split into 3 strings
# print(a,b,c)


'''
keep c the same
choose arbinary b != to init b
xor resulting string from arbiary W with sha(W) to get A


w = b ^ (sha(a) ^ sha(c))
x = not orginal w


0. c is the same
1. we choose w ahead of time
2. xor resulting string from arbiary W with sha(W) to get A
3. b = x ^ (sha(a) ^ sha(c))
'''

# byte string
w = b'A' * 32
w0 = xor(b, xor(sha(a), sha(c))) # w0 is the original w


r = sha(w)
a = xor(xor(sha(w0), sha(w)), a)
b = xor(w, xor(sha(a),sha(c)))
print(b)

print(secure_hash_tm(a + b + c))
print(secure_hash_tm(y))

p.sendline(binascii.hexlify(a+b+c))
p.interactive()