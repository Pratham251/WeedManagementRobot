import time
import threading
import json
import websocket
from mdriver import forward,backward,cw,ccw,stp,toggle_servo_90,toggle_servo_0
from qmc5883 import get_bearing
from gps import get_gps,calculate_distance,calculate_bearing
from jsonh import process_message,x, y, tlat, tlon, confidence
import jsonh
ws_url = "wss://last-semester-project-8ef3ff6c0fd6.herokuapp.com:443"
clat=0
clon=0
distance =0
bearing=0
auto =0
berr=0
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
        #print(f"Sent message to server: {message}")
    else:
        print("WebSocket connection is not established.")

def send_coordinates():
    global clat,clon
    lat_lon = get_gps()
    if lat_lon is not None:
        lat, lon = lat_lon
        if lat is not None and lon is not None:
            send_message(ws, json.dumps({"lat": lat, "lng": lon}))
            time.sleep(0.001)
            clat = lat
            clon = lon
    else:
        print("Failed to get GPS data. Skipping sending coordinates.")
# Create WebSocket instance
ws = websocket.WebSocketApp(ws_url,
                            on_message=on_message,
                            on_error=on_error,
                            on_open=on_open)

# Start a thread for the WebSocket connection
ws_thread = threading.Thread(target=ws.run_forever)
ws_thread.daemon = True
ws_thread.start()

try:
    while True:
        if (jsonh.confidence == 1):
           toggle_servo_90()
           print("servo act")
        if (jsonh.confidence ==0):
           toggle_servo_0()
           print("servo deact")
        send_coordinates()
        if clat is not None and clon is not None and jsonh.tlat is not None and jsonh.tlon is not None:
                distance=calculate_distance(clat, clon,jsonh.tlat,jsonh.tlon)
                bearing=calculate_bearing(clat, clon,jsonh.tlat,jsonh.tlon)
        if (jsonh.x<100 and jsonh.y<100):
            auto =0
        if (jsonh.y<20 and auto is not 1 ):
            forward()
            auto = 0
        if (jsonh.y > 20 and auto is not 1):
            backward()
            auto = 0
        if (jsonh.x > 20 and auto is not 1):
            cw()
            auto = 0
        if (jsonh.x <- 20 and auto is not 1):
            ccw()
            auto = 0
        if(jsonh.x == 0 and jsonh.y ==  0):
            stp()
        if(jsonh.x>100 or jsonh.y>100):
            auto=1
        berr = get_bearing() - bearing
        if berr > 180:
           berr -= 360
        if berr < -180:  # Added a colon here
           berr += 360  # Corrected indentation for this line

        if auto:
            if (abs(berr)<5):
                backward()
            if (berr<-5):
                cw()
            if (berr>5):
                ccw()
            if (distance*1000<0.8):
                stp()
        print(f"auto :{auto},x: {jsonh.x}, y: {jsonh.y}, tlat: {jsonh.tlat}, tlon: {jsonh.tlon}, confidence: {jsonh.confidence},distance: {distance*1000},bearing: {bearing},Cbear:{get_bearing()},bearing diff:{berr}",end="\r")
        time.sleep(0.0011)  # Adjust the interval as needed
except KeyboardInterrupt:

# Clean up and exit gracefully
 stp()
 ws.close()
 ws_thread.join()
