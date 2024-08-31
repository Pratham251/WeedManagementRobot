import serial
from math import radians, sin, cos, sqrt, atan2, degrees

# Create a serial object for UART communication
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
lat_deg = 0
lat_min = 0.0
lon_deg = 0
lon_min = 0.0

def get_gps():
    data = ser.readline().decode('utf-8').strip()
    print(data)
    # Check if the data is a GGA sentence and contains a valid GPS fix
    if data.startswith('$GNGGA'):
        parts = data.split(',')
        # Check GPS fix quality (parts[6])
        if parts[6] == '1':
            # Extract latitude (parts[2]) and longitude (parts[4])
            lat_deg = int(parts[2][0:2])
            lat_min = float(parts[2][2:])
            lon_deg = int(parts[4][0:3])
            lon_min = float(parts[4][3:])
            return (lat_deg + lat_min / 60, lon_deg + lon_min / 60)
    else:
        return None, None

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers
    #distance=distance*1000
    return distance

def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1

    x = cos(lat2) * sin(dlon)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)

    initial_bearing = atan2(x, y)

    # Normalize the result to a compass bearing in degrees (0° <= bearing < 360°)
    initial_bearing = (degrees(initial_bearing) + 360) % 360

    return initial_bearing
import serial
from math import radians, sin, cos, sqrt, atan2, degrees

# Create a serial object for UART communication
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
lat_deg = 0
lat_min = 0.0
lon_deg = 0
lon_min = 0.0

def get_gps():
    data = ser.readline().decode('utf-8').strip()

    # Check if the data is a GGA sentence and contains a valid GPS fix
    if data.startswith('$GNGGA'):
        parts = data.split(',')
        # Check GPS fix quality (parts[6])
        if parts[6] == '1':
            # Extract latitude (parts[2]) and longitude (parts[4])
            lat_deg = int(parts[2][0:2])
            lat_min = float(parts[2][2:])
            lon_deg = int(parts[4][0:3])
            lon_min = float(parts[4][3:])
            return (lat_deg + lat_min / 60, lon_deg + lon_min / 60)
    else:
        return None, None

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers

    return distance

def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1

    x = cos(lat2) * sin(dlon)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)

    initial_bearing = atan2(x, y)

    # Normalize the result to a compass bearing in degrees (0° <= bearing < 360°)
    initial_bearing = (degrees(initial_bearing) + 360) % 360

    return initial_bearing

