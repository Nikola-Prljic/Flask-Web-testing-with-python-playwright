from flask_login import current_user
from flask_socketio import emit, join_room
from flask import session
from chatParsing import Parsing

users_in_rooms = {}

def ioHandler(socketio):

    @socketio.on('connect')
    def connect():
        emit("handleMsg", "Hello, " + current_user.username)
        rooms = []
        for key in users_in_rooms:
            if current_user.username in users_in_rooms[key]:
                rooms.append(key)
        emit('listChannels', rooms)
    

    @socketio.on('sign_in')
    def sign_in():
        print('Client disconnected')

    @socketio.on('sendToBackend')
    def forwardMsg(msg):
        emit("handleMsg", msg[1], room=msg[0], include_self=False)

        parsing = Parsing(msg[1])
        cmds = parsing.cmdSwitch()
        if cmds is None:
            return
        if cmds['cmd'] == "/join":
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
        emit('addChannelToFrontend', room)

    def msgToRoom(room:str, msg:str):
        emit('handleMsg', current_user.username + ": " + msg, room=room, include_self=False)