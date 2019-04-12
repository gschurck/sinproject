import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                         database='arduino',
                         user='root',
                         password='password')

mycursor = mydb.cursor()

Tint=0
Hint=2
sql = "ALTER TABLE valeurs ADD timelog DATETIME()"

mydb.commit()
while 1:
    # sql = "INSERT INTO valeurs (temperature, humidity) VALUES (%s, %s)"
    
    
    """
    val = [
      (Tint, Hint)
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")
    Tint += 2
    Hint += 2
    """