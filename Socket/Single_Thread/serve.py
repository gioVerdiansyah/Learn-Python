import socket

# Auto get IPv4 address
# host = socket.gethostbyname(socket.gethostname())

# Manual
HOST = "192.168.55.63" # check ipconfig in win terminal
PORT = 4545

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# try INET6 for IPv6
# SOCK_STREAM is TCP
# SOCK_DGRAM is UDP

server.bind((HOST, PORT))

server.listen(3)
# 3 means if the server is still processing 3 requests, and if there is another request, it will be rejected.

while True:
    communication_socket, address = server.accept()
    # The server will be waiting for requests. If there are no requests, the server will wait until there is a request.
    # If there is a request, accept() will be triggered and the client's address will be returned.
    # communication_socket is a variable we use to interact with the client.

    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('ascii')
    # number is limited bytes we received
    # we must decode, because client message send is encode (bytes)

    print(f"Message from client is: {message}")
    communication_socket.send(f"Thank you for your message!".encode('ascii'))
    communication_socket.close()

    print(f"Connection with address: {address} ended!")
