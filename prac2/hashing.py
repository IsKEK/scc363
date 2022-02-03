# Include any required modules
import hashlib
import itertools
import string

def HexBinSHA256(stringToConvert):
    # The function should calculate the SHA256 value of stringToConvert
    hash = hashlib.sha256()
    stringInBytes = str.encode(stringToConvert)
    hash.update(stringInBytes)
    hexValue = hash.hexdigest()
    # and convert the hex value to its binary representation
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    binValue = bin(int(hexValue, scale))[2:].zfill(num_of_bits)
    # TODO
    return (hexValue, binValue)

def brute_force(hash):
    letters = itertools.product(string.ascii_lowercase, repeat=5)

    for word in letters:
            password_try = ''.join(word)
            if hashlib.sha256(password_try.encode()).hexdigest() == hash:
                return password_try

# Main
if __name__ == "__main__":
    # while True:
    #     inputString = input()
    #     hexResult, binResult = HexBinSHA256(inputString)
    #     print("Hexadecimal: " + hexResult + "\nBinary: " + binResult)
    #     inputString = ""
    hash = "94f94c9c97bfa92bd267f70e2abd266b069428c282f30ad521d486a069918925"
    password = brute_force(hash)
    print(password)
# “””
# 1. Create a string, e.g. “hello world!”
# 2. Call HexBinSHA256 to calculate its SHA256 value (hex and binary)
# 3. Print the values
# “””