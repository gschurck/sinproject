#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Le Raspberry Pi affiche à l'écran ce que lui envoie l'Arduino 
# http://electroniqueamateur.blogspot.com/2014/05/communication-par-usb-entre-raspberry.html
import time

import serial
import mysql.connector



ser = serial.Serial('/dev/ttyACM0', 9600,timeout=20)
while 1 :
    while 1 :
        print(ser.readline())#python 2.7.15
        ch = ser.readline()
        H=(ch[4:6])
        if ch[0:1] == b'T':
            T=ch[5:7]
            print(T)
            Tint = int(T)
            type(Tint)
            # <class 'int'>
            print(Tint)

        elif ch[0:1] == b'H':
            H=ch[4:6]
            print(H)
            Hint = float(H)
            type(Hint)
            # <class 'int'>
            print(Hint)
        
"""

y = int(x)
type(y)

# <class 'int'>
"""


    
"""   
    mydb = mysql.connector.connect(host='localhost',
                             database='arduino',
                             user='root',
                             password='password')
    
    mycursor = mydb.cursor()



    sql = "INSERT INTO valeurs (temperature, humidity) VALUES (%s, %s)"

    val = [
      (Tint, Hint)
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")

    """
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

import os
import shutil

os.rename("home/pi/image.jpg", "/var/www/html/image.jpg")
shutil.move("home/pi/image.jpg", "/var/www/html/image.jpg")