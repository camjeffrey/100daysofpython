import string

lowercase_alphabet_list = list(string.ascii_lowercase)
uppercase_alphabet_list = list(string.ascii_uppercase)

def encryption(message, shift):
    unencrypted_message = list(message)
    encrypted_message = ""

    for i in unencrypted_message:
        if i == ' ' or i in string.punctuation or i in string.digits:
            encrypted_message += i
        elif i in lowercase_alphabet_list:
            unencrypted_index = lowercase_alphabet_list.index(i)
            encrypted_index = unencrypted_index + shift
            encrypted_message += lowercase_alphabet_list[encrypted_index % len(lowercase_alphabet_list)]
        elif i in uppercase_alphabet_list:
            unencrypted_index = uppercase_alphabet_list.index(i)
            encrypted_index = unencrypted_index + shift
            encrypted_message += uppercase_alphabet_list[encrypted_index % len(uppercase_alphabet_list)]

    return encrypted_message

def decryption(message, shift):
    encrypted_message = list(message)
    unencrypted_message = ""

    for i in encrypted_message:
        if i == ' ' or i in string.punctuation or i in string.digits:
            unencrypted_message += i
        elif i in lowercase_alphabet_list:
            encrypted_index = lowercase_alphabet_list.index(i)
            unencrypted_index = encrypted_index - shift
            unencrypted_message += lowercase_alphabet_list[unencrypted_index % len(lowercase_alphabet_list)]
        elif i in uppercase_alphabet_list:
            encrypted_index = uppercase_alphabet_list.index(i)
            unencrypted_index = encrypted_index - shift
            unencrypted_message += uppercase_alphabet_list[unencrypted_index % len(uppercase_alphabet_list)]

    return unencrypted_message

print("Caesar Cipher")

while True:
    mode = input("Press '1' to encrypt a message, '2' to decrypt a message, or '3' to exit: ")

    if mode == '1':
        message_to_encrypt = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        encrypted_message = encryption(message_to_encrypt, shift)
        print(f"Encrypted message: {encrypted_message}")

    elif mode == '2':
        message_to_decrypt = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        decrypted_message = decryption(message_to_decrypt, shift)
        print(f"Decrypted message: {decrypted_message}")

    elif mode == '3':
        break

    else:
        print("Invalid selection.")