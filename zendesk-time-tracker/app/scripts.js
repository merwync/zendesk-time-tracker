async function get_buttons(value, object) {
    let buttons = await eel.get_buttons()();
    console.log(buttons);
}

async function select_button(value, object) {
    console.log("Button selected" + value);
    var button = document.getElementById(value);
    button.addEventListener('click', function() {
    button.classList.add('active');
});

    // let buttons = await eel.set_button(sub=2)();
}

eel.expose(update_buttons);
function update_buttons(buttons, object) {
    console.log(buttons);
    document.querySelector(".button-container").innerHTML = buttons;
}