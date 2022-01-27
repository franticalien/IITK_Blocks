import hashlib 
import binascii

path = input('Enter path of file')

with open(path, "rb") as binary_file:
    data = binary_file.read()
    transaction_id = hashlib.sha256(data).hexdigest()

    print("Transaction ID : " , transaction_id)


with open(path, "rb") as binary_file:
    

    bytes_number_of_inputs = binary_file.read(4)
    number_of_inputs = int.from_bytes(bytes_number_of_inputs, byteorder='big')
    print("Number of Inputs : " , number_of_inputs)

    for x in range(number_of_inputs):

        print("\tInput : " , x+1)

        bytes_transaction_id = binary_file.read(32)
        input_transaction_id = binascii.hexlify(bytes_transaction_id).decode('utf-8')
        print("\t\t transaction id : ", input_transaction_id)



        bytes_index = binary_file.read(4)
        index = int.from_bytes(bytes_index, byteorder='big')
        print("\t\t index : ", index)

        bytes_signature_length = binary_file.read(4)
        signature_length = int.from_bytes(bytes_signature_length, byteorder='big')
        print("\t\t Length of signature : ", signature_length)

        bytes_signature = binary_file.read(signature_length)
        bytes_signature_text = binascii.hexlify(bytes_signature).decode('utf-8')

        print("\t\t Signature : ", bytes_signature_text)

    bytes_number_of_outputs = binary_file.read(4)
    number_of_outputs = int.from_bytes(bytes_number_of_outputs, byteorder='big')
    print("Number of Outputs : " , number_of_outputs)

    for x in range(number_of_outputs):

        print("\t Output : " , x+1)

        bytes_number_of_coins = binary_file.read(8)
        number_of_coins = int.from_bytes(bytes_number_of_coins, byteorder='big')
        print("\t\t Number of coins : ", number_of_coins)

        bytes_public_key_length = binary_file.read(4)
        public_key_length = int.from_bytes(bytes_public_key_length, byteorder='big')
        print("\t\t Length of public key : ", public_key_length)

        bytes_public_key = binary_file.read(public_key_length)
        public_key_text = binascii.hexlify(bytes_public_key).decode('utf-8')

        print("\t\t Public key : ", public_key_text)







    
