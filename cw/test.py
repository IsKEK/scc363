# Required modules 
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend 

def encrypt(key, iv, plainText):
# Generate an initialisation vector
# Construct an AES-CTR Cipher object with the given key and randomly generated initialisation vector
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(plainText)
    return (cipherText, iv)

def xorThisPls(var, key):
    x = zip(var, key)
    print(tuple(x))
    return bytes(a ^ b for a, b in x)

def findCiphertext(): 
    messageA = b"I'll give you 500 and that's my last offer."
    messageB = b"I'll give you 100 and that's my last offer."
    cipherTextA = b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4"
    key = os.urandom(32)
    iv = os.urandom(16)
    cipherText1 = encrypt(key, iv, messageA)
    cipherText2 = encrypt(key, iv, messageB)
    # print(cipherText1)
    # print(cipherText2)
    someBs = xorThisPls(messageA, cipherTextA)
    print(xorThisPls(messageB, someBs))
    # if (byteText == messageA):
    #     foundKey = key
    #     foundIv = iv
    #     print("success")
    # plainText = byteText.decode("utf-8")
    cipherTextB = ""
    return cipherTextB #ciphertext of messageB in bytes
    
if __name__ == "__main__":
    cipherText = findCiphertext()
    print(cipherText)