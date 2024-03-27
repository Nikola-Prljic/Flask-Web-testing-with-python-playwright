from flask_login import current_user
from flask_socketio import send, emit
from flask import session

def ioHandler(socketio):

    @socketio.on('connect')
    def connect():
        emit("handleMsg", "Hello, " + current_user.username)

    @socketio.on('sign_in')
    def sign_in():
        print('Client disconnected')

    @socketio.on('sendToBackend')
    def forwardMsg(msg):
        print(session)
        print("rcv msg: " + msg)
        emit("handleMsg",msg, broadcast=True, include_self=False)