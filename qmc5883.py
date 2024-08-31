import sys
import time
sys.path.append('/usr/lib/python3/dist-packages')
import py_qmc5883l
import math

# Add the path to the py_qmc5883l library
sys.path.append('/usr/lib/python3/dist-packages')

# Create an instance of the QMC5883L sensor
sensor = py_qmc5883l.QMC5883L()

def get_bearing():
    magnet_data = sensor.get_magnet()

    # Unpack the data, handling the case where only two values are returned
    if len(magnet_data) == 2:
        mx, my = magnet_data
        mz = 0
    elif len(magnet_data) == 3:
        mx, my, mz = magnet_data
    else:
        print("Unexpected number of values returned by get_magnet()")
        return None

    # Calculate the heading
    heading = math.atan2(my, mx)
    heading =64+ math.degrees(heading)

    # Normalize the heading to the range [0, 360)
    if heading < 0:
        heading += 360
    if heading > 360:
        heading-=360

    # Return the heading
    return heading

# Testing the getBearing() function



