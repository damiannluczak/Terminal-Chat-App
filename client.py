import socket
import threading
import sys
from config import ADDR, FORMAT, DISCONNECT_MESSAGE
from functions import command
from functions.client_func import receive, send

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    username = input("Enter Your Username - ")

    user_enc = username.encode(FORMAT)
    user_len = str(len(user_enc)).encode(FORMAT)
    user_len += b' ' * (64 - len(user_len))
    client_socket.send(user_len)
    client_socket.send(user_enc)

    recv_thread = threading.Thread(target=receive, args=(client_socket,))
    recv_thread.start()

    while True:
        msg = input()

        # Usuwamy wpisaną linię z terminala (hack ANSI),
        # dzięki czemu nie pojawia się „podwójny” wpis.
        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

        # Sprawdzamy, czy to komenda rozłączenia
        if msg == "/quit":
            send(DISCONNECT_MESSAGE, client_socket, username)
            break
        if msg.startswith("/"):
            if msg in command.COMMANDS:
                command.COMMANDS[msg](client_socket, username)
            else:
                print("[system]: Komenda nie rozpoznana")




        else:
            send(msg, client_socket, username)

    client_socket.close()

if __name__ == "__main__":
    main()