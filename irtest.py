import RPi.GPIO as GPIO

import time
import picamera

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(4, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

#GPIO.output(4, GPIO.HIGH)
GPIO.output(7, GPIO.HIGH)
with picamera.PiCamera() as camera:

	camera.start_preview()
	time.sleep(5)
	camera.capture('/home/pi/Desktop/test.jpg')
	camera.stop_preview()

#GPIO.output(4, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
