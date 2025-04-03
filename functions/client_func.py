

from config import FORMAT, HEADER


def receive(client_socket, username):
    while True:
        try:
            msg = client_socket.recv(2048).decode(FORMAT)
            if msg.startswith(f"[{username}]"):
                print(f"\r{msg}\n[{username}] -> ",end="")
            elif msg.startswith("Online users:"):
                print(f"\r{msg}\n[{username}] -> ", end="")
            else:
                print(f"\r{msg}\n[{username}] -> ", end="")
        except:
            print("ERROR Connection closed or lost.")
            break

def send(msg, client_socket):
    msg = msg.strip()

    if msg.startswith("/"):
        message = msg.encode(FORMAT)
    else:
        message = msg.encode(FORMAT)

    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client_socket.send(send_length)
    client_socket.send(message)
