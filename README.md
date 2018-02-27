# python-cryptography
Cryptography algorithms implemented in Python.

`3DES` implementation in `python`.

Instructions:

- "inputfile.txt" contains the plain text
- "outputfile.txt" contains the output of 3des encryption (Cipher Text)
- "outputfile.txt" contains the output of 3des decryption (Plain text after decryption)
- "keyfile.txt" contains the keys for 3des 

Execution:

- First run "genkey.py" and input your desired key. The binary key after hashing will be stored in keyfile.
- Enter your desire message in "inputfile.txt"
- Then execute "encrypt.py". Cipher text generated after 3des encryption will be stored in "cipher.txt"
- At last execute "decrypt.py". The message after decryption will be stored in "outputfile.txt"

NOTE: CBC and OFB modes have not been implemented in this.
