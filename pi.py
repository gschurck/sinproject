#!/usr/bin/python
# -*- coding: utf-8 -*-


import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
    message = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    ser.write(message)
    print(ser.readline())
    time.sleep(0.5)