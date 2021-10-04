# CTF Fall 2021 Week 1

## Hash Brown

First thing to do is inspect element. When you inspect element the page you will see all the elements and the script at the end of the code.
Looking at the script element of the code it tells us that the password has to equal a certain hash of
`b0fef621727ff82a7d334d9f1f047dc662ed0e27e05aa8fd1aefd19b0fff312c`. To undo this hash go to the wesbite CrackStation[https://crackstation.net/].
The hash was in sha256 format so you have to unhash that.

```js
<script>
    function get_sha256(password) {
        return sjcl.codec.hex.fromBits(sjcl.hash.sha256.hash(password));
    }
    function check_password() {
        let password = document.getElementById("password").value;
        let hash = get_sha256(password);
        if (hash == "b0fef621727ff82a7d334d9f1f047dc662ed0e27e05aa8fd1aefd19b0fff312c") {
            document.getElementById("login").submit();
        }
        else {
            document.getElementById("wrong_label").style.transform = "translate(-50%, -50%) scale(100%)";
            document.getElementById("wrong_label").style.opacity = "100%";
            setTimeout(() => {
            document.getElementById("wrong_label").style.transform = "translate(-50%, -50%) scale(75%)";
            document.getElementById("wrong_label").style.opacity = "0%";
            }, 3000);
        }
    }

</script>
```

This will give us the password of `pineapple`. After typing the password it will show is site where we have to click on the text `get the flag!` and it will print has the flag.
Another way to get the flag is to inspect element again to for the script code for it again. When looking inside the print_flag function it show a string that is formatted ilke the flag 
`bfh{c1a34ccy3_u45u_Oe0jA5_4e3_t00Q}`. The code looks like it was a ROT13 encryption so when decrypting it, it will give us the flag.

```js
function print_flag() {
    p="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    a="bfh{c1a34ccy3_u45u_Oe0jA5_4e3_t00Q}";
    b=p[s="substr"](13)+p[s](0,13);
    p+=p[l="toLowerCase"]();
    b+=b[l]();
    o='';
    for(i=0;a[i];i++)o+=b[p.indexOf(a[i])]||a[i];
    document.getElementById("bouncyLink").innerHTML = o;
}

```


Flag
```
osu{p1n34ppl3_h45h_Br0wN5_4r3_g00D}
```