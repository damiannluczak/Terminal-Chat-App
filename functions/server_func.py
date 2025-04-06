import json
from datetime import datetime
from config import HEADER, FORMAT, DISCONNECT_MESSAGE

clients = {}
activeUsers = []
room_list = ["lobby",'room1','room2']

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        header = conn.recv(HEADER).decode(FORMAT)
        if not header:
            conn.close()
            return
        username_len = int(header.strip())
        username = conn.recv(username_len).decode(FORMAT)
        clients[conn] = {"username" : username,
                         "room" : "lobby"}
        activeUsers.append(username)
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
                if target_room in room_list:


            if text == DISCONNECT_MESSAGE:
                break
            if text == "/who":
                print("[DEBUG] Otrzymano /who od", username)
                print("[DEBUG] activeUsers:", activeUsers)  # <-- dodaj to tymczasowo
                data_out = {
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "sender": "system",
                    "text": f"Aktywni użytkownicy: {', '.join(activeUsers)}"
                }
                json_out = json.dumps(data_out).encode(FORMAT)
                out_len = len(json_out)
                out_header = str(out_len).encode(FORMAT)
                out_header += b' ' * (HEADER - len(out_header))

                conn.send(out_header)
                conn.send(json_out)
                continue  # <-- ważne! żeby nie leciało dalej

            time_str = datetime.now().strftime("%H:%M:%S")
            data_out = {
                "time": time_str,
                "sender": username,
                "text": text
            }
            json_out = json.dumps(data_out).encode(FORMAT)
            out_len = len(json_out)
            out_header = str(out_len).encode(FORMAT)
            out_header += b' ' * (HEADER - len(out_header))

            for client_sock in list(clients.keys()):
                try:
                    client_sock.send(out_header)
                    client_sock.send(json_out)
                except:
                    client_sock.close()
                    del clients[client_sock]
        except:
            break

    if conn in clients:
        print(f"[DISCONNECT] {clients[conn]} disconnected.")
        if clients[conn] in activeUsers:
            activeUsers.remove(clients[conn])
        del clients[conn]
    conn.close()