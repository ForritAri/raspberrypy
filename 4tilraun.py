import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.output(25,GPIO.LOW)
GPIO.output(22,GPIO.HIGH)
blue = 0
already_changed = 0

try:
	while True:
		change_request = GPIO.input(17)  

		if (change_request):
			if (not already_changed):
				if (blue):
					GPIO.output(25,GPIO.HIGH)
					GPIO.output(22,GPIO.LOW)
					blue = 0
				else:
					GPIO.output(25,GPIO.LOW)
					GPIO.output(22,GPIO.HIGH)
					blue = 1
				
				already_changed = 1
		else:
			already_changed = 0

		time.sleep(0.01)

finally:
	GPIO.cleanup()
