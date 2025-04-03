# 💬 Terminal Chat App (Python TCP)

A simple terminal-based chat application built with **Python sockets** and **threading**, allowing multiple users to chat in real-time. Designed to learn and showcase skills in network programming, concurrency, and client-server architecture.

---

## 🚀 Features

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
- Established TCP connection with `socket`
- Sent messages from client to server

### Commit #2 – "Broadcasting and Receive Thread"
- Added `username` handling on client side
- Implemented **multi-client support** using `threading` in server
- Created server-side **message broadcasting** to all clients
- Implemented **receive thread** on client side to handle incoming messages live
- Added graceful disconnect with `!DISCONNECT`
- Cleaned up and improved logging

### Commit #3 – "Basic Commands"
- Added /help -   prints available commands
- Added /list -  displays list of online users

### Commit #4 – "Bug fix, code clean up"
- Extracted functions to seperate files 
- Added safe re-run
- Repaired display and input UX
- Code cleanup 

## TODO – Upcoming Features

- [ ] Implement commands: `/quit`
- [ ] Add channels/groups: individual chat rooms or topics
- [ ] Build structured CLI UI with navigation levels
  - login → choose channel → enter chat
- [ ] Save message logs to a file on the server
- [ ] Add SSL/TLS encryption for secure communication




