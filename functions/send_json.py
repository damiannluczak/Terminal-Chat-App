from config import FORMAT, HEADER
import json


def send_json(conn, data_out, format=FORMAT, header=HEADER):
    try:
        json_out = json.dumps(data_out).encode(format)
        out_len = len(json_out)
        out_header = str(out_len).encode(format)
        out_header += b' ' * (header - len(out_header))

        conn.send(out_header)
        conn.send(json_out)
    except Exception as e:
        print("[ERROR] Błąd w send_json:", e)
