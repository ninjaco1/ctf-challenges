import os

byte1 = 0x25504446
byte2 = 0xd6df472f



hexstring = byte1 ^ byte2
with open("bathhouse_password", "rb") as f:
    password = f.read(4)
    while password:
        os.write(1, (int.from_bytes(password,'big') ^ hexstring).to_bytes(4, 'big'))
        #os.write(1, hexstring) 
        password = f.read(4)

# out = <decrypted data>  
'''
with open("out.pdf", "wb") as f:
    f.write(out)
'''
