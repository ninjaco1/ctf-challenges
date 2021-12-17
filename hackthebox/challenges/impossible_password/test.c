#include <stdio.h>
#include <stdlib.h>


int main(){

    char *var_ch;
    char *var_8h;
    char *arg1 = "A]Kr=9k0=0o0;k1?k81t"
    
    var_ch = 0;
    for (var_8h = arg1; *(char *)var_8h != '\t'; var_8h = var_8h + 1) {
        if (0x13 < var_ch) break;
        putchar((int32_t)(char)(*(uint8_t *)var_8h ^ 9));
        var_ch = var_ch + 1;
    }
    putchar(10);
    return;
}