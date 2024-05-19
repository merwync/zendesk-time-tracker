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

async function do_login() {
    window.location.href="https://mkc-labs.zendesk.com/auth/v2/login/signin?redirect=https%3A%2F%2Fyahoo.com";

}

function listCookies() {
    var theCookies = document.cookie.split(';');
    var aString = '';
    for (var i = 1 ; i <= theCookies.length; i++) {
        aString += i + ' ' + theCookies[i-1] + "\n";
    }
    return aString;
}
