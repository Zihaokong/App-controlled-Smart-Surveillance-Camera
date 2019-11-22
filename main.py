from Servo import Servo

short_servo_pin = 17
long_servo_pin = 27
speed = 0.01
left_max = 2
right_max = 11.5
short_servo = Servo(short_servo_pin,left_max,right_max)
long_servo = Servo(long_servo_pin,left_max,right_max)


short_servo.reset()
long_servo.reset()

