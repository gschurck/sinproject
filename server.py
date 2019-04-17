#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Le Raspberry Pi affiche à l'écran ce que lui envoie l'Arduino 
# http://electroniqueamateur.blogspot.com/2014/05/communication-par-usb-entre-raspberry.html
import time

import serial
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                             database='arduino',
                             user='root',
                             password='password')

mycursor = mydb.cursor()

ser = serial.Serial('/dev/ttyACM0', 9600,timeout=20)
while 1 :
    while 1 :
        print(ser.readline())#python 2.7.15
        ch = ser.readline()
        H=(ch[4:6])
        if ch[0:1] == b'H':
            T=ch[11:13]
            print(T)
            tint = int(ch[11:13])
            type(tint)
            # <class 'int'>
            print(tint)
            H=ch[4:6]
            print(H)
            hint = int(ch[4:6])
            type(hint)
            # <class 'int'>
            print(hint)
            #mycursor.execute("""select test_id from test_logs where id = %s """, (id,))
            sql = "INSERT INTO valeurs (temperature, humidity, time) VALUES (%s, %s, %s);"
            localtime = time.asctime( time.localtime(time.time()) )
            print(localtime)
            val = (tint, hint, localtime)

            mycursor.executemany(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "was inserted.")


        """
        elif ch[0:1] == b'H':
            H=ch[4:6]
            print(H)
            Hint = int(H)
            type(Hint)
            # <class 'int'>
            print(Hint)
        """

