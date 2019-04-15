import mysql.connector
import time

mydb = mysql.connector.connect(host='localhost',
                         database='arduino',
                         user='root',
                         password='password')

mycursor = mydb.cursor()

Tint=0
Hint=2

localtime = time.asctime( time.localtime(time.time()) )

while 1:
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime)
    sql = "INSERT INTO valeurs (temperature, humidity, time) VALUES (%s, %s, %s);"
    
    val = (Tint, Hint , localtime)


    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")
    Tint += 2
    Hint += 2
    
    
"""

    val = [
      (Tint, Hint , localtime)
    ]
"""