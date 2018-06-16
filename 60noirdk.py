import time
import picamera
from fractions import Fraction
with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.hflip = True
    camera.framerate = Fraction(1,9)
    camera.shutter_speed = 600000
    camera.exposure_mode = 'off'
    camera.iso = 800
    camera.start_preview()
    try:
        for i, filename in enumerate(camera.capture_continuous('noirdk{counter:02d}.jpg')):
            print(filename)
            time.sleep(300)
            if i == 59:
                break
    finally:
        camera.stop_preview()
#taken from chap10
