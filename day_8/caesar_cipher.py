import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)

# def encryption(message, shift):
#     unencrypted_message = list(message)
#     encrypted_message = ""
# 
#     for i in unencrypted_message:
#         if i == ' ' or i in string.punctuation or i in string.digits:
#             encrypted_message += i
#         elif i in lowercase_alphabet_list:
#             unencrypted_index = lowercase_alphabet_list.index(i)
#             encrypted_index = unencrypted_index + shift
#             encrypted_message += lowercase_alphabet_list[encrypted_index % len(lowercase_alphabet_list)]
#         elif i in uppercase_alphabet_list:
#             unencrypted_index = uppercase_alphabet_list.index(i)
#             encrypted_index = unencrypted_index + shift
#             encrypted_message += uppercase_alphabet_list[encrypted_index % len(uppercase_alphabet_list)]
# 
#     return encrypted_message
# 
# def decryption(message, shift):
#     encrypted_message = list(message)
#     unencrypted_message = ""
# 
#     for i in encrypted_message:
#         if i == ' ' or i in string.punctuation or i in string.digits:
#             unencrypted_message += i
#         elif i in lowercase_alphabet_list:
#             encrypted_index = lowercase_alphabet_list.index(i)
#             unencrypted_index = encrypted_index - shift
#             unencrypted_message += lowercase_alphabet_list[unencrypted_index % len(lowercase_alphabet_list)]
#         elif i in uppercase_alphabet_list:
#             encrypted_index = uppercase_alphabet_list.index(i)
#             unencrypted_index = encrypted_index - shift
#             unencrypted_message += uppercase_alphabet_list[unencrypted_index % len(uppercase_alphabet_list)]
# 
#     return unencrypted_message

def caesar_cipher(text, shift, encrypt = True):
    cipher = ""
    message = list(text)
    if not encrypt:
        shift = -shift
    for i in message:
        if i == ' ' or i in string.punctuation or i in string.digits:
             cipher += i
        elif i in lowercase_alphabet:
            original_index = lowercase_alphabet.index(i)
            new_index = original_index + shift
            cipher += lowercase_alphabet[new_index % len(lowercase_alphabet)]
        elif i in uppercase_alphabet:
            original_index = uppercase_alphabet.index(i)
            new_index = original_index + shift
            cipher += uppercase_alphabet[new_index % len(uppercase_alphabet)]
    return cipher

def encrypt(text, shift):
    return caesar_cipher(text, shift, encrypt = True)

def decrypt(text, shift):
    return caesar_cipher(text, shift, encrypt = False)



print("Caesar Cipher")

while True:
    mode = input("Press '1' to encrypt a message, '2' to decrypt a message, or '3' to exit: ")

    if mode == '1':
        message_to_encrypt = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        encrypted_message = encrypt(message_to_encrypt, shift)
        print(f"Encrypted message: {encrypted_message}")

    elif mode == '2':
        message_to_decrypt = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        decrypted_message = decrypt(message_to_decrypt, shift)
        print(f"Decrypted message: {decrypted_message}")

    elif mode == '3':
        break

    else:
        print("Invalid selection.")