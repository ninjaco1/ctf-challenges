from pwn import * 
import os
import time

p = process("./exatlon_v1")

# get the initial text
print(p.recv().strip().decode("utf-8"))
print(p.recv().strip().decode("utf-8"))
print(p.recv().strip().decode("utf-8"))
print(p.recv().strip().decode("utf-8"))


# Enter exatlon password: 
print(p.recv().strip().decode("utf-8"))

# send correct password
# the numbers are multiple of 16
raw_data = "1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000 "
raw_data = raw_data.strip().split(' ')
password = ''

# print("raw_data: ", raw_data)

for num in raw_data:
    # n = int(int(num) / 16)
    # print(n)
    password += chr(int(int(num)/16))

print("password: ", password)
p.send(password.encode())



print(p.recv().strip().decode())


p.interactive()