import sys
import os
import json
from datetime import datetime
from graphlib import TopologicalSorter
from functions.client_func import send
from config import HEADER, FORMAT
from functions.send_json import send_json


def help_command(client_socket, username):
    send("/help", client_socket, username)


def quit_command():
    print("[SYSTEM]: Rozlaczono")


def join_command(client_socket, username):
    send("/join", client_socket, username)


def leave_command(client_socket, username):
    send("/leave", client_socket, username)


def who_command(client_socket, username):
    send("/who", client_socket, username)


COMMANDS = {
    "/help": help_command,
    "/quit": quit_command,
    "/who": who_command,
    "/join": join_command,
    "/leave": leave_command
}


# ---------- SERVER COMMANDS ----------
def server_who_command(conn, username, clients):
    try:
        if conn not in clients:
            print("[ERROR] Client not found in 'clients' dictionary")
            return

        current_room = clients[conn]["room"]

        users_in_room = [
            data["username"]
            for data in clients.values()
            if data["room"] == current_room
        ]

        print(f"[DEBUG] /who: users in room {current_room}:", users_in_room)

        data_out = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "sender": "SYSTEM",
            "text": f"Users in room [{current_room}]: {', '.join(users_in_room)}"
        }

        send_json(conn, data_out)

    except Exception as e:
        print("[ERROR] server_who_command failed:", e)


def server_leave_command(conn, username, clients):
    try:
        current_room = clients[conn]["room"]

        for sock, data in clients.items():
            if sock != conn and data["room"] == current_room:
                broadcast_msg = {
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "sender": "SYSTEM",
                    "text": f"{username} has left the room {current_room}"
                }
                send_json(sock, broadcast_msg)

        clients[conn]["room"] = None

        data_out = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "sender": "SYSTEM",
            "text": f"You left the room {current_room}"
        }
        send_json(conn, data_out)

        print(f"[LEAVE] {username} left room {current_room}")

    except Exception as e:
        print("[ERROR] server_leave_command failed:", e)


def server_join_command(conn, username, target_room, room_list, clients):
    if target_room in room_list:
        clients[conn]["room"] = target_room

        for sock, data in clients.items():
            if sock != conn and data["room"] == target_room:
                broadcast_msg = {
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "sender": "SYSTEM",
                    "text": f"{username} has joined the room {target_room}"
                }
                send_json(sock, broadcast_msg)

        print(f"[JOIN] {username} joined {target_room}")
        data_out = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "sender": "SYSTEM",
            "text": f"You joined {target_room}"
        }
        send_json(conn, data_out)
    else:
        print(f"[WARNING] Invalid room name: {target_room}")
