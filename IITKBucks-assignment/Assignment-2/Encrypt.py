from cryptography.fernet import Fernet
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from Crypto.Cipher import PKCS1_OAEP

input_text1 = input("Enter text ")
print(input_text1)

private_key = input("Enter path to private key")

key = RSA.import_key(open(private_key).read())
encryptor = PKCS1_OAEP.new(key)

encrypted = encryptor.encrypt(input_text1.encode())

print(encrypted)
