import mysql.connector as mycon
mydb=mycon.connect(host='localhost',user='root',password='',database='mmc')
mycursor=mydb.cursor()
sql="update student set name=%s where roll=%s"
values=("manishaa",12)
mycursor.execute(sql,values)  #connected curor name mycursor.execute is used 
mydb.commit()
print("update data successfully")   