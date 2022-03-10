# Required imports 
import string 

def buildTable(a, b):

    cipherTable = {}
    sizeOfAlphabet = len(string.ascii_uppercase)
    
    for i in range(sizeOfAlphabet):
        plainChar = string.ascii_uppercase[i] 
        cipherChar= string.ascii_uppercase[(a*i+b)%sizeOfAlphabet] # apply the affine cipher formula to map each letter in the alphabet

        cipherTable[plainChar] = cipherChar
    
    return cipherTable

def encryptAffine(plainText, a, b): 
    cipherTable = buildTable(a, b)
    cipherText = ""
    for char in plainText:
        if char in cipherTable:  
            cipherText += cipherTable[char] # switch characters that are in the table to its' mapped values
        else:
            cipherText += char  # leave characters that are not in the table unchanged
    return cipherText

if __name__ == "__main__":
    print(encryptAffine("HELLO WORLD", 1, 1))