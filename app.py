from flask import Flask, render_template, request, jsonify
import serial
from serial.serialutil import SerialException
import user_agents
import threading

app = Flask(__name__)

# Initialize serial communication
try:
    ser = serial.Serial('COM10', 9600, timeout=1)#tuja treba svoj com da se stavi u zavisnost u koju portu ti e arduino vidi u device manager
except SerialException as e:
    ser = None
    print(f"Error opening serial port: {e}")

# Global variable to store the latest data from Arduino
arduino_data = None

def read_from_serial():
    global arduino_data
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            # Read the byte data from Arduino
            arduino_data = ser.read(1)  # Read 1 byte
            arduino_data = int.from_bytes(arduino_data, byteorder='big')  # Convert byte to an integer

# Start the serial reading in a separate thread
threading.Thread(target=read_from_serial, daemon=True).start()

@app.route('/')
def index():
    user_agent=request.headers.get('User-Agent')
    ua= user_agents.parse(user_agent)
    
    if arduino_data == 1 or arduino_data == 49:
        message = "SECURE!!! NO GAS DETECTED" 
    elif arduino_data == 2 or arduino_data == 50:
        message = "WARNING!!! GAS DETECTED" 
    else:
        message = "No data from Arduino"

    if ua.is_mobile:
        return render_template('index.html', message=message)#trebashe da ima poseban html za mobilan ama ne uspea jbg
    else:
        return render_template('index.html', message=message)

@app.route('/car', methods=['POST'])
def car():
    if ser and ser.is_open:
        data = request.get_json()  # Get JSON data sent by fetch
        state = data.get('state')
        if state == 'N':
            ser.write(bytes([1]))
        elif state == 'M':
            ser.write(bytes([2]))
        elif state == 'X':
            ser.write(bytes([3])) 
        elif state == 'W':
            ser.write(bytes([4])) 
        elif state == 'S':
            ser.write(bytes([5])) 
        elif state == 'D':
            ser.write(bytes([6])) 
        elif state == 'A':
            ser.write(bytes([7]))
        elif state == 'T':
            ser.write(bytes([9]))
        elif state == 'G':
            ser.write(bytes([10]))
        elif state == 'F':
            ser.write(bytes([11]))
        elif state == 'H':
            ser.write(bytes([12]))
        elif state == 'L':
            ser.write(bytes([13]))
        elif state == 'K':
            ser.write(bytes([14]))
        elif state == 'O':
            ser.write(bytes([15]))
        elif state == 'P':
            ser.write(bytes([16]))
        elif state == 'I':
            ser.write(bytes([17]))
        return jsonify({'message': 'Info sent'}), 200
    else:
        return jsonify({'error': 'Serial port not available'}), 500

if __name__ == '__main__':
    # Run the app on all network interfaces
    app.run(host='192.168.1.141', port=5000, debug=True)# tuj de host od ipconfg da se vidi adresda treba