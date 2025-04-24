import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"  # ja
COLOR_RED = "\033[91m"  # Inni użytkownicy
COLOR_BLUE = "\033[94m"  # Godzina
