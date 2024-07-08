import socket

# IP of server
# if server has IP public, use it
HOST = "192.168.55.63"
PORT = 4545

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello Server".encode('ascii'))
print(socket.recv(1024).decode('ascii'))