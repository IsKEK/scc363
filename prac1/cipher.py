# Include any required modules
from pydoc import plain

def buildTables(rotationNumber):
    # The function should return 2 dictionaries.
    # The dictionaries should keep the mapping of plaintext characters
    # to ciphertext ones and vice versa
    # TODO
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    plainToCipher = {}
    for char in alphabet:
        index = alphabet.index(char) + rotationNumber
        if index > (len(alphabet) - 1):
            offset = index - (len(alphabet))
            plainToCipher[char] = alphabet[offset]
        else:   
            plainToCipher[char] = alphabet[index]
    cipherToPlain = {v: k for k, v in plainToCipher.items()}
    return (plainToCipher, cipherToPlain)

def encrypt(plainText, plainToCipher):
    # The function should encrypt the plaintext using the
    # plainToCipher dictionary built by the function buildTables
    # TODO
    cipher = ""
    for char in plainText:
        if char in plainToCipher:
            cipher = cipher + plainToCipher[char]
        else:
            cipher = cipher + char
    return cipher

def decrypt(cipherText, cipherToPlain):
    # The function should decrypt the cipherText using the
    # cipherToPlain dictionary built by the function buildTables
    # TODO
    text = ""
    for char in cipherText:
        if char in cipherToPlain:
            text = text + cipherToPlain[char]
        else:
            text = text + char
    return text

# Main
if __name__ == "__main__":
    plainToCipher, cipherToPlain = buildTables(10)
    plainString = "hello world!"
    cipher = encrypt(plainString, plainToCipher)
    print(cipher)
    text = decrypt(cipher, cipherToPlain)
    print(text)
# “””
# 1. Create 2 dictionaries using the buildTables function
# using a rotation number, e.g. 10
# 2. Create a string with a plaintext, e.g. “hello world!”
# 3. Encrypt the plaintext and print the ciphertext
# 4. Decrypt the ciphertext and print the plaintext