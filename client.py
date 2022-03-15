import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to Server")
    time.sleep(5)
    sio.disconnect()

@sio.event
def disconnect():
    print("Disconnected from server")

sio.connect("http://127.0.0.1:8000")