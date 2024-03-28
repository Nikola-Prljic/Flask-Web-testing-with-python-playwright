/* class createChannels {
  
  constructor(room, current_room) {
    this.room = room;
    this.current_room = current_room;
  }

  resetButtonColor() {
    document.getElementById("header-room").innerText = this.current_room;
    const other_buttons = document.getElementsByClassName("room-buttons");
    for (let i = 0; i < other_buttons.length; i++) {
      other_buttons[i].classList.remove("btn-success");
      other_buttons[i].classList.add("btn-primary");
    }
  }

  switchChannel(rooms_buttons) {
    this.resetButtonColor();
    rooms_buttons.classList.remove("btn-primary");
    rooms_buttons.classList.add("btn-success");
    this.addChannelBox();
  }

  addChannelButton() {
    const rooms_buttons = document.createElement('button');
    rooms_buttons.innerText=this.room
    rooms_buttons.classList.add("btn", "btn-success", "room-buttons")
    this.resetButtonColor()

    const self = this;
    rooms_buttons.addEventListener("click", function() {
      self.switchChannel(rooms_buttons);
    });
    document.getElementById("rooms-id").appendChild(rooms_buttons);
  }

  addChannelBox() {
    const old_room = document.getElementById("chat-box-id-" + this.current_room);
    if (old_room) {
        old_room.style.display = 'none';
    }
    const new_room = document.getElementById("chat-box-id-" + this.room);
    if (new_room) {
        new_room.style.display = 'block';
        return this.room;
    }
    const new_div = document.createElement('div');
    new_div.classList.add("chat-box");
    new_div.setAttribute("id", "chat-box-id-" + this.room);
    document.getElementById("header-room-div").after(new_div);
    return this.room;
  }

  addChannel() {
    this.current_room = this.addChannelBox();
    this.addChannelButton();
    return this.current_room;
  }
} */