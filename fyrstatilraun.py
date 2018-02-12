import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.output(23,GPIO.LOW)

for y in range (1,5):
    GPIO.output(23,GPIO.HIGH)  
    for x in range (1,20):
      GPIO.output(25,GPIO.HIGH)
      time.sleep(0.01)
      GPIO.output(25,GPIO.LOW)

    time.sleep(0.5)
    GPIO.output(23,GPIO.LOW)  

    
    for x in range (1,40):
      GPIO.output(25,GPIO.HIGH)
      time.sleep(0.005)
      GPIO.output(25,GPIO.LOW)
    time.sleep(1)



GPIO.cleanup()
