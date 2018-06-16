import picamera
from time import sleep
from fractions import Fraction

with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.hflip = True
    camera.resolution = (1280,720)
    #set framerate 1/6fps,shutter speed 6s and ISO 800
    camera.framerate = Fraction(1, 9)
    camera.shutter_speed = 9000000
    camera.exposure_mode = 'off'
    camera.iso = 800
    #long time for camera to measure AWB, or fix
    sleep(10)

    camera.capture('dark3.jpg')
# basic recipes
