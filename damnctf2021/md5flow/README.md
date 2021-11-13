# md5flow


# read_key function
```c
void read_key()
{
	unsigned char key_buf[16];

	FILE* urandom = fopen("/dev/urandom", "rb");
	if (!urandom) exit(EXIT_FAILURE);
	if (fread(key_buf, 16, 1, urandom) != 1) exit(EXIT_FAILURE);
	if (fclose(urandom)) exit(EXIT_FAILURE);

	AES_set_encrypt_key(key_buf, 128, &key);
}

```


