
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
