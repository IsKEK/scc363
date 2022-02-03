import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def generateKeys():
    privateKey = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    publicKey = privateKey.public_key()
    return (privateKey, publicKey)

def encrypt(plainText, publicKey):
    byteText = plainText.encode("utf-8")
    cipherText = publicKey.encrypt(byteText, padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    return cipherText

def decrypt(cipherText, privateKey):
    plainText = privateKey.decrypt(cipherText, padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    plainText = plainText.decode("utf-8")
    return plainText

if __name__ == "__main__":
    privateKey, publicKey = generateKeys()
    plainText = input()
    cipherText = encrypt(plainText, publicKey)
    print(cipherText)
    newPlainText = decrypt(cipherText, privateKey)
    print(newPlainText)

    # Encrypt the plaintext with the public key and print the result.
    # Decrypt the cipher with the private key and print the result.