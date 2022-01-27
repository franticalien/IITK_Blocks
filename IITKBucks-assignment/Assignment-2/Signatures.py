from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from Crypto.Cipher import PKCS1_OAEP


PublicKey = input("enter path to key")
unencrypted = input("enter unencrypted text")
encrypted = input("enter encrypted text")

file = open(PublicKey, 'rb')
key = file.read()
file.close()

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(encrypted.encode())

if(unencrypted==decrypted):
    print("Signature verified")
else :
    print ("verification failed")
