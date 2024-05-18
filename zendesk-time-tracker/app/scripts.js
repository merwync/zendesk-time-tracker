async function get_buttons(value, object) {
    let buttons = await eel.get_buttons()();
    console.log(buttons);
    document.querySelector(".button-container").innerHTML = buttons;
}

async function select_button(value, object) {
    console.log("Button selected" + value);
    let buttons = await eel.get_buttons(sub=1)();
    document.querySelector(".button-container").innerHTML = buttons;
    console.log("Buttons redrawn.");
}