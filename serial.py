import serial
import time

# Set up the serial connection to the HC-06 module
ser = serial.Serial('/dev/ttyS0', 9600)  # Adjust the port name if necessary
time.sleep(2)  # Wait for the serial connection to initialize

def send_data(data):
    ser.write(data.encode())  # Send data to the HC-06 module

def receive_data():
    if ser.in_waiting > 0:
        return ser.readline().decode().strip()
    return None

try:
    while True:
        # Example of sending data
        send_data("Hello from Raspberry Pi")
        time.sleep(1)  # Wait for a second before sending next data
        
        # Example of receiving data
        received = receive_data()
        if received:
            print(f"Received: {received}")

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    ser.close()
