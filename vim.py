import mysql.connector

mydb = mysql.connector.connect(host="localhost",user= "root",passwd="titan@1067")

a= mydb.cursor()

a.execute("show databases")

for i in a:
    print(i)
