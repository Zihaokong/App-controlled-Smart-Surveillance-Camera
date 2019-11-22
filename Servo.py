import RPi.GPIO as GPIO
from time import sleep

class Servo:
        
    _port_num = 0
    _left_min = 2
    _right_max = 11.5

    def __init__(self,port_num,left_min,right_max):
        self._port_num = port_num
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._port_num, GPIO.OUT)
        
        self._servo = GPIO.PWM(port_num, 50)
        self._left_min = left_min
        self._right_max = right_max
        

    

    
    def reset(self):
        self._servo.start(self._left_min)       
        sleep(0.3)
        self._servo.ChangeDutyCycle(self._right_max)
        sleep(0.3)
        self._servo.ChangeDutyCycle(0)
        sleep(0.1)
        """
        start = self._left_min
        increment = 0.1
        while 1:
            self._servo.ChangeDutyCycle(start)
            sleep(0.01)
            start=start+increment
            if start>self._right_max or start<self._left_min:
                increment = -increment
        """
    def surveillance(self,speed):
        start = self._left_min
        increment = speed
        while 1:
            self._servo.ChangeDutyCycle(start)
            sleep(0.01)
            start=start+increment
            if start>self._right_max or start<self._left_min:
                increment = -increment
