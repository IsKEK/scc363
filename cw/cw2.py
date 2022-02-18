# Required modules 
import hashlib 

def avalancheCalculator(string1, string2): 
    string1Hex = hashlib.sha256(string1.encode()).hexdigest()
    string2Hex = hashlib.sha256(string2.encode()).hexdigest() # apply sha256 hashing to both strings
    string1Bin = bin(int(string1Hex, 16))[2:] # convert to binary to find the number of bits that are different between hashed values
    string2Bin = bin(int(string2Hex, 16))[2:] # remove prefix 0b from the strings 
    # add zeros to the start of strings' binary values so they are 256 bits long. They should be 256 bits long because we are using sha256 hash function which outputs 256 bit values. bin() function removes zeros from the start as they don't add any value.
    if len(string1Bin) < 256:
        while len(string1Bin) < 256:
            string1Bin = "0" + string1Bin
    if len(string2Bin) < 256:
            while len(string2Bin) < 256:
                string2Bin = "0" + string2Bin
    avalanceNumber = 0
    # use range(256) because above code makes sure that both values are 256 bits long.
    for i in range(256):
        if string1Bin[i] != string2Bin[i]: # if bits are different, increment avalanche number
            avalanceNumber += 1
    return avalanceNumber

if __name__ == "__main__":
    print(avalancheCalculator("Hello World1", "Hello World2"))