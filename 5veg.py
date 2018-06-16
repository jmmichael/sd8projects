import time
import picamera
with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.hflip = True

    camera.start_preview()
    camera.brightness = 50
    camera.contrast = 30
    try:
        for i, filename in enumerate(camera.capture_continuous('veg{counter:02d}.jpg')):
            print(filename)
            time.sleep(30)
            if i == 5:
                break
    finally:
        camera.stop_preview()
#taken from chap10
