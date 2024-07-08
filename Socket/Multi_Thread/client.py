import socket

HOST = "192.168.55.63"
PORT = 4545

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def send(message):
    msg = message.encode('ascii')
    send_length = str(len(msg)).encode('ascii')
    send_length += b" " * (1024 - len(send_length))
    client.send(send_length)
    client.send(msg)
    recv_msg = client.recv(1024)
    print(recv_msg.decode('ascii'))


while True:
    val = input("Type to sent: ")
    send(val)
    if val.lower() == 'exit':
        break
