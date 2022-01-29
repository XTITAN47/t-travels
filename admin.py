from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from turtle import left
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Titan@1067",
  database = 'titan_travels'
)
cu = mydb.cursor()

def Home():
    def logout():
        home.destroy()
        pass
    def showusers():
        print('showusers')
        treev = ttk.Treeview(frame25, selectmode ='browse')
        treev.pack(side='left')
        verscrlbar = ttk.Scrollbar(frame25,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 90)
        treev.column("2", width = 90)
        treev.column("3", width = 90)
        treev.column('4',width=90)
        treev.heading("1", text ="UserID")
        treev.heading("2", text ="Contact")
        treev.heading("3", text ="Email")
        treev.heading("4", text ="Admin Status")
        cu.execute('select * from users;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[4]))


    def showflights():
        print('showflights')
        treev = ttk.Treeview(frame25, selectmode ='browse')
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(frame25,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 90)
        treev.column("2", width = 90)
        treev.column("3", width = 90)
        treev.column('4',width=90)
        treev.heading("1", text ="AirplaneNo")
        treev.heading("2", text ="AirplaneName")
        treev.heading("3", text ="Departure")
        treev.heading("4", text ="Destination")
        cu.execute('select * from aeroplanes;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[4]))

    def showbuses():
        print('showbuses')
        treev = ttk.Treeview(frame25, selectmode ='browse')
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(frame25,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        treev["columns"] = ("1", "2", "3")
        treev['show'] = 'headings'
        treev.column("1", width = 90)
        treev.column("2", width = 90)
        treev.column("3", width = 90)
        treev.heading("1", text ="BusID")
        treev.heading("2", text ="Departure")
        treev.heading("3", text ="Destination")
        cu.execute('select * from buses;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[3]))
        pass

    def showtrains():
        treev = ttk.Treeview(frame25, selectmode ='browse')
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(frame25,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 90)
        treev.column("2", width = 90)
        treev.column("3", width = 90)
        treev.column('4',width=90)
        treev.heading("1", text ="TrainID")
        treev.heading("2", text ="TrainName")
        treev.heading("3", text ="Departure")
        treev.heading("4", text ="Destination")
        cu.execute('select * from trains;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[3]))
        print('showtrains')
        pass

    def showhotels():
        treev = ttk.Treeview(frame25, selectmode ='browse')
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(frame25,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 90)
        treev.column("2", width = 90)
        treev.column("3", width = 90)
        treev.column('4',width=90)
        treev.heading("1", text ="HotelID")
        treev.heading("2", text ="HotelName")
        treev.heading("3", text ="Address")
        treev.heading("4", text ="Rooms")
        cu.execute('select * from hotels;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[3]))
        print('showhotels')
        pass

    def showreviews():
        treev = ttk.Treeview(frame25, selectmode ='browse')
        treev.pack(side ='left')
        verscrlbar = ttk.Scrollbar(frame25,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        treev.configure(xscrollcommand = verscrlbar.set)
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 90)
        treev.column("2", width = 90)
        treev.column("3", width = 90)
        treev.column('4',width=90)
        treev.heading("1", text ="ReviewID")
        treev.heading("2", text ="UserID")
        treev.heading("3", text ="Name")
        treev.heading("4", text ="Review")
        cu.execute('select * from reviews;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[3]))
        print('showreviews')
        pass
    print('admin')
    home=Tk()
    home.geometry("1280x720")
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
    frame25=Frame(frame24,width=900,height=520,highlightbackground="black",highlightthickness=1)
    frame25.place(x=0,y=0)


    
    
    l3=Label(frame21,text="Admin Panel",font=bigfont,bg="#4b2aa1",fg="white").place(x=250,y=10)

    
    button = Button(frame23, text="Users",command=showusers)
    img1 = PhotoImage(file=r"static\button_users.gif")
    button.config(image=img1)
    button.place(x=0,y=0)

    button2 = Button(frame23, text="Flights",command=showflights)
    img2 = PhotoImage(file=r"static\button_flights.gif")
    button2.config(image=img2)
    button2.place(x=168,y=0)
    
    button3 = Button(frame23, text="Buses",command=showbuses)
    img3 = PhotoImage(file=r"static\button_buses.gif")
    button3.config(image=img3)
    button3.place(x=349,y=0)

    button4 = Button(frame23, text="Trains",command=showtrains)
    img4 = PhotoImage(file=r"static\button_trains.gif")
    button4.config(image=img4)
    button4.place(x=519,y=0)

    button5 = Button(frame23, text="Hotels",command=showhotels)
    img5 = PhotoImage(file=r"static\button_hotels.gif")
    button5.config(image=img5)
    button5.place(x=697,y=0)

    button6 = Button(frame23, text="Reviews",command=showreviews)
    img6 = PhotoImage(file=r"static\button_reviews.gif")
    button6.config(image=img6)
    button6.place(x=875,y=0)

    button7 = Button(frame23, text='Logout',command=logout)
    img7 = PhotoImage(file=r"static\button_log-out.gif")
    button7.config(image=img7)
    button7.place(x=1074,y=0)

    home.mainloop()
    


if __name__ == '__main__':
    Home()