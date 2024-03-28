var socket = io();
var username;
var current_room = "hall";

function scrollDownClass(target) {
    const down = document.getElementsByClassName(target);
    for(i = 0; i < down.length; i++){
        down[i].scrollTop = down[i].scrollHeight;
    }
}

function addElementWithClasses(type, class_list, msg) {
    const element = document.createElement(type);
    for(i = 0; i < class_list.length; i++){
        element.classList.add(class_list[i])
    }
    element.textContent = msg;
    return element;
}

function displayMessage(msg){
    const outher_div = document.createElement('div');
    outher_div.classList.add("w-100", "chat-right")
    document.getElementById("chat-box-id-" + current_room).appendChild(outher_div);

    const new_div = addElementWithClasses('div', ["chat-message", "user-message"], msg)
    outher_div.appendChild(new_div);

    /* const paragraph = document.createElement('div');
    paragraph.classList.add("chat-message")
    paragraph.classList.add("user-message")
    paragraph.textContent = msg; */

    scrollDownClass("chat-box");
}

socket.on('handleMsg', (msg) => {
    const outher_div = document.createElement('div');
    outher_div.classList.add("w-100", "chat-left")
    if(msg[0] === "")
        msg[0] = current_room;
    document.getElementById("chat-box-id-" + msg[0]).appendChild(outher_div);

    const paragraph = document.createElement('div');
    paragraph.classList.add("chat-message")
    paragraph.textContent = msg[1];
    outher_div.appendChild(paragraph);
    
    scrollDownClass("chat-box");
});

//SEND MSG FROM INPUT FIELD!
document.getElementById('chat-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const message = document.getElementById('message-input').value;
    if (message.length > 0) {
        socket.emit('sendToBackend', [current_room, message]);
        displayMessage(message);
    }
    e.target.reset();
});

//SEND MSG FROM INPUT FIELD!
document.getElementById('send-button').addEventListener('click', () => {
    const message = document.getElementById('message-input').value;
    if (message.length > 0) {
        socket.emit('sendToBackend', [current_room, message]);
        displayMessage(message);
    }
    document.getElementById('message-input').value = '';
});

socket.on('addChannelToFrontend', (room) => {
    addChannel(room)
});

socket.on('listChannels', (rooms) => {
    rooms.forEach(addChannel)
});
