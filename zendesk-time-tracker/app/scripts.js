async function get_buttons(value, object) {
    let buttons = await eel.get_buttons()();
    console.log(buttons);
}

var startTimes = {};  // Store start times for each band
var timers = {};  // Move the timers variable inside the function

async function select_button(value, object) {
    console.log("Button selected: " + value);
    var button = document.getElementById(value);
    button.classList.toggle('active');


    if (button.classList.contains('active')) {
        // Start timer
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
        console.log(timers);

    } else {
        console.log("stopping!!");

        // Stop timer
        clearInterval(timers[value]);
        console.log(timers)
    }
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

function login() {
  // If logged in, return the inner HTML that "Fields Last retrieval: ### time"
    eel.new_window('login.html');

    // Run check_headers() every second
    setInterval(async () => {
        const result = await check_headers();
        console.log(result);
        console.log("cookies saved look like: ");
    }, 1000);
}

get_buttons();
