import socket
import threading
import receive

#seting header to 64 b
HEADER = 64
#specyfing port i ip
PORT =5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = "127.0.0.1"

ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

username = input("Enter Your Username")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            print(msg)
        except:
            print("ERROR Connection closed or lost.")
            break

def send(msg):
    message = f"[{username}]: {msg}".encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)

    send_length +=b' ' * (HEADER- len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    msg = input()
    if msg == DISCONNECT_MESSAGE:
        send(msg)
        break
    send(msg)
