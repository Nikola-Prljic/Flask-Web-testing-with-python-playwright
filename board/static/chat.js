var socket = io();
var username;
var current_room = "hall";

function displayMessage(msg){
    const outher_div = document.createElement('div');
    outher_div.classList.add("w-100", "chat-right")
    document.getElementById("chat-box-id-" + current_room).appendChild(outher_div);

    const paragraph = document.createElement('div');
    paragraph.classList.add("chat-message")
    paragraph.classList.add("user-message")
    paragraph.textContent = msg;
    outher_div.appendChild(paragraph)
}

socket.on('handleMsg', (msg) => {
    const outher_div = document.createElement('div');
    outher_div.classList.add("w-100", "chat-left")
    document.getElementById("chat-box-id-" + msg[0]).appendChild(outher_div);

    const paragraph = document.createElement('div');
    paragraph.classList.add("chat-message")
    paragraph.textContent = msg[1];
    outher_div.appendChild(paragraph)
});

document.getElementById('chat-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const message = document.getElementById('message-input').value;
    socket.emit('sendToBackend', [current_room, message]);
    displayMessage(`You: ${message}`);
    e.target.reset();
});

document.getElementById('send-button').addEventListener('click', () => {
    const message = document.getElementById('message-input').value;
    socket.emit('sendToBackend', [current_room, message]);
    displayMessage(`You: ${message}`);
    document.getElementById('message-input').value = '';
});

function sendmsg(){
    console.log("Helloooo: " + username)
}

function handleKeyDown(event) {
    if (event.key === "Enter") {
      event.preventDefault(); // Prevent form submission
      sendmsg();
    }
}

function joinRoom() {
    /* const room = document.getElementById('room').value; */
    room = "jo"
    socket.emit('join', {room: room});
}

/* socket.on('connect', (data) => {
    emit("connect")
}); */

function resetButtonColor(room) {
    document.getElementById("header-room").innerText = room;
    const other_buttons = document.getElementsByClassName("room-buttons");
    for (let i = 0; i < other_buttons.length; i++) {
        other_buttons[i].classList.remove("btn-success");
        other_buttons[i].classList.add("btn-primary");
    }
}

function switchChannel(room, rooms_buttons) {
    resetButtonColor(room);
    rooms_buttons.classList.remove("btn-primary");
    rooms_buttons.classList.add("btn-success");
    addChannelBox(room);
}

function addChannelButton(room) {
    const rooms_buttons = document.createElement('button');
    rooms_buttons.innerText=room
    rooms_buttons.classList.add("btn", "btn-success", "room-buttons")
    resetButtonColor(room)
    rooms_buttons.addEventListener("click", function() {
        switchChannel(room, rooms_buttons);
    });
    document.getElementById("rooms-id").appendChild(rooms_buttons);
}

function addChannelBox(room) {
    const old_room = document.getElementById("chat-box-id-" + current_room);
    if (old_room) {
        old_room.style.display = 'none';
    }
    const new_room = document.getElementById("chat-box-id-" + room);
    if (new_room) {
        new_room.style.display = 'block';
        current_room=room;
        return;
    }
    const new_div = document.createElement('div');
    new_div.classList.add("chat-box");
    new_div.setAttribute("id", "chat-box-id-" + room);
    document.getElementById("header-room-div").after(new_div);
    current_room=room;
}

function addChannel(room) {
    addChannelBox(room);
    addChannelButton(room);
}

socket.on('addChannelToFrontend', (room) => {
    addChannel(room)
});

socket.on('listChannels', (rooms) => {
    rooms.forEach(addChannel)
});
