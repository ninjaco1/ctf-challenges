# Cryptography Challenge AES

server.py is a program of what the server is running.
When looking at the code it can be seen that it is using output feedback mode(OFB).
`https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_feedback_(OFB)`
When looking at the encrypt function it be seen that the nonce, which is the IV encrypted with a key, is prepend onto cipher message. Together the nonce and the cipher message creates the ciphertext. 
