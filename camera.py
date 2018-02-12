import picamera


with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.capture('/home/pi/Desktop/image.jpg')
