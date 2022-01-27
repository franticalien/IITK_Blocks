import hashlib 

output_bytes = bytearray()

number_of_inputs = int(input("Please enter number of inputs"))
bytes_number_of_inputs = number_of_inputs.to_bytes(4,byteorder='big', signed=True)
output_bytes.extend(bytes_number_of_inputs)


for x in range(number_of_inputs):
    transaction_id = int(input("enter transaction ID"),16)
    bytes_transaction_id = transaction_id.to_bytes(32,byteorder='big')
    output_bytes.extend(bytes_transaction_id)

    #print(transaction_id)
    index = int(input("enter index"))
    bytes_index = index.to_bytes(4,byteorder='big')
    output_bytes.extend(bytes_index)

    



    signature = input("enter signature")
    bytes_signature = bytearray.fromhex(signature)

    

    

    signature_length = len(bytes_signature)
    bytes_signature_length = signature_length.to_bytes(4,byteorder = 'big')
    output_bytes.extend(bytes_signature_length)

    output_bytes.extend(bytes_signature)

number_of_outputs = int(input("Please enter number of outputs"))
bytes_number_of_outputs = number_of_outputs.to_bytes(4,byteorder='big')
output_bytes.extend(bytes_number_of_outputs)

for x in range(number_of_outputs):
    number_of_coins = int(input("Enter number of coins"))
    bytes_number_of_coins = number_of_coins.to_bytes(8,byteorder='big')
    output_bytes.extend(bytes_number_of_coins)
    
    path = input("Enter path to public key")
    with open(path, "rb") as binary_file:
        bytes_public_key = binary_file.read()

        public_key_length = len(bytes_public_key)
        bytes_public_key_length = public_key_length.to_bytes(4,byteorder='big')
        output_bytes.extend(bytes_public_key_length)
        output_bytes.extend(bytes_public_key)   

result_hash = hashlib.sha256(output_bytes)

print(result_hash.hexdigest())
result_hash_hex = result_hash.hexdigest()
file_name =result_hash_hex+".dat"

with open(file_name, "wb") as binary_file:
    # Write text or bytes to the file
    binary_file.write(output_bytes)
        
    


