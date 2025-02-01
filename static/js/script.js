function controlCar(state) {
  fetch('/car', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ state: state })
  })
  .then(response => response.json())
  .then(data => {
      console.log(data.message);
  })
  .catch(error => console.error('Error:', error));
}

let holdInterval;

function handlePress(state) {
    controlCar(state); // Send state immediately
    holdInterval = setInterval(() => controlCar(state), 100); // Repeat while holding
}

function handleRelease() {
    clearInterval(holdInterval); // Stop when button is released
}

function toggleButtonMode(clickedButton) {
    // Deactivate all Mode buttons
    document.querySelectorAll('.mode-button').forEach(button => {
        button.classList.remove('active');
    });
    // Activate the clicked button
    clickedButton.classList.add('active');
}

// Toggle active state for Speed buttons
function toggleButtonSpeed(clickedButton) {
    // Deactivate all Speed buttons
    document.querySelectorAll('.speed-button').forEach(button => {
        button.classList.remove('active');
    });
    // Activate the clicked button
    clickedButton.classList.add('active');
}

// Toggle active state for Light buttons
function toggleButtonLight(clickedButton) {
    // Deactivate all Light buttons
    document.querySelectorAll('.light-button').forEach(button => {
        button.classList.remove('active');
    });
    // Activate the clicked button
    clickedButton.classList.add('active');
}

// JavaScript to handle keypress and send data to Flask backend
document.addEventListener('keydown', function(event) {
    let keyState = '';
    switch (event.key) {
        case 'w': keyState = 'W'; break;
        case 's': keyState = 'S'; break;
        case 'd': keyState = 'D'; break;
        case 'a': keyState = 'A'; break;
        case 'ArrowUp': keyState = 'T'; break;
        case 'ArrowDown': keyState = 'G'; break;
        case 'ArrowRight': keyState = 'F'; break;
        case 'ArrowLeft': keyState = 'H'; break;
        default:
            return; // Ignore keys that do not match any action
    }

    // Send the key state to Flask backend
    fetch('/car', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ state: keyState })
    })
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error('Error:', error));
});