from time import sleep
import picamera
camera = picamera.PiCamera()
camera.vflip = True
camera.brightness = 70
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
