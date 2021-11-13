from pwn import *
import binascii 


def xorbreak(line):
    e = binascii.unhexlify(line) # makes it characters
    for key in range(256):
        d = ''.join(chr(b ^ key) for b in e)
        if d.isprintable():
            print(d)


path = './flags.txt'
file = open(path, 'r')

lines = []
for line in file:
    lines.append(line.strip())

file.close()

for line in lines:
    xorbreak(line)


