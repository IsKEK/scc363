# Required modules 
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import dh 
from cryptography.hazmat.primitives.kdf.hkdf import HKDF 
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_parameters, load_pem_public_key, load_pem_private_key 
from dhCheck import dhCheckCorrectness # You MUST have this included for your submission on Coderunner. You can remove it when you test your code in local system. 

def Diffie_Hellman(): 
    dhParametersString = b'-----BEGIN DH PARAMETERS-----\nMEYCQQDP+dSNnBRy4jbHTvr0YcEk0bMzisMy+p/k9VYCb+gPNU/OSDkmEX62YKTc\nj1QrAo8+f3du/bjdfVKfv71LWtxjAgEC\n-----END DH PARAMETERS-----\n' 
    dhParameters = serialization.load_pem_parameters(dhParametersString)
    peerPublicKeyString = b'-----BEGIN PUBLIC KEY-----\nMIGaMFMGCSqGSIb3DQEDATBGAkEAz/nUjZwUcuI2x0769GHBJNGzM4rDMvqf5PVW\nAm/oDzVPzkg5JhF+tmCk3I9UKwKPPn93bv243X1Sn7+9S1rcYwIBAgNDAAJAYyRw\n2K7KvbqudRx9DQtKH/tAQjDtDMIw7hFWYslMFnE/t44wArXQ/wuo0NPhFL4b63R8\nJZA7cF7tP+CAj3WHFA==\n-----END PUBLIC KEY-----\n' 
    peerPublicKey = serialization.load_pem_public_key(peerPublicKeyString)
    myPrivateKey = dhParameters.generate_private_key() # generate my private and public keys according to dh parameters
    myPublicKey = myPrivateKey.public_key()
    sharedKey = myPrivateKey.exchange(peerPublicKey) # find shared key using my private key and peer public key
    derivedKey = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(sharedKey) # derive key using peer public key and my private key (Y_A)^(X_B) mod q
    myPublicKeyPem = myPublicKey.public_bytes(serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo) # encode my public key to PEM format
    return (myPublicKeyPem, derivedKey)

if __name__ == "__main__":
    publicKey, derivedKey = Diffie_Hellman()
    print(publicKey)
    print(derivedKey)
