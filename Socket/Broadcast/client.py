import socket
import threading
import sys

HOST = "192.168.55.63"
PORT = 4545

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(('', 0))  # Bind to a random available port

server_address = (HOST, PORT)

def receive():
    while True:
        try:
            msg, _ = client.recvfrom(1024)
            print(f"\r\nsomeone: {msg.decode('utf-8')}\n> ", end='')
            sys.stdout.flush()
        except:
            break

# Start the thread to receive messages
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

def send(message):
    msg = message.encode('utf-8')
    client.sendto(msg, server_address)


send("has connected.")


while True:
    val = input("> ")
    send(val)
    if val.lower() == 'exit':
        break

client.close()
