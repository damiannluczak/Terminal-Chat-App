import socket
import threading

from functions.client_func import receive, send
from config import ADDR, DISCONNECT_MESSAGE,HEADER,FORMAT

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


username = input("Enter Your Username -")

username_encoded = username.encode(FORMAT)
username_length = str(len(username_encoded)).encode(FORMAT)
username_length += b' ' * (HEADER - len(username_length))
client.send(username_length)
client.send(username_encoded)

receive_thread = threading.Thread(target=receive, args=(client, username))
receive_thread.start()

while True:
    msg = input(f"[{username}] -> ").lstrip()

    if msg == "/help":
        print("Dostępne komendy:\n/help\n/list\n!DISCONNECT")
        continue

    if msg == "/list":
        send("/list", client)
        continue

    if msg == DISCONNECT_MESSAGE:
        send(msg, client)
        break

    send(msg, client)
