import socket
import threading
import sys
from config import ADDR, FORMAT, DISCONNECT_MESSAGE
from functions import command
from functions.client_func import receive, send

# localroom list TODO -query server/db about current room list
roomslist = ["lobby", "room1", "room2"]


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    username = input("Enter Your Username - ")
    user_enc = username.encode(FORMAT)
    user_len = str(len(user_enc)).encode(FORMAT)
    user_len += b' ' * (64 - len(user_len))
    client_socket.send(user_len)
    client_socket.send(user_enc)

    choose_chat_room(username, client_socket)

    recv_thread = threading.Thread(target=receive, args=(client_socket,))
    recv_thread.start()

    while True:
        msg = input()

        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

        if msg.startswith("/"):
            if msg in command.COMMANDS:
                command.COMMANDS[msg](client_socket, username)
                if msg == "/leave":
                    choose_chat_room(username, client_socket)
            else:
                print("[system]: Komenda nie rozpoznana")
        else:
            send(msg, client_socket, username)

    client_socket.close()


def choose_chat_room(username, client_socket):
    print("Choose the room that you want to join")
    for num, room in enumerate(roomslist, start=1):
        print(f"{num} : {room}")
    try:
        choice = int(input())
    except ValueError:
        print("Type in an Integer!")
        return choose_chat_room(username, client_socket)
    match choice:
        case 1:
            room = "lobby"
            send("/join lobby", client_socket, username)
        case 2:
            room = "room1"
            send("/join room1", client_socket, username)
        case 3:
            room = "room2"
            send("/join room2", client_socket, username)
        case _:
            print(f"Room doesnt exists. Choose room from the list")
            return choose_chat_room(username, client_socket)


if __name__ == "__main__":
    main()
