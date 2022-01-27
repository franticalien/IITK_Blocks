import time
import hashlib

output_bytes = bytearray()




index = int(input("Please enter index"))
bytes_index = index.to_bytes(4,byteorder='big')
output_bytes.extend(bytes_index)

parent_hash = input("Please enter hash of parent block")
bytes_parent_hash = bytearray.fromhex(parent_hash)
output_bytes.extend(bytes_index)





path_block_body = input("Block body")
body_hash = 1
bytes_block_body = 1
with open(path_block_body, "rb") as binary:
    bytes_block_body = binary.read()
    
    body_hash = hashlib.sha256(bytes_block_body).hexdigest()
    bytes_body_hash = bytearray.fromhex(body_hash)
    
    output_bytes.extend(bytes_body_hash)

target = int(input("Target"),16)
bytes_target = target.to_bytes(32,byteorder='big')
output_bytes.extend(bytes_target)
i = 1
start_time = int(time.time()*1000000000)

tempbytes = output_bytes
while True:
    
    time1 = int(time.time()*1000000000)
    bytes_timestamp = time1.to_bytes(8,byteorder = 'big')
    bytes_i = i.to_bytes(8,byteorder = 'big')
    tempbytes.extend(bytes_timestamp)
    tempbytes.extend(bytes_i)
    header_hash = int(hashlib.sha256(tempbytes).hexdigest(),16)
    
    if(header_hash<target):
        print("Nonce value")
        print(i)
        print("Time stamp for this nonce value")
        print(time1)
        print("SHA256 hash of block header")
        print(header_hash)
        print("time difference is ")
        print(int((time1 - start_time)/1000000000))
        break

    

    
    

    i+=1

