from turtle import width
import mysql.connector
from tkinter import *
from tkinter.font import Font
import os

def Review(user,fname):
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
    def submitreview():
        r = rv.get()
        sql = "INSERT INTO reviews VALUES (%s, %s,%s,%s);"
        val = (id,user,fname,r)
        cu.execute(sql, val)
        mydb.commit()
        w.destroy()
        return 1

    id = givrvid()
    w = Tk()
    w.geometry("400x200")
    w.config(bg="#262626")
    w.title("Review")
    w.resizable(0,0)

    rv = StringVar()

    bigfont3= Font(family="arial",
            size=15,
            weight="bold")
    bigfont4= Font(family="arial",
            size=15)
    f=Frame(w,width=400,height=200)
    f.place(x=0,y=0)
    label12=Label(f,text="Your Review",font=bigfont3,width=33)
    label12.place(x=0,y=0)
    
    t = Entry(f, width=60,font=bigfont4,textvariable=rv)
    t.place(x=0,y=30,height=168)

    button = Button(f, text="Submit",command=submitreview)
    button.place(x=170,y=150)

    
    w.mainloop()
if __name__ == '__main__':
    Review('anonymous','anonymous')