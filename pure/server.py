import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '$DISCONNECT!!!'
PORT = 4000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while(connected):
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if(msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if(msg==DISCONNECT_MSG):
                connected = False
                print(f"[DISCONNECTED] {addr}")
                conn.send("Securely Terminated !!!".encode(FORMAT))
            else:
                print(f'[{addr}] {msg}')
                conn.send("GOTCHA !!!".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[SERVER IS LISTENING AT {SERVER}]")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handleClient,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()