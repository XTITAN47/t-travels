from tkinter import messagebox
import mysql.connector
from database import *

from database import pushDBtoDAT

PASS = 'Titan@1067'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASS,  database='titan_travels'
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

def checkDatabaseExists():
    cu = mydb.cursor()
    data = cu.execute('SHOW DATABASES;')
    result = cu.fetchall()
    for i in result:
        if 'titan_travels' in i:
            return True
    return False

def DatabaseDoesNotExist():
    cu = mydb.cursor()
    cu.execute('CREATE DATABASE titan_travels;')
    cu.execute('use titan_travels;')
    cu.execute('CREATE TABLE users (user varchar(10),contact varchar(11),email varchar(255),psw varchar(255),adminstat varchar(255),primary key(user));')
    cu.execute('CREATE TABLE aeroplanes (flightid varchar(10),flightname varchar(255),departure varchar(255),destination varchar(255),primary key(flightid));')
    cu.execute('CREATE TABLE hotels (hotelid varchar(10),hotelname varchar(255),address varchar(11),family varchar(255), single varchar(255),doubleBed varchar(255),checkin varchar(255), checkout varchar(255),primary key(hotelid));')
    cu.execute('CREATE TABLE buses (busid varchar(10),departure varchar(255),destination varchar(255),primary key(busid));')
    cu.execute('CREATE TABLE trains (trainid varchar(10),trainname varchar(255),departure varchar(11),destination varchar(255),primary key(trainid));')
    cu.execute('CREATE TABLE airtickets (airticketid varchar(10),user varchar(10),flightno varchar(10),username varchar(255), flightname varchar(255),departure varchar(255),destination varchar(255),price int(11),primary key(airticketid));')
    cu.execute('create table hoteltickets(hotelticketid varchar(10), user varchar(10), hotelid varchar(10), fname varchar(255), hotelname varchar(255), city varchar(255), roomtype varchar(255), checkin varchar(255), checkout varchar(255), price varchar(255), primary key(hotelticketid));')
    cu.execute('CREATE TABLE bustickets (busticketid varchar(10),user varchar(10),busid varchar(10),username varchar(255),departure varchar(255),destination varchar(255),price int(11),primary key(busticketid));')
    cu.execute('CREATE TABLE traintickets (trainticketid varchar(10),user varchar(10),trainid varchar(10),username varchar(255),trainname varchar(255),departure varchar(255),destination varchar(255),price int(11),primary key(trainticketid));')
    cu.execute('CREATE TABLE reviews (reviewid varchar(10),user varchar(10),username varchar(255),review varchar(255),primary key(reviewid));')
    sql = "INSERT INTO users (user, contact,email,psw,adminstat) VALUES (%s, %s,%s,%s, %s)"
    val = ("titan","123","titan@titan.com",'admin', 'True')
    cu.execute(sql, val)
    mydb.commit()
    
def authenticateReg(a):
    cu = mydb.cursor()
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
        messagebox.showinfo(title="Account Created!",message="Success!")

        return 1

def authenticateLogin(user,password):
    cu = mydb.cursor()
    cu.execute('select * from users;')
    data = cu.fetchall()
    for x in data:
        if x[0] == user and x[3] == password:
            if x[4] == 'True':
                return 2
            messagebox.showinfo(title="Success!",message="Logging in!")
            return 1      
    messagebox.showinfo(title="Error!",message="Please check username or password!")



if __name__ =='__main__':
    print(checkDatabaseExists())
    if checkDatabaseExists == False:
        DatabaseDoesNotExist()
    
