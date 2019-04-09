import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                             database='arduino',
                             user='root',
                             password='password')

mycursor = mydb.cursor()



sql = "INSERT INTO valeurs (temperature, humidity) VALUES (%s, %s)"

val = [
  ('0', '5'),
  ('20', '50'),
  ('80', '40'),
 
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")