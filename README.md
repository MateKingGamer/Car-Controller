# Car Control Web Interface

This project is a Flask-based web application that allows users to control a robotic car using their keyboard. The interface listens for key presses and sends corresponding commands to an Arduino via serial communication.

## Features
- Real-time keypress detection to control the car.
- Buttons that visually indicate active controls.
- Communication with an Arduino over a serial connection.
- Simple Flask backend to handle key events.

## Technologies Used
- **Python** (Flask for the backend)
- **JavaScript** (Key listener and fetch requests)
- **HTML/CSS** (Basic interface with active button states)
- **Serial Communication** (Using `pyserial` for communication with Arduino)

## Installation
### Prerequisites
- Python 3 installed
- `pip` installed
- An Arduino or another serial device connected

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/car-control-web.git
   cd car-control-web
   ```

2. Install dependencies:
   ```sh
   pip install flask pyserial
   ```

3. Run the Flask server:
   ```sh
   python app.py
   ```

4. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Press the following keys to control the car:
  - `W` - Move Forward
  - `S` - Move Backward
  - `A` - Turn Left
  - `D` - Turn Right
  - `N` - Neutral
  - `M` - Move Mode
  - `L` - Left Turn
  - `K` - Right Turn
  - `O` - Stop
  - `P` - Pause
  - `I` - Start
- The corresponding button on the web page will highlight when a key is pressed.

## Troubleshooting
- If the serial port is unavailable, ensure that your Arduino is properly connected and the correct COM port is used in `app.py`.
- If Flask does not start, check for missing dependencies and install them using `pip install -r requirements.txt` (if available).

## Future Enhancements
- Improve the UI with additional indicators (e.g., current speed, battery status).
- Implement WebSocket for real-time communication.
- Add support for game controller input.

## License
This project is open-source and available under the MIT License.

---
Feel free to contribute to this project by submitting issues or pull requests!

