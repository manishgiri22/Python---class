import mysql.connector  as cond
mydb=cond.connect(host='localhost',user='root',password='',database='mmc')
mycursor=mydb.cursor()
# sql="create table student(roll int primary key, name varchar(40),address varchar(50))"
# mycursor.execute(sql)
print("table creation successfully")
'''insertsql="insert into student(roll,name,address) values(%s,%s,%s)"
values=(13,"manish","btm")
mycursor.execute(insertsql,values)
mydb.commit()''' # from execution you should commit to the database each and every code of sql which you will write 
print("data insert successfully")


# insert multiple values in one time 
mysql="insert into student(roll,name,address) values(%s,%s,%s)"
value=[(12,'manish','btm'),(23,'rohan','ktm'),(24,'sohan','llt')]
mycursor.executemany(mysql,value)
mydb.commit()
print("insert mulitple values successfully")