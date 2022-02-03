# Include any required modules
import hashlib
import itertools

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
    letters = [chr(n) for n in range(ord('a'), ord('z'))]
    digits = [chr(n) for n in range(ord('0'), ord('9'))]

    for part1 in itertools.product(letters, repeat=3):
        for part2 in itertools.product(digits, repeat=4):
            password_try = ''.join(part1 + part2)
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
    print(brute_force(hash))
# “””
# 1. Create a string, e.g. “hello world!”
# 2. Call HexBinSHA256 to calculate its SHA256 value (hex and binary)
# 3. Print the values
# “””