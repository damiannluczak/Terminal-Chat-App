# CLI Chat – Terminal Chat Application

CLI Chat is a lightweight terminal-based chat application written in Python. It allows users to communicate in real-time over a local or remote network, supporting multiple chat rooms and basic message formatting. The project is designed with clarity, modularity, and simplicity in mind.

## Key Features

- Multi-room support (e.g. `lobby`, `room1`, `room2`)
- Real-time message exchange using TCP sockets
- Message formatting with timestamps and user highlighting
- Basic server-side logging (message history, user activity)
- Modular codebase split into server and client logic

## Technologies

- Python 3.12
- TCP sockets
- Multithreading
- JSON message format
- ANSI terminal colors (optional)

## Project Structure

```
CliChat/
├── client.py
├── server.py
├── functions/
│   ├── __init__.py
│   ├── client_func.py
│   ├── server_func.py
│   ├── command.py
├── .gitignore
└── README.md
```

## Usage

### Start the server
```bash
python server.py
```

### Start a client
```bash
python client.py
```

Each user can enter a username and join or create a chat room.

## Example Use Cases

- Educational project to understand networking and sockets in Python
- LAN chat during workshops or coding sessions
- Lightweight communication tool in isolated environments


## Possible Extensions

- User authentication system
- Message encryption
- WebSocket-based version
- Persistent message storage (e.g. SQLite or JSON logs)

