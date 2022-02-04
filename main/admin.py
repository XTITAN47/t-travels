from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import tkinter as tk
import mysql.connector

PASS = 'Titan@1067'

mydb = mysql.connector.connect(host="localhost",user="root",password=PASS,database="titan_travels")
cu = mydb.cursor()

def Home():

    def logout():
        home.destroy()
        import project
        pass
    udta=["S.No","UserID","Contact","Email","Admin Status"]
    uwd=[70,200,200,200,200]
    fldta=["Flightid","Flightname","Departure","Destination"]
    fwd=[100,200,200,200]
    busdta=["BusId","Departure","Destination"]
    buswd=[100,200,200]
    trdta=["TrainId","Trainname","Departure","Destination"]
    trwd=[100,200,200,200]
    htldta=["hotelid","hotelname","city","family_rooms","single_rooms","double_rooms"]
    htlwd=[100,200,100,100,100,100]
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
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=PASS,database="titan_travels")
        c=mydb.cursor()
        c.execute("select * from "+x)
        if x=="users":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(count,i[0],i[1],i[2],i[4]))
                count=count+1

        elif x=="aeroplanes" or x=="trains" or x=="reviews":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(i[0],i[1],i[2],i[3]))
                count=count+1

        elif x=="buses":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(i[0],i[1],i[2]))
                count=count+1
        elif x=="hotels":
            count=1
            for i in c:
                tbl.insert('',count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
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
        
        def delete():
            m = tbl.selection()
            y = tbl.item(m,'values')
            for rec in m:
                tbl.delete(rec)
                mydb = mysql.connector.connect(host="localhost",user="root",password=PASS,database="titan_travels")
                cu = mydb.cursor()
                if x=='users':
                    s = ('delete from users where user=%s;')
                    v = (y[1],)
                    cu.execute(s,v)
                elif x=='aeroplanes':
                    s = ('delete from aeroplanes where flightid= %s;')
                    v = (y[0],)
                    cu.execute(s,v)
                elif x=='hotels':
                    s = ('delete from hotels where hotelid=%s;')
                    v = (y[0],)
                    cu.execute(s,v)
                elif x=='buses':
                    s = ('delete from buses where busid=%s;')
                    v = (y[0],)
                    cu.execute(s,v)
                elif x=='trains':
                    s = ('delete from trains where trainid=%s;')
                    v = (y[0],)
                    cu.execute(s,v)
                mydb.commit()
        button11 = Button(home, text='DELETE',command=delete)
        button11.place(x=20,y=598,width=200,height=90)



    def usrs():
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        v6 = StringVar()
        treetbl("users",udta,uwd)
        frame26=Frame(frame24,width=450,height=400,bg="#66c2e3",highlightbackground="black",highlightthickness=4)
        frame26.place(x=800,y=0)
        l0=Label(frame26,text="====DATABASE MANAGER====",font="arial 20 bold",bg="#66c2e3").place(x=0,y=1)
        l1=Label(frame26,text="USER ID:-",font="arial 15 bold",bg="#66c2e3").place(x=50,y=50)
        e1=Entry(frame26,textvariable=v1).place(x=250,y=53)
        l2=Label(frame26,text="CONTACT:-",font="arial 15 bold",bg="#66c2e3").place(x=50,y=100)
        e2=Entry(frame26,textvariable=v2).place(x=250,y=103)
        l4=Label(frame26,text="EMAIL:-",font="arial 15 bold",bg="#66c2e3").place(x=50,y=150)
        e4=Entry(frame26,textvariable=v3).place(x=250,y=153)
        l3=Label(frame26,text="PASSWORD:-",font="arial 15 bold",bg="#66c2e3").place(x=50,y=200)
        e3=Entry(frame26,textvariable=v4).place(x=250,y=203)
        l4=Label(frame26,text="CONFIRM:-",font="arial 15 bold",bg="#66c2e3").place(x=50,y=250)
        e4=Entry(frame26,textvariable=v5).place(x=250,y=253)
        l4 = Checkbutton(frame26,variable=v6, text = "ADMIN",bg="#66c2e3",onvalue = 'True',offvalue = 'False',height = 2,width = 10,font='arial 14 bold') 
        l4.place(x=250,y=303)
        l4.deselect()
        def add():
            a = v1.get()
            b = v2.get()
            c = v3.get()
            d = v4.get()
            e = v5.get()
            f = v6.get()
            if a != "" and b != "" and c != "" and d !="" and e != '' and f != '':
                if d == e:
                    sql = "INSERT INTO users VALUES (%s, %s,%s,%s,%s)"
                    val = (a,b,c,d,f)
                    cu.execute(sql, val)
                    mydb.commit()
                    print('ADDED USER')
        button8 = Button(frame26, text='ADD',command=add)
        button8.place(x=250,y=283)


    def flt():
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        treetbl("aeroplanes",fldta,fwd)
        frame27=Frame(frame24,width=450,height=400,bg="pink",highlightbackground="black",highlightthickness=4)
        frame27.place(x=800,y=0)
        l0=Label(frame27,text="====DATABASE MANAGER====",font="arial 20 bold",bg="pink").place(x=0,y=1)
        l1=Label(frame27,text="FLIGHT ID:-",font="arial 15 bold",bg="pink").place(x=50,y=50)
        e1=Entry(frame27,textvariable=v1).place(x=250,y=53)
        l2=Label(frame27,text="FLIGHT NAME:-",font="arial 15 bold",bg="pink").place(x=50,y=100)
        e2=Entry(frame27,textvariable=v2).place(x=250,y=103)
        l4=Label(frame27,text="DEPARTURE:-",font="arial 15 bold",bg="pink").place(x=50,y=150)
        e4=Entry(frame27,textvariable=v3).place(x=250,y=153)
        l3=Label(frame27,text="DESTINATION:-",font="arial 15 bold",bg="pink").place(x=50,y=200)
        e3=Entry(frame27,textvariable=v4).place(x=250,y=203)

        def add():
            a = v1.get()
            b = v2.get()
            c = v3.get()
            d = v4.get()
            if a != "" and b != "" and c != "" and d !="":
                sql = "INSERT INTO aeroplanes VALUES (%s, %s,%s,%s)"
                val = (a,b,c,d)
                cu.execute(sql, val)
                mydb.commit()
                print('ADDED FLIGHT')

        button8 = Button(frame27, text='ADD',command=add).place(x=250,y=253)



    def bus():
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        treetbl("buses",busdta,buswd)
        frame28=Frame(frame24,width=450,height=400,bg="#6ca2d4",highlightbackground="black",highlightthickness=4)
        frame28.place(x=800,y=0)
        l0=Label(frame28,text="====DATABASE MANAGER====",font="arial 20 bold",bg="#6ca2d4").place(x=0,y=1)
        l1=Label(frame28,text="BUS ID:-",font="arial 15 bold",bg="#6ca2d4").place(x=50,y=50)
        e1=Entry(frame28,textvariable=v1).place(x=250,y=53)
        l4=Label(frame28,text="DEPARTURE:-",font="arial 15 bold",bg="#6ca2d4").place(x=50,y=100)
        e4=Entry(frame28,textvariable=v2).place(x=250,y=103)
        l3=Label(frame28,text="DESTINATION:-",font="arial 15 bold",bg="#6ca2d4").place(x=50,y=150)
        e3=Entry(frame28,textvariable=v3).place(x=250,y=153)
        def add():
            a = v1.get()
            b = v2.get()
            c = v3.get()
            if a != "" and b != "" and c != "":
                    sql = "INSERT INTO buses VALUES (%s, %s,%s)"
                    val = (a,b,c)
                    cu.execute(sql, val)
                    mydb.commit()
                    print('ADDED BUS')
        button8 = Button(frame28, text='ADD',command=add).place(x=250,y=253)   


    def train():
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        treetbl("trains",trdta,trwd)
        frame29=Frame(frame24,width=450,height=400,bg="#d8f26d",highlightbackground="black",highlightthickness=4)
        frame29.place(x=800,y=0)
        l0=Label(frame29,text="====DATABASE MANAGER====",font="arial 20 bold",bg="#d8f26d").place(x=0,y=1)
        l1=Label(frame29,text="TRAIN ID:-",font="arial 15 bold",bg="#d8f26d").place(x=50,y=50)
        e1=Entry(frame29,textvariable=v1).place(x=250,y=53)
        l2=Label(frame29,text="TRAIN NAME:-",font="arial 15 bold",bg="#d8f26d").place(x=50,y=100)
        e2=Entry(frame29,textvariable=v2).place(x=250,y=103)
        l4=Label(frame29,text="DEPARTURE:-",font="arial 15 bold",bg="#d8f26d").place(x=50,y=150)
        e4=Entry(frame29,textvariable=v3).place(x=250,y=153)
        l3=Label(frame29,text="DESTINATION:-",font="arial 15 bold",bg="#d8f26d").place(x=50,y=200)
        e3=Entry(frame29,textvariable=v4).place(x=250,y=203)
        def add():
            a = v1.get()
            b = v2.get()
            c = v3.get()
            d = v4.get()
            if a != "" and b != "" and c != "" and d !="":
                    sql = "INSERT INTO trains VALUES (%s, %s,%s,%s)"
                    val = (a,b,c,d)
                    cu.execute(sql, val)
                    mydb.commit()
                    print('ADDED TRAIN')
        button8 = Button(frame29, text='ADD',command=add).place(x=250,y=253)

    def hotel():
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        v6 = StringVar()
        treetbl("hotels",htldta,htlwd)
        frame30=Frame(frame24,width=450,height=400,bg="#e69647",highlightbackground="black",highlightthickness=4)
        frame30.place(x=800,y=0)
        l0=Label(frame30,text="====DATABASE MANAGER====",font="arial 20 bold",bg="#e69647").place(x=0,y=1)
        l1=Label(frame30,text="HOTEL ID:-",font="arial 15 bold",bg="#e69647").place(x=50,y=50)
        e1=Entry(frame30,textvariable=v1).place(x=250,y=53)
        l2=Label(frame30,text="HOTEL NAME:-",font="arial 15 bold",bg="#e69647").place(x=50,y=100)
        e2=Entry(frame30,textvariable=v2).place(x=250,y=103)
        l4=Label(frame30,text="CITY:-",font="arial 15 bold",bg="#e69647").place(x=50,y=150)
        e4=Entry(frame30,textvariable=v3).place(x=250,y=153)
        l3=Label(frame30,text="FAMILY ROOMS:-",font="arial 15 bold",bg="#e69647").place(x=50,y=200)
        e3=Entry(frame30,textvariable=v4).place(x=250,y=203)
        l3=Label(frame30,text="SINGLE_BED ROOMS:-",font="arial 15 bold",bg="#e69647").place(x=50,y=250)
        e3=Entry(frame30,textvariable=v5).place(x=300,y=253)
        l3=Label(frame30,text="DOUBLE_BED ROOMS:-",font="arial 15 bold",bg="#e69647").place(x=50,y=300)
        e3=Entry(frame30,textvariable=v6).place(x=300,y=303)
        def add():
            a = v1.get()
            b = v2.get()
            c = v3.get()
            d = v4.get()
            e = v5.get()
            f = v6.get()
            if a != "" and b != "" and c != "" and d !="" and e != '' and f != '':
                    sql = "INSERT INTO hotels VALUES (%s, %s,%s,%s,%s,%s)"
                    val = (a,b,c,d,e,f)
                    cu.execute(sql, val)
                    mydb.commit()
                    print('ADDED HOTEL')
        button8 = Button(frame30, text='ADD',command=add).place(x=250,y=353)


    def rev():
        treetbl("reviews",rvdta,rvwd)
        frame31=Frame(frame24,width=450,height=400,bg="#9647e6",highlightbackground="black",highlightthickness=4)
        frame31.place(x=800,y=0)
    
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
    #======================================EDITING FRAME=======================================================================
    

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

    #button8 = Button(frame25, text='ADD')
    #img8 = PhotoImage(file=r"static\ADD.gif")
    #button8.config(image=img8)
    #button8.place(x=10,y=10)

    #button9 = Button(frame25, text='UPDATE')
    #img9 = PhotoImage(file=r"static\UPDATE.gif")
    #button9.config(image=img9)
    #button9.place(x=160,y=10)

    #button10 = Button(frame25, text='DELETE')
    #img10 = PhotoImage(file=r"static\DELETE.gif")
    #button10.config(image=img10)
    #button10.place(x=350,y=10)

    home.mainloop()

if __name__ == '__main__':
    Home()