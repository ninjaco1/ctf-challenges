from pwn import *

conn = remote("ctf.ropcity.com", 31337)

conn.recvuntil("Encrypted flag: ")
flag_text = conn.recvline().decode()

given_nonce = bytes.fromhex(flag_text[:32])
encrypted_flag = bytes.fromhex(flag_text[32:])

print(f"the nonce is given {given_nonce}")

def get_plain_text(e_one, e_two, p_bytes):
    first_block = list()
    for i in range(len(e_two)):
        first_block.append(e_one[i] ^ e_two[i])
        first_block[i] ^= p_bytes[i]
        first_block[i] = chr(first_block[i])
    return "".join(first_block)

my_plaintext = b'Hello_worldddddddddddddddddddddddddddddddddddddddddddddddddddddddd'.hex()

conn.recvuntil("?")
conn.sendline(my_plaintext)
conn.sendline(given_nonce.hex())
conn.recvuntil(": ")

# Decode the byte string into bytes
encrypted_message = bytes.fromhex(conn.recvline()[32:].decode())
print(f"the msg is {encrypted_message}")

print(get_plain_text(encrypted_message, encrypted_flag, bytes.fromhex(my_plaintext)))
