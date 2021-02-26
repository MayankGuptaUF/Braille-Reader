import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2,1)

'''
if(GPIO.input(18)==1):
    print('hey')
else:
    print('yo')
'''