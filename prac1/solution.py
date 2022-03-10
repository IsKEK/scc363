# Required modules
import string

# Task Caesars algorithm
def buildTables(rotation_number):

    plainToCipher = {}
    cipherToPlain = {}
    sizeOfAlphabet = len(string.ascii_lowercase)

    for i in range(sizeOfAlphabet):

        plainChar = string.ascii_lowercase[i]
        cipherChar= string.ascii_lowercase[(i+rotation_number)%sizeOfAlphabet]

        plainToCipher[plainChar] = cipherChar
        cipherToPlain[cipherChar] = plainChar
    
    return (plainToCipher, cipherToPlain)

# Define an encryption function
# plainText: the text to be encrypted
# plainToCipher: the hashtable that has the plain to cipher mappings
def encrypt(plainText, plainToCipher):
    
    result = ""

    for char in plainText:
        if char in plainToCipher: # deal with numbers etc.
            result += plainToCipher[char]
        else:
            result += char
    
    return result

# Define an encryption function
# cipherText: the text to be decrypted
# cipherToPlain: the hashtable that has the cipher to plain mappings
def decrypt(cipherText, cipherToPlain):
    return encrypt(cipherText, cipherToPlain)



# Extra challenge: cryptogram
import secrets

def buildTablesCryptogram():

    plainToCipher = {}
    cipherToPlain = {}
    visited = set()
    sizeOfAlphabet = len(string.ascii_lowercase)

    for i in range(sizeOfAlphabet):

        plainChar = string.ascii_lowercase[i]
        randomLetterIndex = -1
        while True:
            randomLetterIndex = secrets.randbelow(sizeOfAlphabet)
            if (randomLetterIndex not in visited):
                visited.add(randomLetterIndex)
                break

        cipherChar= string.ascii_lowercase[randomLetterIndex]
        
        plainToCipher[plainChar] = cipherChar
        cipherToPlain[cipherChar] = plainChar
    
    return (plainToCipher, cipherToPlain)


if __name__ == "__main__":

    # Build the dictionaries
    pTable, cTable = buildTables(10)
    
    # Define a plaintext
    pText = "hello world!"
    
    # Encrypt plaintext
    cText = encrypt(pText,pTable)

    print("Ceaser: Ciphertext is: ", cText )
    print("Ceaser: Plaintext is: ", decrypt(cText,cTable) )

    # Testing Extra Challenge
    pTable, cTable = buildTablesCryptogram()
    
    pText = "help me, obi-wan kenobi. you’re my only hope."
    cText = encrypt(pText,pTable)

    print("Cryptogram: Ciphertext is: ", cText )
    print("Cryptogram: Plaintext is: ", decrypt(cText,cTable) )
