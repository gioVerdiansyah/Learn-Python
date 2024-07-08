import socket
import threading

HOST = "192.168.55.63"
PORT = 4545

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def handle_client(comm, addr):
    client_ip = f"{addr[0]}:{addr[1]}"
    print(f"[NEW CONNECTION] from {client_ip}")

    while True:
        msg_len = comm.recv(1024).decode('ascii')
        if msg_len:
            msg_len = int(msg_len)
            msg = comm.recv(msg_len).decode('ascii')
            if msg.lower() == "exit":
                print(f"[{client_ip}] has disconnected.")
                comm.send("See you later...".encode('ascii'))
                break
            print(f"[{client_ip}] message is: {msg}")
            comm.send(f"Your message is: {msg}".encode('ascii'))
    comm.close()


def handle_start():
    server.listen()
    print(f"[LISTENING] on {HOST}:{PORT}")
    while True:
        communication_sock, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(communication_sock, address))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


print("[START] Server has ben started.")
handle_start()