from turtle import width
import mysql.connector
from tkinter import *
from tkinter.font import Font
import os

def Review(user,fname,r):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Titan@1067",
        database='titan_travels')
    cu = mydb.cursor()
    def givrvid():
            cu.execute('SELECT * FROM reviews;')
            data = cu.fetchall()
            count = 0
            rvid = "RV" + str(count)
            for i in data:
                if i[0] == rvid:
                    count += 1
                    rvid = "RV" + str(count)
            print('ReviewID:',rvid)
            return rvid

    print('Review:',r)
    sql = "INSERT INTO reviews VALUES (%s, %s,%s,%s);"
    val = (givrvid(),user,fname,r)
    cu.execute(sql, val)
    mydb.commit()
if __name__ == '__main__':
    Review('anonymous','anonymous','noice')