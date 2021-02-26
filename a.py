
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

'''
GPIO.output(2,GPIO.HIGH)
GPIO.output(3,GPIO.HIGH)
GPIO.output(4,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)

time.sleep(3)

GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

        
'''    

#hecking all the LED's 
a=[2,3,4,17,27,22]
for j in a:
    for i in range(10):
        print("LED on")
        GPIO.output(j,GPIO.HIGH)
        time.sleep(0.05)
        print("LED off")
        GPIO.output(j,GPIO.LOW)
        time.sleep(0.05)



