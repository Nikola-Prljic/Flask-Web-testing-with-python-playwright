from flask_login import current_user
from flask_socketio import emit, join_room
from flask import session
from chatParsing import Parsing

users_in_rooms = {}

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
        parsing = Parsing(msg)
        cmds = parsing.cmdSwitch()
        if cmds == None:
            emit("handleMsg",msg, broadcast=True, include_self=False)
        elif cmds['cmd'] == "/join":
            on_join(cmds['room'])
        elif cmds['cmd'] == "/msg":
            msgToRoom(cmds['room'], cmds['msg'])

    @socketio.on('join')
    def on_join(room):
        username = current_user.username
        if username in users_in_rooms.get(room, []):
            emit('handleMsg', f'{username} is already in the room {room}')
            return
        join_room(room)
        if room not in users_in_rooms:
            users_in_rooms[room] = []
        users_in_rooms[room].append(username)
        emit('handleMsg', f'{username} has joined the room {room}', room=room, include_self=False)
        """ emit('joined', f'{username} has joined the room {room}', room=room) """

    def msgToRoom(room:str, msg:str):
        emit('handleMsg', current_user.username + ": " + msg, room=room, include_self=False)