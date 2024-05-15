from cryptography.fernet import Fernet

# Make sure the length of the key
key = Fernet.generate_key()

chiper_suit = Fernet(key)
message = input("Write your message: ")
encrypt_message = chiper_suit.encrypt(message.encode())

with open("resources/message.txt", "wb") as file:
    file.write(encrypt_message)
    file.write(key)