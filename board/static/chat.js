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

socket.on('addChannelToFrontend', (room) => {
    addChannel(room)
});

socket.on('listChannels', (rooms) => {
    rooms.forEach(addChannel)
});
