# Include any required modules
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt(key, plainText):
# Generate an initialisation vector
    iv = os.urandom(16)
# Construct an AES-CTR Cipher object with the given key and randomly generated initialisation vector
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(str.encode(plainText))
    return (cipherText, iv)

def decrypt(key, cipherText, iv):
# Construct an AES-CTR Cipher object with the given key and iv to decrypt
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    decryptor = cipher.decryptor()
    byteText = decryptor.update(cipherText) + decryptor.finalize()
    plainText = byteText.decode("utf-8")
    return (plainText)
# Main

if __name__ == "__main__":
    key = os.urandom(32)
    plainText = "some test string"
    cipherText, iv = encrypt(key, plainText)
    print("cipher text is: " + cipherText)
    newPlainText = decrypt(key, cipherText, iv)
    print(newPlainText)
"""
1. Create a key for AES and a plaintext
2. Encrypt the plaintext and print the result
3. Decrypt the ciphertext and print the result
"""