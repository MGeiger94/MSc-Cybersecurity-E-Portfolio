"""Encryption and Decryption of short text (e.g. passwords) using fernet"""

from cryptography.fernet import Fernet

# Key Generation
key = Fernet.generate_key()

print ("The generated key is: " + (str(key,'utf8')))

# Encryption

encrypter = Fernet (key)

pw = encrypter.encrypt(b'here could be a secret')
print("The encrypted phrase / password with fernet is: " + (str(pw,'utf8')))

# Decryption

decrypter = encrypter.decrypt(pw)
print ("The encrypted text was: " + (str(decrypter)))



print ("End of fernet paragraph")
print (" ")



"""Encryption and Decryption of short text (e.g. passwords) using hashlib"""

import hashlib


# Encryption using hashlib (sha256)

encrypter2 = hashlib.sha256()
encrypter2.update(b"here could be a password")
print ("The encrypted phrase / password with hashlib is: " + (encrypter2.hexdigest()))
print (" ")

# Encryption using key derivation with hashlib(from https://docs.pyhton.org/2/library/hashlib.html)

encrypter3 = hashlib.pbkdf2_hmac('sha256',b'here could be a password', b'additional character', 1000000)

print ("The multiple times encrypted phrase is: " +  (str(encrypter3)))





