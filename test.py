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
        print(ch[14:16])
        H=(ch[14:16])
    
    #b=int.from.bytes(b'\ 27')
    #print(bytes([27]))
    print("H=", H)
    #S=H+2
    print("H")


    # <class 'int'>

    
    
    mydb = mysql.connector.connect(host='localhost',
                             database='arduino',
                             user='root',
                             password='password')
    
    mycursor = mydb.cursor()



    sql = "INSERT INTO valeurs (temperature, humidity) VALUES (%s, %s)"

    val = [
      ('0', y),
      ('20', y),
      ('80', y),
     
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")



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