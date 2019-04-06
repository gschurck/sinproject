#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Le Raspberry Pi affiche à l'écran ce que lui envoie l'Arduino 
# http://electroniqueamateur.blogspot.com/2014/05/communication-par-usb-entre-raspberry.html
import time
##########################################
"""
import serial


#ser = serial.Serial('/dev/ttyACM0', 9600)
"""
##########################################

while 1 :
    #print(ser.readline())#python 2.7.15
    #ch = ser.readline()
    #print(ch)
    ch = "Temperature : 6"
    
   #"""
    if ch[0]=="T":  
        # SQL Temperature
        temperature=ch[14:15]
        print("Temperature :")
        #print(ch[5:7])
        print(temperature)
        time.sleep(1)
    elif ch[0]=="H":
        # SQL Humidity
        humidity=ch[5:7]
        print(ch[5:7])
        print("h")
    elif ch[0]=="b":
        # SQL Humidity
        humidity=ch[5:7]
        print(ch[5:7])
        print("b")
    #"""       
