import sys
import os
from functions.client_func import send


def help_command():
    print("[system]: Dostepne Komendy: /help, /quit, /who")

def quit_command():
    print("[system]: Rozlaczono")

def who_command(client_socket,username):
    send("/who", client_socket, username)

def join_command(client_socket,username):
    send("/join",client_socket,username)


COMMANDS = {
    "/help" : help_command,
    "/quit" : quit_command,
    "/who" : who_command,
}




