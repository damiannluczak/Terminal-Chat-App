# 💬 Terminal Chat App (Python TCP)

A simple terminal-based chat application built with **Python sockets** and **threading**, allowing multiple users to chat in real-time. Designed to learn and showcase skills in network programming, concurrency, and client-server architecture.

---

## 🚀 Features

- Multi-client support using `threading`
- Real-time messaging over TCP
- Username handling and message formatting
- Server-side message broadcasting
- Graceful disconnect handling (`!DISCONNECT`)
- Terminal-only interface (CLI)
- Clean, modular architecture

---

## Project Structure

Cli-Chat/
├── server.py       # Multi-client TCP server
├── client.py       # Interactive client with sending/receiving
├── README.md       # Project documentation

---

## Commits History

### Commit #1 – "Initial Working Connection"
- Created `server.py` and `client.py`
- Established TCP connection with `socket`
- Sent messages from client to server

### Commit #2 – "Broadcasting and Receive Thread"
- Added `username` handling on client side
- Implemented **multi-client support** using `threading` in server
- Created server-side **message broadcasting** to all clients
- Implemented **receive thread** on client side to handle incoming messages live
- Added graceful disconnect with `!DISCONNECT`
- Cleaned up and improved logging

## TODO – Upcoming Features

- [ ] Implement commands: `/help`, `/list`, `/quit`
- [ ] Add channels/groups: individual chat rooms or topics
- [ ] Build structured CLI UI with navigation levels
  - login → choose channel → enter chat
- [ ] Save message logs to a file on the server
- [ ] Add SSL/TLS encryption for secure communication



##  How to Run

### Start the Server
```bash
python server.py

