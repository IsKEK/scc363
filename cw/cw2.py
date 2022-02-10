# Required modules 
import hashlib 

def avalancheCalculator(string1, string2): 
    string1Hex = hashlib.sha256(string1.encode()).hexdigest()
    string2Hex = hashlib.sha256(string2.encode()).hexdigest()
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    string1Bin = bin(int(string1Hex, scale))[2:].zfill(num_of_bits)
    string2Bin = bin(int(string2Hex, scale))[2:].zfill(num_of_bits)
    # string1Bin = bin(int(string1Hex, 16))
    # string2Bin = bin(int(string2Hex, 16))
    if len(string1Bin) < 256:
        while len(string1Bin) < 256:
            string1Bin = "0" + string1Bin
    if len(string2Bin) < 256:
            while len(string2Bin) < 256:
                string2Bin = "0" + string2Bin
    avalanceNumber = 0
    # for char in string1Bin:
    #     if (char != string2Bin[string1Bin.index(char)]):
    #         avalanceNumber += 1
    for i in range(256):
        if string1Bin[i] != string2Bin[i]:
            avalanceNumber += 1
    return avalanceNumber

if __name__ == "__main__":
    print(avalancheCalculator("Hello World1", "Hello World2"))