import picamera
from time import sleep


with picamera.PiCamera() as camera:
    camera.vflip = True
    # camera.start_preview()
    # sleep(10)
    # camera.stop_preview()
    # camera.exposure_mode = 'night'
    camera.capture('/home/pi/Desktop/image.jpg')
