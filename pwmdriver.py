import RPi.GPIO as GPIO 
import time 
import math
# Set up GPIO pins
GPIO.setmode(GPIO.BCM) 
GPIO.setup(25, GPIO.OUT) 
GPIO.setup(4, GPIO.OUT)
# Define PWM frequency and amplitude
frequency = 2000 # Hz amplitude = 50 # % 
try:
    # Create and start PWM objects on both pins
    pwm25= GPIO.PWM(25, frequency) 
    pwm4 = GPIO.PWM(4, frequency) 
    pwm25.start(0) 
    pwm4.start(0) 
    while True:
        # Generate a sine wave
        for i in range(90):
            # Calculate the PWM duty cycle based on the sine wave
            duty_cycle = 100 * (math.sin(math.radians(i)))
            # Print the duty cycle
            print("Duty Cycle:", duty_cycle)
            # Set the PWM duty cycle on both pins
            pwm25.ChangeDutyCycle(duty_cycle) 
            pwm4.ChangeDutyCycle(duty_cycle)
            # Wait for a short period to generate the sine wave
            time.sleep(0.01) 
except KeyboardInterrupt:
    # Clean up GPIO pins on exit
    pwm25.stop() 
    pwm4.stop() 
    GPIO.cleanup()
