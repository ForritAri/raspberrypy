import time
import picamera

with picamera.PiCamera() as camera:

    camera.start_recording('/home/pi/Desktop/video.h264')
    time.sleep(20)
    camera.stop_recording()
