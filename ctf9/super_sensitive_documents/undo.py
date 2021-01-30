import sys

file = "flag.txt.sn0w"

f = open(file,"br")
key = f.read(32)
text = f.read()

nkey = []
for i in range(len(key)):
    nkey.append(int(key[i]) & 127 ^ 66)

fin = []
for i in range(len(text)):
    fin.append(text[i] ^ nkey[i % 32])

print(bytes(fin))

