import json
from datetime import datetime
from config import HEADER, FORMAT, DISCONNECT_MESSAGE
from functions.command import server_who_command, server_join_command
from functions.send_json import send_json
from functions.command import server_leave_command

clients = {}

room_list = ["lobby", 'room1', 'room2']


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        header = conn.recv(HEADER).decode(FORMAT)
        if not header:
            conn.close()
            return
        username_len = int(header.strip())
        username = conn.recv(username_len).decode(FORMAT)
        clients[conn] = {"username": username,
                         "room": "lobby"}

        print(f"[USERNAME] {username} connected from {addr}")
    except:
        conn.close()
        return

    while True:
        try:
            msg_header = conn.recv(HEADER).decode(FORMAT)
            if not msg_header:
                break
            msg_length = int(msg_header.strip())
            raw_msg = conn.recv(msg_length).decode(FORMAT)
            data_in = json.loads(raw_msg)
            text = data_in.get("text", "")

            if text.startswith("/join"):
                target_room = text.split(" ", 1)[1].strip()
                server_join_command(conn, username, target_room, room_list, clients)
                continue
            if text == DISCONNECT_MESSAGE:
                break
            if text == "/who":
                print("[DEBUG] Otrzymano /who od", username)
                print("[DEBUG] users in clients:", [c["username"] for c in clients.values()])
                server_who_command(conn, username, clients)
                continue
            if text == "/leave":
                print("[DEBUG] Otrzymano /leave od", username)
                server_leave_command(conn, username, clients)
                continue

            time_str = datetime.now().strftime("%H:%M:%S")
            data_out = {
                "time": time_str,
                "sender": username,
                "text": text
            }
            for client_sock in list(clients.keys()):
                if clients[client_sock]["room"] != clients[conn]["room"]:
                    continue
                try:
                    send_json(client_sock, data_out)
                except:
                    client_sock.close()
                    del clients[client_sock]
        except:
            break

    if conn in clients:
        username = clients[conn]["username"]
        print(f"[DISCONNECT] {username} disconnected.")
        del clients[conn]

    conn.close()
