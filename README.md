# Terminal Chat App (Python TCP)

A simple terminal-based chat application built with **Python sockets** and **threading**, allowing multiple users to chat in real-time. Designed to learn and showcase skills in network programming, concurrency, and client-server architecture.

---

## Features

- Multi-client support using `threading`
- Real-time messaging over TCP
- Username handling and message formatting
- Server-side message broadcasting
- Terminal-only interface (CLI)
- Clean, modular architecture

---

## Project Structure

Cli-Chat/

├── client.py                 # Client entry point (connects, sends, receives)          
├── server.py                 # Server entry point (accepts clients, manages threads)      
├── config.py                 # Shared constants (IP, port, format, header)
├── README.md                 # documentation        
├── functions/      
│  ├── client_func.py        # Client logic (send, receive functions)
│  └── server_func.py        # Server logic (handle_client function)

---


## Commits History

### Commit #1 – "Initial Working Connection"
- Created `server.py` and `client.py`
- Established basic TCP connection
- Enabled single-message sending from client to server

### Commit #2 – "Broadcasting and Receive Thread"
- Implemented **multi-client support** using `threading`
- Added `username` input and tagging messages with it
- Server now broadcasts incoming messages to all clients
- Added live **receive thread** on client side
- Introduced `!DISCONNECT` command

### Commit #3 – "Basic Commands"
- Added `/help` – prints available commands
- Added `/list` – shows online users on request

### Commit #4 – "Bug Fixes and Cleanup"
- Extracted reusable logic into `functions/`
- Improved terminal formatting and UX
- Made code restart-safe and modular

###  Commit #5 – "Switch to JSON Msg Format + Timestamp"
- Migrated message format to **JSON**
  - Includes `time`, `sender`, and `text` fields
- Messages are now parsed and formatted consistently
- Timestamp is added on the server (for sync)
- Removed local echo of user input (to avoid duplicates)
- Added terminal cursor tricks to clear user input after `Enter`

---

## TODO – Upcoming Features

- [ ] Add channels/groups (chat rooms)
- [ ] Build CLI UI navigation (login → channel → chat)
- [ ] Save message history to file on the server
- [ ] Add TLS/SSL encryption for secure messages
- [ ] Create emoji support or text reactions 😄
