from time import sleep
from picamera import PiCamera

camera = PiCamera()
#camera.vflip = True
#camera.brightness = 30
#camera.contrast = 50
camera.start_preview()
sleep(200)
