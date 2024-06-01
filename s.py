import io
import socket
import struct
import time
import picamera
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((sys.argv[1], int(sys.argv[2])))

connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        print("Starting camera...")
        time.sleep(2)
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg'):
            # Write the length of the capture to the stream and flush to ensure it gets sent.
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            # Rewind the stream and send the image data over the wire.
            stream.seek(0)
            connection.write(stream.read())
            # Reset the stream for the next capture.
            stream.seek(0)
            stream.truncate()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Send end-of-stream signal.
    connection.write(struct.pack('<L', 0))
    connection.close()
    client_socket.close()
