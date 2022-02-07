# Required imports 
import string 

def buildTable(a, b):

    cipherTable = {}
    sizeOfAlphabet = len(string.ascii_uppercase)

    for i in range(sizeOfAlphabet):

        plainChar = string.ascii_uppercase[i]
        cipherChar= string.ascii_uppercase[(a*i+b)%sizeOfAlphabet]

        cipherTable[plainChar] = cipherChar
    
    return cipherTable

def encryptAffine(plainText, a, b): 
    cipherTable = buildTable(a, b)
    cipherText = ""
    for char in plainText:
        if char in cipherTable:
            cipherText += cipherTable[char]
        else:
            cipherText += char
    return cipherText

if __name__ == "__main__":
    print(encryptAffine("HELLO WORLD", 1, 1))