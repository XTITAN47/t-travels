from tkinter import *
from tkinter import ttk
from tokenize import ContStr
from PIL import Image, ImageTk
from tkinter.font import Font
import mysql.connector
import random
from invoice import genFlightInvoice
from tkinter import messagebox
import review
PASS = 'Titan@1067'

def pay():
    i = random.randrange(5000,15001,1000)
    return i

def airticket():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASS,
    database='titan_travels')
    cu = mydb.cursor()
    cu.execute('SELECT * FROM airtickets;')
    data = cu.fetchall()
    count = 0
    ticketname = "AR" + str(count)
    for i in data:
        if i[0] == ticketname:
            count += 1
            ticketname = "AR" + str(count)
    return ticketname



def air(user):
    a=1
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASS,
    database='titan_travels')
    cu = mydb.cursor()
    cu.execute('SELECT * FROM AEROPLANES;')
    data = cu.fetchall()
    noOfAvFlights = 0
    departure=[""]
    destination=[""]
    flights=[]
    for i in data:
        noOfAvFlights +=1
        if i[2] not in departure:
            departure.append(i[2])
        if i[3] not in destination:
            destination.append(i[3])
        data = [i[0],i[1],i[2],i[3]]
        flights.append(data)
        print(i)

#================================================== SEARCH and DISPLAY ===================================================
    def search():
        def confirm():
            def makeinvoice():
                pm = int(p)
                gst = 0.18 * pm
                total = gst + pm
                gst = str(gst)
                total = str(total)
                try:
                    genFlightInvoice(airtktid,user,flightno,fname,flightname,a,b,str(p),gst,total)
                    messagebox.showinfo("File Downloaded", "Success!")
                except:
                    print('Error executing pdf...')
                    messagebox.showerror("Error", "Unable to load File")
                frame24.destroy()

            fname = name.get()
            if fname != "":
                airtktid=airticket()
                sql = "INSERT INTO airtickets VALUES (%s, %s,%s,%s,%s, %s,%s,%s)"
                val = (airtktid,user,flightno,fname,flightname,a,b,p)
                cu.execute(sql, val)
                mydb.commit()
                frame23.destroy()
                frame24=Frame(airwin,width=900,height=300,bg='green',highlightbackground="black",highlightthickness=2)
                frame24.place(x=200,y=305)
                l1=Label(frame24,text=f"You Have Successfully Booked Flight {flightname}",font=bigfont3)
                l2=Label(frame24,text=f"Happy Journey!",font=bigfont3)
                button6=Button(frame24,text="Download Invoice",command=makeinvoice,width=50,padx=275)
                l1.grid(row=1,column=1)
                l2.grid(row=2,column=1)
                button6.grid(row=3,column=1,sticky=W)
                
                rv = StringVar()
                bigfont4= Font(family="arial",
                        size=15)
                f=Frame(frame24,width=400,height=200,pady=40)
                f.grid(row=4,column=1)
                label12=Label(f,text="Your Review",font=bigfont3,width=33)
                label12.grid(row=1,column=1)
                t = Entry(f, width=60,font=bigfont4,textvariable=rv)
                t.grid(row=2,column=1)
                def submitreview():
                    r = rv.get()
                    review.Review(user,fname,r)
                    f.destroy()
                    f2=Frame(frame24,width=400,height=200)
                    f2.grid(row=4,column=1)
                    label12=Label(f2,text="Thanks for the review!",font=bigfont3,width=33)
                    label12.grid(row=1,column=1)

                button = Button(f, text="Submit",command=submitreview)
                button.grid(row=3,column=1)
                

        a= var1.get()
        b= var2.get()
        p = pay()
        if a != b and (a and b)!="":
            for i in flights:
                if i[2] == a and  i[3] == b:
                    flightno = i[0]
                    flightname = i[1]
            name = StringVar()
            frame23=Frame(airwin,width=900,height=300,highlightbackground="black",highlightthickness=2)
            frame23.place(x=200,y=305)
            l1=Label(frame23,text="Full Name:",font=bigfont3)
            l1.grid(row=1,column=0)
            username=Entry(frame23,width=125,textvariable=name)
            username.grid(row=1,column=1)

            l2=Label(frame23,text="UserID: ",font=bigfont3)
            l2.grid(row=2,column=0)
            l3=Label(frame23,text="Flight No: ",font=bigfont3)
            l3.grid(row=3,column=0)
            l4=Label(frame23,text="Flight Name: ",font=bigfont3)
            l4.grid(row=4,column=0)
            l5=Label(frame23,text="Departure: ",font=bigfont3)
            l5.grid(row=5,column=0)
            l6=Label(frame23,text="Destination: ",font=bigfont3)
            l6.grid(row=6,column=0)
            l7=Label(frame23,text="Sub Total: ",font=bigfont3)
            l7.grid(row=7,column=0)

            l22=Label(frame23,text=user,font=font4)
            l22.grid(row=2,column=1,sticky=W)
            l32=Label(frame23,text=flightno,font=font4)
            l32.grid(row=3,column=1,sticky=W)
            l42=Label(frame23,text=flightname,font=font4)
            l42.grid(row=4,column=1,sticky=W)
            l52=Label(frame23,text=a,font=font4)
            l52.grid(row=5,column=1,sticky=W)
            l62=Label(frame23,text=b,font=font4)
            l62.grid(row=6,column=1,sticky=W)
            l72=Label(frame23,text=p,font=font4)
            l72.grid(row=7,column=1,sticky=W)
            button4=Button(frame23,text="CONFIRM",command=confirm,width=50,padx=150)
            button4.grid(row=8,column=1,sticky=W)

#===============================================================================================================================                                             
                    
    airwin=Tk()
    airwin.geometry("1280x720")
    airwin.resizable(0,0)
    airwin.title("INDIAN AIRWAYS")
    img = Image.open(r"static\planes.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(airwin,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)

    def home():
        airwin.destroy()
        while a==1:
            import project
    #=====================================================================================================
    bigfont= Font(family="segoe script",
                size=30,
                weight="bold")
    bigfont2= Font(family="segoe script",
                size=25,
                weight="bold")
    bigfont3= Font(family="arial",
                size=15,
                weight="bold")
    font4= Font(family="arial",
                size=15,)
    #============================================FRAMES==================================================================
    frame21=Frame(airwin,width=800,height=100,highlightbackground="black",bg="#4b2aa1",highlightthickness=5)
    frame21.place(x=250,y=30)
    frame22=Frame(airwin,width=900,height=100,highlightbackground="black",highlightthickness=2)
    frame22.place(x=200,y=180)
    l3=Label(frame21,text="....INDIAN AIRWAYS.....",font=bigfont,bg="#4b2aa1",fg="white")
    l3.place(x=150,y=10)
    l1=Label(frame22,text="FROM",font=bigfont2)
    l1.place(x=20,y=20)
    l2=Label(frame22,text="TO",font=bigfont2)
    l2.place(x=600,y=30)
    var1 = StringVar()
    var2 = StringVar()   
    combo= ttk.Combobox(frame22,value=departure,textvariable=var1,state='readonly')
    combo.current(0)
    combo.place(x=200,y=45)
    combo1= ttk.Combobox(frame22,value=destination,textvariable=var2,state='readonly')
    combo1.current(0)
    combo1.place(x=700,y=45)
    button=Button(airwin,text="SEARCH",command=search,width=127)
    button.place(x=201,y=280)
    button2 = Button(airwin,command=home,bg="#d6d689")
    img2 = PhotoImage(file=r"static\button_home.gif")
    button2.config(image=img2)
    button2.place(x=10,y=10)
    airwin.mainloop()

if __name__ == '__main__':
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASS,
    database='titan_travels')
    air('titan')
    #print(airticket())