import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to Server")
    while(True):
        sio.emit("data-request","Password")
        time.sleep(1)

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.on("data")
def ver(x):
    print(f"Time from server : \n{x}")

@sio.on("error")
def verificate(x):
    print(f"Error from Server : \n{x}")
    sio.disconnect()

sio.connect("http://127.0.0.1:8000")