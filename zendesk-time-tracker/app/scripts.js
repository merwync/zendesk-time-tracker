async function get_buttons(value, object) {
    let buttons = await eel.get_buttons()();
    console.log(buttons);
}

var startTimes = {};  // Store start times for each band
var timers = {};  // Move the timers variable inside the function


async function activate_timer(value, startTime, object) {
    eel.start_timer(value)

    console.log("starting timer!")
    startTimes[value] = Date.now();
    timers[value] = setInterval(function() {
        // Update timer for this band
        var elapsedTime = Date.now() - startTimes[value];

        var hours = Math.floor(elapsedTime / 3600000);
        var minutes = Math.floor((elapsedTime % 3600000) / 60000);
        var seconds = Math.floor((elapsedTime % 60000) / 1000);

        document.getElementById('hours-' + value).textContent = padZero(hours);
        document.getElementById('minutes-' + value).textContent = padZero(minutes);
        document.getElementById('seconds-' + value).textContent = padZero(seconds);
    }, 1000);

}

eel.expose(select_button);
async function select_button(value, object) {
    console.log("Button selected: " + value);
    var button = document.getElementById(value);
    button.classList.toggle('active');

    if (button.classList.contains('active')) {
        // Start timer
        activate_timer(value)
        console.log(timers);
    } else {
        // Stop timer
        console.log("stopping!!");
        clearInterval(timers[value]);
        console.log(timers)
        eel.stop_timer(value)

    }
}

eel.expose(set_active_js)
async function set_active_js() {
    var values = await eel.get_active()();
    console.info(values);
    values.forEach((active) => {
        console.info(active);
        select_button(active);
    });
}

function padZero(number) {
    return number.toString().padStart(2, '0');
}


eel.expose(addEventListeners);
function addEventListeners(values, object) {
    console.log(values)
    values.forEach((id) => {
        var button = document.getElementById(id);
        if (button) {
            button.addEventListener('click', function() {
            });
        }
    });
}

eel.expose(update_buttons);
function update_buttons(buttons, object) {
    console.log(buttons);
    document.querySelector(".button-container").innerHTML = buttons;
}

async function do_login() {
    await eel.python_print('Go to Login')();
    eel.python_print('At login')();
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function check_headers() {
    console.log("my check header is " + 0);

    // Simulating an external function (replace with your actual logic)
  const external_function = Math.random() < 0.5 ? 0 : 1;

      if (external_function === 0) {
        return 0;
      } else {
        return 1;
      }
}

function get_json_results() {
    const url = "https://d3v-mkc-labs.zendesk.com/api/v2/views/hydrate.json?filter%5Bids%5D=2%2C1&include=last_comment";
    window.open(url, '_blank');
    fetch(url)
      .then((response) => response.json())
      .then((json) => console.log(json));

}

function login() {

  const url = "https://d3v-mkc-labs.zendesk.com/auth/v2/login/signin?return_to=https%3A%2F%2Fd3v-mkc-labs.zendesk.com%2F";
  window.open(url, '_blank');


  // If logged in, return the inner HTML that "Fields Last retrieval: ### time"
    //eel.new_window('login.html');

    // Run check_headers() every second
    setInterval(async () => {
        const result = await check_headers();
        console.log(result);
        console.log("cookies saved look like: ");
    }, 1000);
}

function open_menu() {
    menu = document.getElementById("nav")
    menu.classList.toggle('open');
}


function add_manual_entry() {
    var entry = document.querySelector("#new-manual-entry").value;
    console.log("Adding new manual value: " + entry);
    eel.add_manual_entry(entry)();
    set_active_js();
}


get_buttons();
set_active_js();