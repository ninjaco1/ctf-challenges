# Cryptography Challenge AES

`server.py` is a program of what the server is running.
When looking at the code it can be seen that it is using output feedback mode(OFB).\
`https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_feedback_(OFB)`\
When looking at the encrypt function it be seen that the nonce, which is the IV encrypted with a key, is prepend onto cipher message. Together the nonce and the cipher message creates the ciphertext. Which means that when the ciphertext prints out the first 16 bytes are the nonce. 

`key = get_random_bytes(16)`\
`nounce = IV xor key`

Next creating `pwn.py` which is a program to find the decrypted cipher.\
`plaintext = encrypted_message xor encrypted_flag`\
Also can be seen in function `get_plain_text()` also can be seen below

``` python
def get_plain_text(e_one, e_two, p_bytes):
    first_block = list()
    for i in range(len(e_two)):
        first_block.append(e_one[i] ^ e_two[i])
        first_block[i] ^= p_bytes[i]
        first_block[i] = chr(first_block[i])
    return "".join(first_block)
```


