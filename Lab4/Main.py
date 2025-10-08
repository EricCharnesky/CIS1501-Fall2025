def encrypt(message, stride):
    jumbled_message = ""
    for starting_index in range(stride):
        jumbled_message += message[starting_index::stride]

    encrypted_message = ""
    for index in range(len(jumbled_message)):
        encrypted_message += chr(ord(jumbled_message[index]) + index)

    return encrypted_message

def decrypt(encrypted_message, stride):
    jumbled_message = ""
    for index in range(len(encrypted_message)):
        jumbled_message += chr(ord(encrypted_message[index]) - index)

    message = ""
    chunk_lengths = []
    for chunk_number in range(stride):
        chunk_length = len(jumbled_message) // stride
        if len(jumbled_message) % stride > chunk_number:
            chunk_lengths.append(chunk_length + 1)
        else:
            chunk_lengths.append(chunk_length)

    for character_index in range(chunk_lengths[-1]):
        for chunk_index in range(stride):
            message += jumbled_message[sum(chunk_lengths[0:chunk_index]) + character_index]

    for index, chunk_length in enumerate(chunk_lengths):
        character_index = 0
        if chunk_length != chunk_lengths[-1]:
            character_index += chunk_lengths[index] - 1
            message += jumbled_message[character_index]

    return message


encrypted_message = encrypt("Happy Monday!!!!", 3)

print(encrypted_message)
decrypted_message = decrypt(encrypted_message, 3)
print(decrypted_message)