import socket
import threading
from pickle import FRAME

from server import HEADER, SERVER, FORMAT

HEADER = 64

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR  =(SERVER,PORT)

FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)