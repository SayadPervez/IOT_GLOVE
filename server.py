import socketio
import time


sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid,environ):
    print(f"{sid} CONNECTED !!!")

@sio.event
def disconnect(sid):
    print(f"{sid} DISCONNECTED !!!")

@sio.on("data-request")
def user_data(sid,pwd):
    if(pwd=="Password"):
        sio.emit("data",{"time":time.time()},room=sid)
    else:
        sio.emit("error","Password Incorrect",room=sid)

# gunicorn --threads 50 server:app