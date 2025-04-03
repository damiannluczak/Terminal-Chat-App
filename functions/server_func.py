from config import HEADER, FORMAT, DISCONNECT_MESSAGE

# Todo  wykrycie timeout


clients = {}  # conn : ussername


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    # odbieranie nazwy użytkownika
    username_length = conn.recv(HEADER).decode(FORMAT)
    if username_length:
        username_length = int(username_length)
        username = conn.recv(username_length).decode(FORMAT)
        clients[conn] = username

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # obsługa  /list
            if msg == "/list":
                user_list = "\n".join(clients.values())
                conn.send(f" Online users:\n{user_list}".encode(FORMAT))
                continue

            # obsługa dc
            if msg == DISCONNECT_MESSAGE:
                connected = False
                break
            if msg.startswith("/"):
                continue

            print(f"[{username}] {msg}")

            # rozsylanie
            for client in clients:
                if client != conn:
                    try:
                        client.send(f"[{username}]: {msg}".encode(FORMAT))
                    except:
                        client.close()
                        del clients[client]

    conn.close()
    if conn in clients:
        del clients[conn]
