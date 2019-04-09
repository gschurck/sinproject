#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Le Raspberry Pi affiche à l'écran ce que lui envoie l'Arduino 
# http://electroniqueamateur.blogspot.com/2014/05/communication-par-usb-entre-raspberry.html
import time

import serial


ser = serial.Serial('/dev/ttyACM0', 9600,timeout=20)
while 1 :
    print(ser.readline())#python 2.7.15
    ch = ser.readline()
    print(ch[14:16])
    H=(ch[14:16])
    #b=int.from.bytes(b'\ 27')
    #print(bytes([27]))
    print("H=", H)
    #S=H+2
    print("H")
    print(int.from_bytes(b'\x27', "big", signed=True))

    y = int(H.decode()) # decode is a method on the bytes class that returns a string
    type(y)
    print(y)
    # <class 'int'>
    """
    x = b'27'

    y = int(x.decode()) # decode is a method on the bytes class that returns a string
    type(y)
    # <class 'int'>

######################################

    y = int(b'27')
    type(y)
    # <class 'int'>
    """