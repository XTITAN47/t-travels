from distutils import command
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from turtle import left
import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="titan@1067",database="titan_travels")
cu = mydb.cursor()

def Home():
    def logout():
        home.destroy()
        pass
    
    udta=["S.No","UserID","Contact","Email","Admin Status"]
    uwd=[70,200,200,200,200]
    fldta=["Flightid","Flightname","Departure","Destination"]
    fwd=[100,200,200,200]
    busdta=["BusId","Departure","Destination"]
    buswd=[100,200,200]
    trdta=["TrainId","Trainname","Departure","Destination"]
    trwd=[100,200,200,200]
    htldta=["hotelid","hotelname","address","rooms_available"]
    htlwd=[100,200,200,200]
    rvdta=["ReviewId","UserId","Username","Review"]
    rvwd=[100,200,200,200]
    
    def treetbl(x,y,z):
        s=ttk.Style() ; s.theme_use("clam")
        tbfr=Frame(frame24,border=0)
        tbfr.place(x=0,y=0,width=800,height=300)

        tbl=ttk.Treeview(tbfr,show="headings",columns=tuple(y))
        for i in range(len(y)):
            tbl.column(y[i],width=z[i],minwidth=10,anchor=tk.CENTER)
            tbl.heading(y[i],text=y[i],anchor=tk.CENTER)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="titan@1067",database="titan_travels")
        c=mydb.cursor()
        c.execute("select * from "+x)
        if x=="users":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(count,i[0],i[1],i[2],i[4]))
                count=count+1

        elif x=="aeroplanes" or x=="trains" or x=="hotels" or x=="reviews":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(count,i[1],i[2],i[3]))
                count=count+1

        elif x=="buses":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(count,i[1],i[2]))
                count=count+1

        hsb=Scrollbar(tbfr,orient=HORIZONTAL)
        vsb=Scrollbar(tbfr,orient=VERTICAL)

        tbl.config(xscrollcommand=hsb.set)
        tbl.config(yscrollcommand=vsb.set)

        hsb.pack(fill=X,side=BOTTOM)
        hsb.config(command=tbl.xview)
        vsb.pack(fill=Y,side=RIGHT)
        vsb.config(command=tbl.yview)
        tbl.pack(fill=BOTH,expand=1)

    def usrs():
        treetbl("users",udta,uwd)
    def flt():
        treetbl("aeroplanes",fldta,fwd)
    def bus():
        treetbl("buses",busdta,buswd)
    def train():
        treetbl("trains",trdta,trwd)
    def hotel():
        treetbl("hotels",htldta,htlwd)
    def rev():
        treetbl("reviews",rvdta,rvwd)
    
    print('admin')
    home=Tk()
    home.geometry("1280x720+100+50")
    home.resizable(0,0)
    home.title("Admin Panel")

    bigfont= Font(family="Valentine",
            size=30,
            weight="bold")

    bigfont2= Font(family="Valentine",
            size=25,
            weight="bold")

    frame21=Frame(home,width=800,height=100,highlightbackground="black",bg="#4b2aa1",highlightthickness=5)
    frame21.place(x=250,y=0)
    frame22=Frame(home,width=1272,height=605,highlightbackground="black",highlightthickness=1)
    frame22.place(x=4,y=110)
    frame23=Frame(frame22,width=1268,height=79,highlightbackground="black",highlightthickness=1)
    frame23.place(x=0,y=0)
    frame24=Frame(frame22,width=1272,height=520,highlightbackground="black",highlightthickness=1)
    frame24.place(x=-1,y=80)
    frame25=Frame(frame24,width=1272,height=100,highlightbackground="black",highlightthickness=1)
    frame25.place(x=10,y=400)
    frame26=Frame(frame24,width=450,height=400,bg="#66c2e3",highlightbackground="black",highlightthickness=4)
    frame26.place(x=800,y=0)

    l3=Label(frame21,text="Admin Panel",font=bigfont,bg="#4b2aa1",fg="white").place(x=250,y=10)

    
    button = Button(frame23, text="Users",command=usrs)
    img1 = PhotoImage(file=r"static\button_users.gif")
    button.config(image=img1)
    button.place(x=0,y=0)

    button2 = Button(frame23, text="Flights",command=flt)
    img2 = PhotoImage(file=r"static\button_flights.gif")
    button2.config(image=img2)
    button2.place(x=168,y=0)
    
    button3 = Button(frame23, text="Buses",command=bus)
    img3 = PhotoImage(file=r"static\button_buses.gif")
    button3.config(image=img3)
    button3.place(x=349,y=0)

    button4 = Button(frame23, text="Trains",command=train)
    img4 = PhotoImage(file=r"static\button_trains.gif")
    button4.config(image=img4)
    button4.place(x=519,y=0)

    button5 = Button(frame23, text="Hotels",command=hotel)
    img5 = PhotoImage(file=r"static\button_hotels.gif")
    button5.config(image=img5)
    button5.place(x=697,y=0)

    button6 = Button(frame23, text="Reviews",command=rev)
    img6 = PhotoImage(file=r"static\button_reviews.gif")
    button6.config(image=img6)
    button6.place(x=875,y=0)

    button7 = Button(frame23, text='Logout',command=logout)
    img7 = PhotoImage(file=r"static\button_log-out.gif")
    button7.config(image=img7)
    button7.place(x=1074,y=0)

    button8 = Button(frame25, text='ADD')
    img8 = PhotoImage(file=r"static\ADD.gif")
    button8.config(image=img8)
    button8.place(x=10,y=10)

    button9 = Button(frame25, text='UPDATE')
    img9 = PhotoImage(file=r"static\UPDATE.gif")
    button9.config(image=img9)
    button9.place(x=160,y=10)

    button10 = Button(frame25, text='DELETE')
    img10 = PhotoImage(file=r"static\DELETE.gif")
    button10.config(image=img10)
    button10.place(x=350,y=10)

    home.mainloop()

if __name__ == '__main__':
    Home()
