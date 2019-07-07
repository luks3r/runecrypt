# runecrypt
Simple crypt tools based on runic alphabet and random keys.

- Currently only supports russian alphabet, but you can improve that, if you need it.

Usage:
```py
import runecrypt as rc

key = 3
some_crypted_text = rc.crypt("Some Text", key)

# Or

decrypted = rc.decrypt(some_crypted_text, key)
```

