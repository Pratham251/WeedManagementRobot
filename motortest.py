import RPi.GPIO as GPIO
import time
import math

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for motors
motor_pins = [22, 23, 24, 27]
speed_pins = [4, 25]

for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
for pin in speed_pins:
    GPIO.setup(pin, GPIO.OUT)

# Set up PWM for motor speed control
pwm25 = GPIO.PWM(25, 2000)   # pin 25, frequency 2000Hz
pwm4 = GPIO.PWM(4, 2000)     # pin 4, frequency 2000Hz

# Start PWM with 0 duty cycle
pwm25.start(0)
pwm4.start(0)

# Motor control functions
def rf():
    GPIO.output(27, GPIO.HIGH)  # IN1
    GPIO.output(22, GPIO.LOW)   # IN2

def rb():
    GPIO.output(27, GPIO.LOW)   # IN1
    GPIO.output(22, GPIO.HIGH)  # IN2

def lf():
    GPIO.output(23, GPIO.HIGH)  # IN3
    GPIO.output(24, GPIO.LOW)   # IN4

def lb():
    GPIO.output(23, GPIO.LOW)   # IN3
    GPIO.output(24, GPIO.HIGH)  # IN4

def stp():
    GPIO.output(27, GPIO.HIGH)  # IN1
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)  # IN3
    GPIO.output(24, GPIO.HIGH)

# Function to control motor speed
def set_motor_speed(left_speed, right_speed):
    # Ensure speed is within 0-100%
    left_speed = max(0, min(150, left_speed))
    right_speed = max(0, min(150, right_speed))
    
    # Set PWM duty cycle
    pwm4.ChangeDutyCycle(left_speed)
    pwm25.ChangeDutyCycle(right_speed)
    print(f"Setting motor speeds: Left = {left_speed}%, Right = {right_speed}%")

# Movement functions
def forward():
    print("Moving forward")
    rf()
    lf()

def backward():
    print("Moving backward")
    rb()
    lb()

def cw():
    print("Rotating clockwise")
    rb()
    lf()

def ccw():
    print("Rotating counterclockwise")
    rf()
    lb()

# Example usage with a long sequence of different directions and speeds
try:
    while True:
        forward()  # Move forward
        set_motor_speed(50, 50)  # Set speed of left and right motors to 50%
        time.sleep(5)  # Move for 2 seconds

        backward()  # Move backward
        set_motor_speed(60, 60)  # Set speed of left and right motors to 30%
        time.sleep(5)  # Move for 2 seconds

        cw()  # Rotate clockwise
        set_motor_speed(70, 70)  # Set speed of left and right motors to 70%
        time.sleep(5)  # Rotate for 2 seconds

        ccw()  # Rotate counterclockwise
        set_motor_speed(70, 70)  # Set speed of left and right motors to 70%
        time.sleep(5)  # Rotate for 2 seconds

        stp()  # Stop all motors
        print("Stopping")
        time.sleep(5)  # Stop for 2 seconds

        forward()
        set_motor_speed(100, 60)
        time.sleep(5)

        backward()
        set_motor_speed(60, 100)
        time.sleep(5)

        cw()
        set_motor_speed(100, 100)
        time.sleep(5)

        ccw()
        set_motor_speed(60, 60)
        time.sleep(5)

        stp()
        print("Stopping")
        time.sleep(5)
        break
except KeyboardInterrupt:
    # Clean up GPIO pins on exit
    pwm25.stop()
    pwm4.stop()
    GPIO.cleanup()
    print("Exiting program and cleaning up GPIO pins")
