
# Tuturial By Navin Reddy Telusko
'''
AIM : Connect database to Python.
created database in MYSQL and tables also created.
Now to connect any language to MYSQL we need a connector.
Install the connector using the following command in the cmnd prompt -
   " pip3 install mysql-connector "
Then import the connector as shown below.
'''

import mysql.connector

'''
The ip address is specified in the place of host if the server is in any other machine.
In our case the host is "localhost".
user we can use "root" or "alan".
Type in the password.
Also mention the name of the database we are exceuting the sql statements on.
'''

#Create a variable mydb
#Connect to the database server
mydb=mysql.connector.connect(host="localhost:3308",user="alan",passwd="1234",database="sakila")

#Create a cursor
#Cursor is like a pointer to point to something or a location.
myCursor=mydb.cursor()
# Connect is method and Cursor is an object.

#Now to execute any sql statemnt simply use the execute() method.
#Write the query to be executed as the arguement of the method.

myCursor.execute("show databases")
#This will store all the database names to the cursor object
#We dont be getting any print output for this.
#To get the print output use a for loop.
for i in myCursor:
    print(i)

# We can also fetch the data stored in cursor to a variable.
# We can then print the data from the variable as well.
result=myCursor.execute("SELECT * FROM actor")
for j in result:
    print(i)
