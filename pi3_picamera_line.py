#!/usr/bin/env python3

#refer to https://projects.raspberrypi.org/en/projects/timelapse-setup
from picamera import PiCamera
from os import system
from time import sleep
import time
import os
#import lineTool #added by R.L.at 2019/5/16
import datetime #added by R.L.at 2019/5/16
import subprocess  #added by R.L.at 2019/5/16 for ip...
import requests, os  #added by R.L.at 2019/5/16
#Above is added by R.L.at 2019/5/16

camera = PiCamera()
camera.resolution = (640, 480)
#camera.rotate = 180
#camera.resolution = (1920, 1080) # didn't work with LINE, commented by R.L. at 20190519
#camera.framerate = 15  # simultaneously exists with 1920x1080 definition
#camera.resolution = (60, 60) # the minimum definition
#camera.resolution = (2592, 1944) # the maximum definition
#camera.framerate = 15  # simultaneously exists with the maximum definition
print('Rest for 60 seconds for settling down...') #Rest for 60 seconds for settling down, added by R.L. at 20190519
sleep(5) #Rest for 60 seconds for settling down, added by R.L. at 20190519

i=1
x=100 #TTL photos to capture
n=60 #interval between capturing photo
print('camera capturing...')
for i in range(x): #****Don't less than 10   #for i in range(10):
    #added by R.L.at 2019/5/16
    def lineNotify(token, msg, picURI):
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + token
        }
    
        payload = {'message': msg}
        files = {'imageFile': open(picURI, 'rb')}
        r = requests.post(url, headers = headers, params = payload, files = files)
        return r.status_code
     #Above is added by R.L.at 2019/5/16
 
    camera.start_preview() #added by R.L. at 20190504
    camera.awb_mode = "auto"  #off,auto,sunlight,cloudy,shade,tungsten,fluorescent,incandescent,flash,horizon
    camera.exposure_mode = "auto" #off, auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
    sleep(5) #added by R.L. at 20190504
    timenow = (time.strftime("%y-%b-%d_%H:%M:%S"))
    #camera.capture('/home/pi/picamera_file/image{0:04d}.jpg'.format(i))
    #camera.capture("/home/pi/picamera_file/"+timenow+".jpg".format(i))
    camera.capture("/home/pi/picamera_file_dontmove/"+timenow+".jpg".format(i))
    #print("/home/pi/picamera_file/"+timenow+".jpg")
    print("/home/pi/picamera_file_dontmove/"+timenow+".jpg")
    
    #Below is added by R.L.at 2019/5/16
    token = "your token"
    #Below is added by R.L.at 2019/5/17
    TurnOn_message = "\nHello Python, this is from Raspberry Pi Zero W. \n Pi Zero W IP: "
    ip = subprocess.check_output(['hostname', '-I']) 
    ip_message = subprocess.check_output(['hostname', '-I']) 
    void_message ="\n"
    Time_message0="Now is: "
    Time_message = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    Photo_message ="\nThis is the "+str(i)+"/"+str(x)+" photo. Interval: "+str(n)+" seconds"
    mmsg = ''
    time.sleep(5)    
    msg = TurnOn_message+ ip_message+ Time_message0+ Time_message+ Photo_message
    #Above is added by R.L.at 2019/5/17 

    #picURI = '/home/pi/picamera_file/'+str(timenow)+'.jpg'
    picURI = '/home/pi/picamera_file_dontmove/'+str(timenow)+'.jpg'
    
    print(picURI)
    lineNotify(token, msg, picURI)
    print("Send a file to Line successfully") #added by R.L at 2019/5/11
    #Above is added by R.L.at 2019/5/16
    sleep(n) #every shot interval  #revised by R.L. at 20190504
#system('convert -delay 10 -loop 0 /home/pi/picamera_file/image*.jpg /home/pi/picamera_file/animation.gif')
print("capturing done")
print("Exit the program...")
print("sudo shutdown now -h")
def lineNotify(token, msg, picURI):
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + token
        }
    
        payload = {'message': msg}
        files = {'imageFile': open(picURI, 'rb')}
        r = requests.post(url, headers = headers, params = payload, files = files)
        return r.status_code
     #Above is added by R.L.at 2019/5/16
#Below is added by R.L.at 2019/5/16
token = "Your token"
msg = "Bye Bye Python, we are gonna shutdown now -h, this is from Raspberry Pi Zero W."
picURI = '/home/pi/image.jpg'
lineNotify(token, msg, picURI)
#Above is added by R.L.at 2019/5/16
os.system("lxterminal -e sudo shutdown now -h")
