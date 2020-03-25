#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os
import sys
import subprocess
from subprocess import Popen

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

state = True

while(1):
	if GPIO.input(17) == state:
		myprocess = Popen(['omxplayer','-b','/media/aayu/welcome.mp4'],stdin=subprocess.PIPE)
		time.sleep(13)
		myprocess.stdin.write('q')
