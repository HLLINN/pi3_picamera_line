#!/usr/bin/env python3

import datetime 
import time 
import os
import glob
import shutil


datefold = time.strftime("%Y-%m-%d", time.localtime())


# define the name of the directory to be created
newpath = "/home/pi/picamera_file/{}/".format(datefold)
print("newpath =%s" % newpath)

try:  
    os.makedirs(newpath)
except OSError:  
    print ("Creation of the directory %s failed" % newpath)
else:  
    print ("Successfully created the directory %s" % newpath)

time.sleep(10) 


source = '/home/pi/picamera_file/'
dest1 = newpath


files = os.listdir(source)

for f in files:
    if f.endswith('.jpg'):
        shutil.move(source+f, dest1)


          
print ("Have done with moving files to new directory %s " % newpath)
exit() #force to quit this python program
