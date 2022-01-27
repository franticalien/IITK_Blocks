from Crypto.PublicKey import RSA 

bits = 2048
new_key = RSA.generate(bits, e=65537) 
public_key = new_key.publickey().exportKey("PEM") 
private_key = new_key.exportKey("PEM") 

f = open('private.pem','wb')
f.write(private_key)
f.close()
f = open('public.pub','wb')
f.write(public_key)
f.close()

