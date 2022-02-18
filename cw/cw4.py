# Required modules 
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend 

def xorMessages(message1, message2):
    # xor every byte of message 1 with message 2
    # the byte strings doesn't have to be the same size because zip functions zips to whatever byte string is the shortest
    return bytes([a ^ b for a, b in zip(message1, message2)])

def findCiphertext(): 
    messageA = b"I'll give you 500 and that's my last offer."
    messageB = b"I'll give you 100 and that's my last offer."
    cipherTextA = b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4"
    keyAndIvValue = xorMessages(messageA, cipherTextA) # xor message a plaintext and ciphertext to get the added value of key, iv and counter
    cipherTextB = xorMessages(messageB, keyAndIvValue) # xor the found value with message b plaintext to find it's ciphertext
    return cipherTextB #ciphertext of messageB in bytes
    
if __name__ == "__main__":
    cipherText = findCiphertext()
    print(cipherText)