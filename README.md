# Capturing a photo automatically every thirty minutes and transmit it via LINE. And it will shutdown after done with capturing specific pieces photos.

### Device Requirement:

**1. Raspberry Pi3 B+ or Raspberry Pi Zero W**

**2. 8MP Raspberry Pi NoIR Camera Module(v2)**

**3. Official Case for Raspberry Pi Zero W (Selective)**

**4. Mobile phone with LINE Instant Message(IM)**


### STEPs:

**1. `$sudo apt-get update`<br/>
     `$sudo apt-get intall python-picamera python3-picamera`<br/>
     or`$sudo pip install picamera`**<br/>

**2. [Apply for LINE Token(LINE Notify API Document)](https://notify-bot.line.me/zh_TW/)**

**3. Create a python program "pi3_picamera_gif_test2.py"**

**4. The last step is that: `$sudo nano ~/.config/lxsession/LXDE-pi/autostart` Then add a line of script: `@sh /home/pi/pi3camera/pi3_picamera_gif_test2.py`**

**5. Finally, restart your Raspberry Pi Zero W to test the working status of this function.  `$sudo reboot`**

**6. This function shows like this:**
![image](picture or gif url)
ex:![image](https://github.com/stephyang/CarouSell-test/blob/master/CarouSell-test-login.gif)


### Reference:

**1.[How To Send A Captured Image Through Email Using Raspberry Pi, Pi Camera, And Python](https://www.c-sharpcorner.com/article/how-to-send-the-captured-an-image-through-the-mail-using-raspberry-pi-and-python/)
<br/>
2.[picamera__official website](https://picamera.readthedocs.io/en/release-1.10/api_camera.html)
<br/>
3.[HOW TO STREAM THE PICAMERA TO YOUR BROWSER](https://desertbot.io/blog/how-to-stream-the-picamera)
<br/>
4.<http://pythonorz.blogspot.com/2017/12/python-line-notify-line-notify-line.html>
<br/>
5.<http://pythonorz.blogspot.com/2017/12/python-line-notify_18.html> **
<br/>