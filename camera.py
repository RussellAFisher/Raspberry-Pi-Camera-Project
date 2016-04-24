import picamera
import os
import RPi.GPIO as GPIO
from datetime import datetime

camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
while True:
    d = datetime.now()
    saveFile = '/media/pi/6A5B-D5451/'
    if GPIO.wait_for_edge(24, GPIO.FALLING):
        day = "%02d" % (d.day)
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)
        sec = "%02d" % (d.second)
        camera.hflip = True
        camera.vflip = True
        camera.brightness = 60
        camera.resolution = (640, 480)
        camera.start_preview ()
        camera.start_recording(str(saveFile) + str(hour) + '_' + str(mins) + '_' + str(sec) + '.h264')
        camera.wait_recording(15)
        camera.stop_recording()
        camera.stop_preview()
        print ("Saving file as" + hour + "_" + mins + "_" + sec)
        os.system('killall')
