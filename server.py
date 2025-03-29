import socket
import threading

# seting header to 64 b
HEADER = 64

# specyfing port i ip
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# creasting a socket INTET == using ipv4   stream - we will stream data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(msg)
            for client in clients:
                if client != conn:
                    try:
                        client.send(msg.encode(FORMAT))
                    except:
                        client.close()
                        clients.remove(client)
    conn.close()
    if conn in clients:
        clients.remove(conn)


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount()}")


print("[START] server is starting")
start()
