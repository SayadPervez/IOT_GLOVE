import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid,environ):
    print(f"{sid} CONNECTED !!!")

@sio.event
def disconnect(sid):
    print(f"{sid} DISCONNECTED !!!")

# gunicorn --threads 50 server:app