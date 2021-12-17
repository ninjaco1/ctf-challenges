# impossible password

# important
1. first input = SuperSeKretKey
2. random number
3. key -> that is use to decode the flag 

## python decode script

```py

key = 'A]Kr=9k0=0o0;k1?k81t'
flag = ''

for l in key:
    flag += chr(ord(l) ^ 9)

print(flag)


```

## write up 
Opening up the decompiler code for this binary you can see that flag is encoded but to decode it all you do is XOR that key with 9 `(key ^ 9)`. Each character in the string is XOR with 9 after that it will give you the flag. 

## flag 
`HTB{40b949f92b86b18}`