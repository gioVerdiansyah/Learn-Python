import socket
import threading

HOST = "192.168.55.63"
PORT = 4545

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.bind((HOST, PORT))

clients = set()


def handle_client():
    while True:
        msg, addr = server.recvfrom(1024)
        client_ip = f"{addr[0]}:{addr[1]}"
        if addr not in clients:
            clients.add(addr)
            print(f"[NEW CONNECTION] from {client_ip}")
        msg_decoded = msg.decode('utf-8')
        print(f"[{client_ip}]: {msg_decoded}")
        if msg_decoded.lower() == "exit":
            clients.remove(addr)
            print(f"[{client_ip}] has disconnected.")
            continue
        for client in clients:
            if client != addr:
                server.sendto(f"{msg_decoded}".encode('utf-8'), client)


print(f"[ACTIVE] server has started on {HOST}:{PORT}")

handle_thread = threading.Thread(target=handle_client)
handle_thread.start()
