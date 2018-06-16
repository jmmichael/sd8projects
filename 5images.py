import time
import picamera
with picamera.PiCamera() as camera:
    camera.vflip = True
    camera.hflip = True

    camera.start_preview()
    try:
        for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
            print(filename)
            time.sleep(3000)
            if i == 5:
                break
    finally:
        camera.stop_preview()
#taken from chap10
