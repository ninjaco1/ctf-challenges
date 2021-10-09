# CTF Fall 2021 Week 2

## main function

```as
    0x0000000000400a81 <+0>:     push   rbp
    0x0000000000400a82 <+1>:     mov    rbp,rsp
    0x0000000000400a85 <+4>:     mov    rax,QWORD PTR [rip+0x200614]        # 0x6010a0 <stdin@@GLIBC_2.2.5>
    0x0000000000400a8c <+11>:    mov    esi,0x0
    0x0000000000400a91 <+16>:    mov    rdi,rax
    0x0000000000400a94 <+19>:    call   0x400720 <setbuf@plt>
    0x0000000000400a99 <+24>:    mov    rax,QWORD PTR [rip+0x2005f0]        # 0x601090 <stdout@@GLIBC_2.2.5>
    0x0000000000400aa0 <+31>:    mov    esi,0x0
    0x0000000000400aa5 <+36>:    mov    rdi,rax
    0x0000000000400aa8 <+39>:    call   0x400720 <setbuf@plt>
    0x0000000000400aad <+44>:    mov    eax,0x0
    0x0000000000400ab2 <+49>:    call   0x400936 <password_check>
    0x0000000000400ab7 <+54>:    mov    eax,0x0
    0x0000000000400abc <+59>:    pop    rbp
    0x0000000000400abd <+60>:    ret 
```

## password check function

First program first generate a random. Then you want to send a line that is equal to the random number. After that it prints ` b'You passed the nonce check! Now, Unlock the UltraSecure(tm) Vault:'`. That means the inputted number matches the random number. After that you want to send the right number to print out the flag which is `-559041729 `. After that the flag will print out.

```c

void password_check(void)

{
  time_t tVar1;
  uint get_correct_rand;
  int local_3c;
  timeval local_38;
  timeval local_28;
  long local_18;
  uint rand_num;
  int correct_num;
  
  correct_num = -0x21524cc1;
  local_3c = 0;
  rand_num = 0;
  get_correct_rand = 0;
  tVar1 = time((time_t *)0x0);
  srand((uint)tVar1);
  rand_num = rand();
  gettimeofday(&local_28,(__timezone_ptr_t)0x0);
  printf("Prove that you are not human, repeat this to me in less than .05s: %d\n",(ulong)rand_num);
  __isoc99_scanf(&DAT_00400b9f,&get_correct_rand);
  gettimeofday(&local_38,(__timezone_ptr_t)0x0);
  local_18 = ((local_38.tv_sec - local_28.tv_sec) * 1000000 + local_38.tv_usec) - local_28.tv_usec;
  if (50000 < local_18) {
    puts("Whoops, too slow");
                    /* WARNING: Subroutine does not return */
    exit(-0x60);
  }
  if (rand_num != get_correct_rand) {
    puts("Whoops, wrong nonce!");
                    /* WARNING: Subroutine does not return */
    exit(-0x2a);
  }
  puts("You passed the nonce check! Now, Unlock the UltraSecure(tm) Vault:");
  __isoc99_scanf(&DAT_00400b9f,&local_3c);
  if (correct_num == local_3c) {
    print_flag();
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("Whoops, wrong password :(");
                    /* WARNING: Subroutine does not return */
  exit(-0x45);
}

```


## python script

```py

from pwn import *

# p = process("./ultrasecure") # local

c = remote("chal.ctf-league.osusec.org", 4545) # remote
context.log_level = "debug"
# 

s1 = c.recv() # receive first line

correct_random_num = s1.split(b':')[1].strip()
# print("check: " + correct_random_num)
c.sendline(correct_random_num)

s2 = c.recv()
print(s2)

deadbeef = -559041729    #0xdeadb33f

c.sendline(str(deadbeef).encode('utf-8'))

# s3 = c.recv()
# print(s3)

c.interactive()
```

## flag

`osu{d3c0mp1ler_go_brrrr}`