import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234")

print(mydb)
if mydb:
    print("Conection Established")
else:
    print("Connection Not Established")

mycursor = mydb.cursor()
#Create the database
mycursor.execute("CREATE DATABASE newDB")
# To see all the existing databases>
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
