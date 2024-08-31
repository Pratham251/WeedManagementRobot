import serial
# Create a serial object for UART communication
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1) 
def getGPS():
    data = ser.readline().decode('utf-8').strip()
    
    if data: 
        print(f"Received raw data: {data}") 
        return data 
    else: 
        print("Error: No data received") 
        return None
# Example usage
while True: 
  getGPS()
