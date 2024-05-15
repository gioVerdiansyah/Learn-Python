from cryptography.fernet import Fernet

with open("resources/message.txt", "rb") as file:
    encrypt_message = file.read()

# Make sure length of the key is same in Encrypt
key = encrypt_message[-44:]
encrypt_message = encrypt_message[:-44]

chiper_suite = Fernet(key)

open_message_encrypt = chiper_suite.decrypt(encrypt_message).decode('utf-8')

print(open_message_encrypt)