var startButton = document.getElementById('start');
var stopButton = document.getElementById('stop');
var resetButton = document.getElementById('reset');
var minutesSpan = document.getElementById('minutes');
var secondsSpan = document.getElementById('seconds');
var millisecondsSpan = document.getElementById('milliseconds');

var stopwatchInterval;
var startTime;

startButton.addEventListener('click', function() {
  startTime = Date.now();
  stopwatchInterval = setInterval(updateStopwatch, 10);
});

stopButton.addEventListener('click', function() {
  clearInterval(stopwatchInterval);
});

resetButton.addEventListener('click', function() {
  clearInterval(stopwatchInterval);
  minutesSpan.textContent = '00';
  secondsSpan.textContent = '00';
  millisecondsSpan.textContent = '00';
});

function updateStopwatch() {
  var elapsedTime = Date.now() - startTime;

  var minutes = Math.floor(elapsedTime / 60000);
  var seconds = Math.floor((elapsedTime % 60000) / 1000);
  var milliseconds = Math.floor((elapsedTime % 1000) / 10);

  minutesSpan.textContent = padZero(minutes);
  secondsSpan.textContent = padZero(seconds);
  millisecondsSpan.textContent = padZero(milliseconds);
}

function padZero(number) {
  return number.toString().padStart(2, '0');
}
