import picamera
import time

with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.hflip = True
    camera.resolution = (1280,720)
    #camera.framerate = 24
    camera.start_preview
    camera.annotate_text = 'annotate'
    time.sleep(2)

    camera.capture('annotatenoframerate.jpg')
# basic recipes
