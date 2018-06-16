import picamera
from time import sleep
camera = picamera.PiCamera()
#camera.vflip = True
#camera.brightness = 90
#camera.contrast = 80
camera.resolution = (3280, 2464)
camera.capture('imageslee5.jpg')
sleep(5)
camera.capture('imagesleep6.jpg')
camera.close()
