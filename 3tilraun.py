import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.output(25,GPIO.LOW)
GPIO.output(22,GPIO.HIGH)
light = 0

try:
	while True:
		input = GPIO.input(17)  

		if (input):
			print("Who let the dogs out?!?")
			if (not light):
				GPIO.output(25,GPIO.HIGH)
				GPIO.output(22,GPIO.LOW)
				light = 1
				
			else:
				GPIO.output(25,GPIO.LOW)
				GPIO.output(22,GPIO.HIGH)
				light = 0
			time.sleep(0.1) # stop pushing!

		time.sleep(0.1)

finally:
	GPIO.cleanup()
    