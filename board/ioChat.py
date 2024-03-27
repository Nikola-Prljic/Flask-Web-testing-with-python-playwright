from flask_login import current_user
from flask_socketio import send, emit

def ioHandler(socketio):

    @socketio.on('connect')
    def connect():
        emit("welcome", current_user.username)

    @socketio.on('sign_in')
    def sign_in():
        print('Client disconnected')