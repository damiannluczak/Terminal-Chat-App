import socket
import threading


HEADER = 64

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = "127.0.0.1"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

username = input("Enter Your Username")


def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            if msg.startswith(f"[{username}]"):
                print(f"\r🟢 {msg}\n> ", end="")
            else:
                print(f"\r{msg}\n> ", end="")
        except:
            print("ERROR Connection closed or lost.")
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()


def send(msg):
    msg = msg.strip()

    if msg.startswith("/"):
        message = msg.encode(FORMAT)
    else:
        message = msg.encode(FORMAT)

    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)


while True:
    msg = input("> ")

    if msg == "/help":
        print("Dostępne komendy:\n/help\n/list\n!DISCONNECT")
        continue

    if msg == "/list":
        send("/list")
        continue

    if msg == DISCONNECT_MESSAGE:
        send(msg)
        break

    send(msg)
