import time
import os
import serial
import sys
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO 
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

while (1):
	print('reading...')
	start = ser.readline(1)
	if (start == 'h'):
		ayu = Popen(['omxplayer','/boot/menu/ayu.mp4'], stdin=subprocess.PIPE)
		time.sleep(13)
		ayu.stdin.write('q')
		lan = Popen(['omxplayer','/boot/menu/lang.mp4'], stdin=subprocess.PIPE)
		while (1):
                                        lang = ser.readline(1)
                                        if (lang == 'a'):
                                                lan.stdin.write('q')
                                                aa = Popen(['omxplayer','/boot/menu/1e.mp4'], stdin=subprocess.PIPE)
                                                while (1):
                                                        wht = ser.readline(1)
                                                        if (wht == 'a'):
                                                                aa.stdin.write('q')
                                                                bb = Popen(['omxplayer','/boot/menu/2e.mp4'], stdin=subprocess.PIPE)
                                                                while (1):
                                                                        z =ser.readline(1)
                                                                        if (z == 'c'):
                                                                                bb.stdin.write('q')
                                                                                ser.write('f')
                                                                                cc = Popen(['omxplayer','--loop','/boot/menu/3e.mp4'], stdin=subprocess.PIPE)
                                                                                GPIO.output(21,True)
                                                                                time.sleep(0.5)
                                                                                GPIO.output(21,False)
                                                                                while (1):
                                                                                        zz = ser.readline(1)
                                                                                        if (zz == 'e'):
                                                                                                cc.stdin.write('q')
                                                                                                arrived = Popen(['omxplayer','/boot/menu/4e.mp4'],stdin=subprocess.PIPE)
                                                                                                time.sleep(13)
												break
                                                                                arrived.stdin.write('q')
                                                                                break
								break
						break
                                        elif (lang == 'b'):
                                                lan.stdin.write('q')
                                                smenu = Popen(['omxplayer','/boot/menu/1s.mp4'], stdin=subprocess.PIPE)
                                                while(1):
                                                        mokak = ser.readline(1)
                                                        if (mokak == 'a'):
                                                                smenu.stdin.write('q')
                                                                bb = Popen(['omxplayer','/boot/menu/2s.mp4'], stdin=subprocess.PIPE)
                                                                while (1):
                                                                        z =ser.readline(1)
                                                                        if (z == 'c'):
                                                                                bb.stdin.write('q')
                                                                                cc = Popen(['omxplayer','--loop','/boot/menu/3s.mp4'], stdin=subprocess.PIPE)
                                                                                GPIO.output(21,True)
                                                                                time.sleep(0.5)
                                                                                GPIO.output(21,False)
                                                                                while (1):
                                                                                        zz = ser.readline(1)
                                                                                        if (zz == 'e'):
                                                                                                cc.stdin.write('q')
                                                                                                arrived = Popen(['omxplayer','/boot/menu/4s.mp4'],stdin=subprocess.PIPE)
                                                                                                time.sleep(13)
												break
                                                                                arrived.stdin.write('q')
                                                                                break
								break
						break
                                        elif (lang == 'c'):
                                                lan.stdin.write('q')
                                                smenu = Popen(['omxplayer','/boot/menu/1s.mp4'], stdin=subprocess.PIPE)
                                                while(1):
                                                        mokak = ser.readline(1)
                                                        if (mokak == 'a'):
                                                                smenu.stdin.write('q')
                                                                bb = Popen(['omxplayer','/boot/menu/2s.mp4'], stdin=subprocess.PIPE)
                                                                while (1):
                                                                        z =ser.readline(1)
                                                                        if (z == 'c'):
                                                                                bb.stdin.write('q')
                                                                                cc = Popen(['omxplayer','--loop','/boot/menu/3s.mp4'], stdin=subprocess.PIPE)
                                                                                GPIO.output(21,True)
                                                                                time.sleep(0.5)
                                                                                GPIO.output(21,False)
                                                                                while (1):
                                                                                        zz = ser.readline(1)
                                                                                        if (zz == 'e'):
                                                                                                cc.stdin.write('q')
                                                                                                arrived = Popen(['omxplayer','/boot/menu/4s.mp4'],stdin=subprocess.PIPE)
                                                                                                time.sleep(13)
												break
                                                                                arrived.stdin.write('q')
                                                                                break
								break
						break
	time.sleep(1)
