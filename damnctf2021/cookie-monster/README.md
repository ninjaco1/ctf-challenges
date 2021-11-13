# cookie monster

nc dev-rcds-toxicz.damctf.xyz 31312


## bakery

```
    0x08048586 <+0>:     push   ebp
    0x08048587 <+1>:     mov    ebp,esp
    0x08048589 <+3>:     push   ebx
    0x0804858a <+4>:     sub    esp,0x34
    0x0804858d <+7>:     call   0x80484c0 <__x86.get_pc_thunk.bx>
    
    
    0x08048592 <+12>:    add    ebx,0x1a6e
    0x08048598 <+18>:    mov    eax,gs:0x14
    0x0804859e <+24>:    mov    DWORD PTR [ebp-0xc],eax
    0x080485a1 <+27>:    xor    eax,eax
    0x080485a3 <+29>:    sub    esp,0xc
    0x080485a6 <+32>:    lea    eax,[ebx-0x1888]
    0x080485ac <+38>:    push   eax
    0x080485ad <+39>:    call   0x8048400 <printf@plt>
    printf();
    
    
    0x080485b2 <+44>:    add    esp,0x10
    0x080485b5 <+47>:    mov    eax,DWORD PTR [ebx-0x8]
    0x080485bb <+53>:    mov    eax,DWORD PTR [eax]
    0x080485bd <+55>:    sub    esp,0x4
    0x080485c0 <+58>:    push   eax
    0x080485c1 <+59>:    push   0x20
    0x080485c3 <+61>:    lea    eax,[ebp-0x2c]
    0x080485c6 <+64>:    push   eax
    0x080485c7 <+65>:    call   0x8048410 <fgets@plt>
    fget();
    
    
    0x080485cc <+70>:    add    esp,0x10
    0x080485cf <+73>:    sub    esp,0xc
    0x080485d2 <+76>:    lea    eax,[ebx-0x1876]
    0x080485d8 <+82>:    push   eax
    0x080485d9 <+83>:    call   0x8048400 <printf@plt>
    printf()
    
    
    0x080485de <+88>:    add    esp,0x10
    0x080485e1 <+91>:    sub    esp,0xc
    0x080485e4 <+94>:    lea    eax,[ebp-0x2c]
    0x080485e7 <+97>:    push   eax
    0x080485e8 <+98>:    call   0x8048400 <printf@plt>
    printf()
    
    
    0x080485ed <+103>:   add    esp,0x10
    0x080485f0 <+106>:   sub    esp,0xc
    0x080485f3 <+109>:   lea    eax,[ebx-0x186c]
    0x080485f9 <+115>:   push   eax
    0x080485fa <+116>:   call   0x8048430 <puts@plt>
    puts()
    
    
    0x080485ff <+121>:   add    esp,0x10
    0x08048602 <+124>:   sub    esp,0xc
    0x08048605 <+127>:   lea    eax,[ebx-0x1846]
    0x0804860b <+133>:   push   eax
    0x0804860c <+134>:   call   0x8048440 <system@plt>
    system()
    
    
    0x08048611 <+139>:   add    esp,0x10
    0x08048614 <+142>:   sub    esp,0xc
    0x08048617 <+145>:   lea    eax,[ebx-0x1834]
    0x0804861d <+151>:   push   eax
    0x0804861e <+152>:   call   0x8048430 <puts@plt>
    
    
    0x08048623 <+157>:   add    esp,0x10
    0x08048626 <+160>:   mov    eax,DWORD PTR [ebx-0x8]
    0x0804862c <+166>:   mov    eax,DWORD PTR [eax]
    0x0804862e <+168>:   sub    esp,0x4
    0x08048631 <+171>:   push   eax
    0x08048632 <+172>:   push   0x40
    0x08048634 <+174>:   lea    eax,[ebp-0x2c]
    0x08048637 <+177>:   push   eax
    0x08048638 <+178>:   call   0x8048410 <fgets@plt>
    
    
    0x0804863d <+183>:   add    esp,0x10
    0x08048640 <+186>:   sub    esp,0xc
    0x08048643 <+189>:   lea    eax,[ebx-0x1812]
    0x08048649 <+195>:   push   eax
    0x0804864a <+196>:   call   0x8048430 <puts@plt>
    
    
    0x0804864f <+201>:   add    esp,0x10
    0x08048652 <+204>:   nop
    0x08048653 <+205>:   mov    eax,DWORD PTR [ebp-0xc]
    0x08048656 <+208>:   xor    eax,DWORD PTR gs:0x14
    0x0804865d <+215>:   je     0x8048664 <bakery+222>
    0x0804865f <+217>:   call   0x8048740 <__stack_chk_fail_local>
    
    
    0x08048664 <+222>:   mov    ebx,DWORD PTR [ebp-0x4]
    0x08048667 <+225>:   leave  
    0x08048668 <+226>:   ret 
```