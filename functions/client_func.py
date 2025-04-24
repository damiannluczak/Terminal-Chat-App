import json
from datetime import datetime
from config import HEADER, FORMAT, COLOR_RESET, COLOR_RED, COLOR_GREEN, COLOR_BLUE


def display_message(data):
    time_str = data.get("time", "")
    sender = data.get("sender", "")
    text = data.get("text", "")
    print(f"{COLOR_BLUE}[{time_str}]{COLOR_RESET} {COLOR_GREEN}[{sender}]{COLOR_RESET}: {COLOR_RED}{text}{COLOR_RESET}")


def receive(client_socket):
    while True:
        try:
            header = client_socket.recv(HEADER).decode(FORMAT)
            if not header:
                break
            msg_length = int(header.strip())
            raw_data = client_socket.recv(msg_length).decode(FORMAT)

            data = json.loads(raw_data)
            display_message(data)
        except Exception as e:
            import traceback
            traceback.print_exc()  # pokaże dokładnie, gdzie i dlaczego wywala
            print("[ERROR] podczas odbierania wiadomości:", e)
            break


def send(msg, client_socket, username):
    data = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "sender": username,
        "text": msg
    }
    encoded = json.dumps(data).encode(FORMAT)
    length = len(encoded)
    header = str(length).encode(FORMAT)
    header += b' ' * (HEADER - len(header))

    try:
        client_socket.send(header)
        client_socket.send(encoded)
    except:
        pass
