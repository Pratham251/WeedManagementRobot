import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for motors and servos
motor_pins = [22, 23, 24, 27]
servo_pins = [4, 25]

for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)

# Set up PWM for servo pins
servo_pwm_4 = GPIO.PWM(4, 50)   # pin 4, frequency 50Hz for servos
servo_pwm_25 = GPIO.PWM(25, 50)  # pin 25, frequency 50Hz for servos

# Start PWM with 0 duty cycle
servo_pwm_4.start(0)
servo_pwm_25.start(0)

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

# Function to set servo angle on a specific pin
def set_servo_angle(pin, angle):
    duty = 2 + (angle / 18)  # Convert angle to duty cycle
    if pin == 4:
        servo_pwm_4.ChangeDutyCycle(duty)
    elif pin == 25:
        servo_pwm_25.ChangeDutyCycle(duty)

# Movement functions
def forward():
    rf()
    lf()

def backward():
    rb()
    lb()

def cw():
    rb()
    lf()

def ccw():
    rf()
    lb()

# Function to toggle servo on pin 4 between 0 and 90 degrees
def toggle_servo_90():
    set_servo_angle(4, 100)
    
# Function to toggle servo on pin 25 between 0 and 90 degrees
def toggle_servo_0():
    set_servo_angle(4,0)
# Example usage

