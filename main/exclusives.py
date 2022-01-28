from tkinter import messagebox
import mysql.connector
from database import *

from mainp.tanmay.database import pushDBtoDAT
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Titan@1067",
  database="Titan_Travels"
)

def validateUserReg(a):
    for i in range(5):
        if a[i] == "":
            messagebox.showinfo(title="Error!",message="Empty Form")
            return 0
    if a[3] != a[4]:
        messagebox.showinfo(title="Error!",message="Passwords do not MATCH")
        return 0
    return 1

def checkUserTableExists():
    cu = mydb.cursor()
    cu.execute('SHOW TABLES LIKE users')
    result = cu.fetchone()
    if result:
        return True
    else:
        return False
    
def authenticateReg(a):
    cu = mydb.cursor()
    cu.execute('CREATE DATABASE IF NOT EXISTS titan_travels;')
    if checkUserTableExists == False:
        cu.execute('CREATE TABLE users (user varchar(10),contact varchar(11),email varchar(255),psw varchar(255),primary key(user));')
    '''sql = "INSERT INTO users (user, contact,email,psw) VALUES (%s, %s,%s,%s)"
    val = ("titan","123","titan@titan.com",'admin')
    cu.execute(sql, val)
    mydb.commit()'''

    cu.execute('SELECT * FROM users;')
    data = cu.fetchall()
    for x in data:
        if x[0] == a[0] or x[1] == a[1] or x[3] == a[3]:
            messagebox.showinfo(title="Error!",message="Account Exists!")
            return 0
    else:
        sql = "INSERT INTO users (user, contact,email,psw) VALUES (%s, %s,%s,%s)"
        val = (a[0],a[1],a[2],a[3])
        cu.execute(sql, val)
        mydb.commit()
        pushDBtoDAT()
        return 1

def authenticateLogin(user,password):
    cu = mydb.cursor()
    cu.execute('select * from users;')
    data = cu.fetchall()
    for x in data:
        if x[0] == user and x[3] == password:
            messagebox.showinfo(title="Success!",message="Logging in!")
            return 1
    messagebox.showinfo(title="Error!",message="Please check username or password!")



if __name__ =='__main__':
    pass
    
