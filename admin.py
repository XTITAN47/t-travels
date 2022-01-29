from tkinter import *
from tkinter.font import Font
from tkinter import ttk
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
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 100)
        treev.column("2", width = 100)
        treev.column("3", width = 100)
        treev.column('4',width=100)
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
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 100)
        treev.column("2", width = 100)
        treev.column("3", width = 100)
        treev.column('4',width=100)
        treev.heading("1", text ="AirplaneNo")
        treev.heading("2", text ="AirplaneName")
        treev.heading("3", text ="Departure")
        treev.heading("4", text ="Destination")
        cu.execute('select * from aeroplanes;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[3]))

    def showbuses():
        treev["columns"] = ("1", "2", "3")
        treev['show'] = 'headings'
        treev.column("1", width = 100)
        treev.column("2", width = 150)
        treev.column("3", width = 150)
        treev.heading("1", text ="BusID")
        treev.heading("2", text ="Departure")
        treev.heading("3", text ="Destination")
        cu.execute('select * from buses;')
        data = cu.fetchall()
        c = 0
        for i in data:
            c +=1
            treev.insert("", 'end', text ="L{c}", values =(i[0], i[1], i[2], i[3]))

    def showtrains():
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 100)
        treev.column("2", width = 100)
        treev.column("3", width = 100)
        treev.column('4',width=100)
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

    def showhotels():
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 100)
        treev.column("2", width = 100)
        treev.column("3", width = 100)
        treev.column('4',width=100)
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

    def showreviews():
        treev["columns"] = ("1", "2", "3",'4')
        treev['show'] = 'headings'
        treev.column("1", width = 100)
        treev.column("2", width = 100)
        treev.column("3", width = 100)
        treev.column('4',width=100)
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

    frame1=Frame(home,width=1270,height=710,bg='black',highlightbackground="black",highlightthickness=5)
    frame1.place(x=0,y=0)
    frame2=Frame(frame1,width=1270,height=80,highlightbackground="black",bg="#4b2aa1",highlightthickness=1)
    frame2.grid(row=0,column=0)
    l3=Label(frame2,text="Admin Panel",font=bigfont,bg="#4b2aa1",fg="white")
    l3.place(x=520,y=10)

    frame3=Frame(frame1,width=1270,height=630,highlightbackground="black",bg='black',highlightthickness=1)
    frame3.grid(row=1,column=0)

    frame4=Frame(frame3,width=800,height=630,bg='green',highlightbackground="black",highlightthickness=1)
    frame4.grid(row=0,column=0)

    frame5=Frame(frame3,width=470,height=630,bg='blue',highlightbackground="black",highlightthickness=1)
    frame5.grid(row=0,column=1)

    frame6=Frame(frame4,width=800,height=630,bg='green',highlightbackground="black",highlightthickness=1)
    frame6.grid(row=0,column=0)

    treev = ttk.Treeview(frame6, selectmode ='browse')
    treev.pack(fill='both',expand=True)
    verscrlbar = ttk.Scrollbar(frame6,
                                orient ="vertical",
                                command = treev.yview)
    verscrlbar.pack(side ='right', fill ='x')
    treev.configure(xscrollcommand = verscrlbar.set)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 20))
    horscrlbar = ttk.Scrollbar(frame6,
                            orient ="horizontal",
                            command = treev.xview)
    horscrlbar.pack( fill ='y')
    treev.configure(yscrollcommand = horscrlbar.set)





    
    button = Button(frame3, text="Users",command=showusers)
    img1 = PhotoImage(file=r"static\button_users.gif")
    button.config(image=img1)
    button.place(x=0,y=0)

    button2 = Button(frame3, text="Flights",command=showflights)
    img2 = PhotoImage(file=r"static\button_flights.gif")
    button2.config(image=img2)
    button2.place(x=168,y=0)
    
    button3 = Button(frame3, text="Buses",command=showbuses)
    img3 = PhotoImage(file=r"static\button_buses.gif")
    button3.config(image=img3)
    button3.place(x=349,y=0)

    button4 = Button(frame3, text="Trains",command=showtrains)
    img4 = PhotoImage(file=r"static\button_trains.gif")
    button4.config(image=img4)
    button4.place(x=519,y=0)

    button5 = Button(frame3, text="Hotels",command=showhotels)
    img5 = PhotoImage(file=r"static\button_hotels.gif")
    button5.config(image=img5)
    button5.place(x=697,y=0)

    button6 = Button(frame3, text="Reviews",command=showreviews)
    img6 = PhotoImage(file=r"static\button_reviews.gif")
    button6.config(image=img6)
    button6.place(x=875,y=0)

    button7 = Button(frame3, text='Logout',command=logout)
    img7 = PhotoImage(file=r"static\button_log-out.gif")
    button7.config(image=img7)
    button7.place(x=1074,y=0)

    home.mainloop()
    


if __name__ == '__main__':
    Home()
