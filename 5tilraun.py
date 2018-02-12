import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.output(25,GPIO.LOW)
GPIO.output(22,GPIO.HIGH)
blue = 0
seconds = 0
freeze = 0


try:

	while True:
		freeze = GPIO.input(17)
		
		while freeze:
			print "freeze: %d" % freeze
			time.sleep(1)
			freeze = freeze ^ GPIO.input(17)

		if blue:
			print "to red..."
			GPIO.output(25,GPIO.HIGH)
			GPIO.output(22,GPIO.LOW)
			blue = 0
		else:
			print "to blue..."
			GPIO.output(25,GPIO.LOW)
			GPIO.output(22,GPIO.HIGH)
			blue = 1

		time.sleep(1)
		seconds += 1
		if seconds  > 60:
			print "sleeping for 60s..."
			seconds = 0
			time.sleep(60)
finally:
	GPIO.cleanup()
