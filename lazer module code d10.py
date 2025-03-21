from machine import Pin, PWM
import time

# Setup Servo Motors
servo1 = PWM(Pin(12), freq=50)  # First Door Servo
servo2 = PWM(Pin(14), freq=50)  # Second Door Servo (Mirrored Motion)

# Setup Laser Sensor
laser_sensor = Pin(13, Pin.IN)  # Digital Output from Laser Sensor

def set_servo_angle(servo, angle):
    duty = int((angle / 180) * 102 + 26)  # Convert angle to duty cycle
    servo.duty(duty)

def open_doors():
    print("🚪 Doors Opening!")
    set_servo_angle(servo1, 90)  # Open first door
    set_servo_angle(servo2, 0)   # Mirror second door

def close_doors():
    print("🚪 Doors Closing!")
    set_servo_angle(servo1, 0)   # Close first door
    set_servo_angle(servo2, 90)  # Mirror second door

while True:
    if laser_sensor.value() == 0:  # Laser is blocked
        open_doors()   # Open doors immediately
        time.sleep(1)  # Keep doors open for 3 seconds
        close_doors()  # Close doors after 3 seconds
