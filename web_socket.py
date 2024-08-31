import time
import threading
import websocket
from jsonh import process_message

# Define WebSocket event handlers
def on_message(ws, message):
    print(f"Received message from server: {message}")
    process_message(message)

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_open(ws):
    print("WebSocket connection established.")

def send_message(ws, message):
    if ws.sock and ws.sock.connected:
        ws.send(message)
        print(f"Sent message to server: {message}")
    else:
        print("WebSocket connection is not established.")

# WebSocket URL
ws_url = "wss://last-semester-project-8ef3ff6c0fd6.herokuapp.com:443"

# Create WebSocket instance
ws = websocket.WebSocketApp(ws_url,
                            on_message=on_message,
                            on_error=on_error,
                            on_open=on_open)

# Start a thread for the WebSocket connection
ws_thread = threading.Thread(target=ws.run_forever)
ws_thread.daemon = True
ws_thread.start()

# Wait for the WebSocket connection to be established
while not ws.sock or not ws.sock.connected:
    time.sleep(1)

# Main loop to send GPS data to the server
while True:
     # Get GPS data
    lat, lon = 20.2323233,30.232334234
    if lat is not None and lon is not None:
        send_message(ws, f'{{"lat": {lat}, "lon": {lon}}}')
        time.sleep(0.1)  # Adjust the sleep time as needed

# Keep the main thread running until the WebSocket connection is closed
ws_thread.join()
