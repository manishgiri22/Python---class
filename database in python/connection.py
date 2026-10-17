import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='',database='mmc')
mycursor=mydb.cursor()   # to make the sql suitable for the python to run 
print("connection establish successfully")
mysql="create database mmc"
mycursor.execute(mysql)
print("database creation successfully")