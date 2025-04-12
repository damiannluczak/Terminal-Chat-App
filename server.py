import socket
import threading
from datetime import datetime

from config import SERVER, ADDR

from functions.server_func import handle_client

# creasting a socket INTET ==  ipv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count()}")


print("[START] server is starting")
start()
