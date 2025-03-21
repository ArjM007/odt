from machine import Pin, PWM
import time

# Setup Servo Motors
servo1 = PWM(Pin(12), freq=50)
servo2 = PWM(Pin(14), freq=50)  
# Setup Laser Sensor
laser_sensor = Pin(13, Pin.IN) 
def set_servo_angle(servo, angle):
    duty = int((angle / 180) * 102 + 26) 
    servo.duty(duty)

def open_doors():
    print(" Doors Opening!")
    set_servo_angle(servo1, 90) 
    set_servo_angle(servo2, 0) 

def close_doors():
    print(" Doors Closing!")
    set_servo_angle(servo1, 0)
    set_servo_angle(servo2, 90) 

while True:
    if laser_sensor.value() == 0:  
        open_doors()  
        time.sleep(1) 
        close_doors() 
