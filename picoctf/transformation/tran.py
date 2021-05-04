#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
import shutil
# opening the file 
enc = open("enc",'r',encoding='UTF-8').read()

#finding out the encoded message
print(enc)
# print (hex(ord(enc[0])))


flag = "" # flag as hex values
for i in range(len(enc)):
    
    flag += (hex(ord(enc[i]))[2:])

bytes_object = bytes.fromhex(flag)
print(bytes_object.decode("ASCII"))