from calendar import Calendar
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter.font import Font
import mysql.connector
from PIL import Image, ImageTk
import random
import review
from invoice import genHotelInvoice
from tkinter import messagebox


PASS='Titan@1067'


def pay(room_type):
    #["",'Family room', 'Single Bed', 'Double Bed']
    if room_type == 'Family room':
        i = random.randrange(3000,5001,100)
    elif room_type == 'Single Bed':
        i = random.randrange(700,2000,100)
    elif room_type == 'Double Bed':
        i = random.randrange(1000,3000,100)
    return i

def hotelticket():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASS,
    database='titan_travels')
    cu = mydb.cursor()
    cu.execute('SELECT * FROM hoteltickets;')
    data = cu.fetchall()
    count = 0
    hoteltkt = "HT" + str(count)
    for i in data:
        if i[0] == hoteltkt:
            count += 1
            hoteltkt = "HT" + str(count)
    return hoteltkt

def hotel(userid):
    chkindt = ""
    chkoutdt = ""
    def searchhotels():
        SlctdCity=combo.get()
        room_type=combo1.get()
        print('dates:',CheckInDate,CheckOutDate)
        if city != '' and room_type != '' and CheckInDate != '' and CheckOutDate != '':
            frame24=Frame(main,highlightbackground="black",highlightthickness=5)
            frame24.place(x=10,y=350)
            for i in hotels:
                hotelBtns = {}
                if i[2] == SlctdCity:
                    z = f"{i[1]}, {i[2]}"

                    def slctdhotel(hotel=i[1]):
                        hotelid= i[0]
                        hotelname = i[1]
                        city = i[2]
                        hname = hotelname + ", "+city
                        roomtype = room_type
                        p = pay(room_type)
                        def confirm():
                            def makeinvoice():
                                pm = int(p)
                                gst = 0.18 * pm
                                total = gst + pm
                                gst = str(gst)
                                total = str(total)
                                try:
                                    genHotelInvoice(htltktid,user,hotelid,fname,hname,roomtype,CheckInDate,CheckOutDate,str(p),gst,total)
                                    messagebox.showinfo("File Downloaded", "Success!")
                                except:
                                    print('Error executing pdf...')
                                    messagebox.showerror("Error", "Unable to load File")
                                frame24.destroy()
                            fname = name.get()
                            if fname != "":
                                htltktid=hotelticket()
                                sql = "INSERT INTO hoteltickets VALUES (%s, %s,%s,%s,%s, %s,%s,%s,%s,%s)"
                                val = (htltktid,user,hotelid,fname,hotelname,city,roomtype,CheckInDate,CheckOutDate,p)
                                cu.execute(sql, val)
                                mydb.commit()
                                frame25.destroy()
                                frame24=Frame(main,width=900,height=300,bg='green',highlightbackground="black",highlightthickness=2)
                                frame24.place(x=200,y=305)
                                l1=Label(frame24,text=f"You Have Successfully Booked Hotel {hotelname}",font=bigfont3)
                                l2=Label(frame24,text=f"We wish you have a great day!",font=bigfont3)
                                button6=Button(frame24,text="Download Invoice",command=makeinvoice,width=50,padx=275)
                                l1.grid(row=1,column=1)
                                l2.grid(row=2,column=1)
                                button6.grid(row=3,column=1,sticky=W)
                                review.Review(user,fname)
                                

                        frame24.destroy()
                        frame25=Frame(main,highlightbackground="black",highlightthickness=5)
                        frame25.place(x=10,y=350)
                        name = StringVar()

                        l1=Label(frame25,text="Full Name:",font=bigfont3)
                        l1.grid(row=1,column=0)
                        username=Entry(frame25,width=125,textvariable=name)
                        username.grid(row=1,column=1)

                        l2=Label(frame25,text="UserID: ",font=bigfont3)
                        l2.grid(row=2,column=0)
                        l3=Label(frame25,text="HotelID: ",font=bigfont3)
                        l3.grid(row=3,column=0)
                        l4=Label(frame25,text="Hotel Name: ",font=bigfont3)
                        l4.grid(row=4,column=0)
                        l8=Label(frame25,text="Room Type: ",font=bigfont3)
                        l8.grid(row=5,column=0)
                        l5=Label(frame25,text="Check In: ",font=bigfont3)
                        l5.grid(row=6,column=0)
                        l6=Label(frame25,text="Check Out: ",font=bigfont3)
                        l6.grid(row=7,column=0)
                        l7=Label(frame25,text="Sub Total: ",font=bigfont3)
                        l7.grid(row=8,column=0)

                        l22=Label(frame25,text=user,font=font4)
                        l22.grid(row=2,column=1,sticky=W)
                        l32=Label(frame25,text=hotelid,font=font4)
                        l32.grid(row=3,column=1,sticky=W)
                        l42=Label(frame25,text=hname,font=font4)
                        l42.grid(row=4,column=1,sticky=W)
                        l82=Label(frame25,text=roomtype,font=font4)
                        l82.grid(row=5,column=1,sticky=W)
                        l52=Label(frame25,text=CheckInDate,font=font4)
                        l52.grid(row=6,column=1,sticky=W)
                        l62=Label(frame25,text=CheckOutDate,font=font4)
                        l62.grid(row=7,column=1,sticky=W)
                        l72=Label(frame25,text=p,font=font4)
                        l72.grid(row=8,column=1,sticky=W)
                        button4=Button(frame25,text="CONFIRM",command=confirm,width=50,padx=150)
                        button4.grid(row=9,column=1,sticky=W)
                        


                    hotelBtns[i[1]] = Button(frame24,text=z,command=slctdhotel,width=138,font=font3)
                    hotelBtns[i[1]].pack()

    a=1
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASS,
    database='titan_travels')
    cu = mydb.cursor()
    cu.execute('SELECT * FROM HOTELS;')
    data = cu.fetchall()
    noOfAvHotels = 0
    city=[""]
    roomtypes=["",'Family room', 'Single Bed', 'Double Bed']
    r1 = r2 = r3 = 0
    hotels=[]
    for i in data:
        noOfAvHotels +=1
        if i[2] not in city:
            city.append(i[2])
        data = [i[0],i[1],i[2],i[3],i[4],i[5]]
        hotels.append(data)
        print(i)
    user = userid
    main=Tk()
    main.geometry("1280x720")
    main.resizable(0,0)
    img = Image.open(r"static\hotel.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(main,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)
    bigfont= Font(family="segoe script",
            size=30,
            weight="bold")
    bigfont2= Font(family="segoe script",
            size=25,
            weight="bold")
    bigfont3= Font(family="arial",
                size=15,
                weight="bold")
    font3= Font(family="segoe script",
            size=10,
            weight="bold")
    font4= Font(family="arial",
                size=15,)
    frame21=Frame(main,width=800,height=100,highlightbackground="black",bg="#adefff",highlightthickness=5)
    frame21.place(x=250,y=30)
    l1=Label(frame21,text="...HOTEL BOOKINGS... ",font=bigfont).place(x=10,y=10)
    frame22=Frame(main,width=1250,height=100,highlightbackground="black",highlightthickness=3)
    frame22.place(x=10,y=200)
    l2=Label(frame22,text="CITY",font=bigfont2).place(x=10,y=10)
    l3=Label(frame22,text="ROOM TYPE",font=bigfont2).place(x=300,y=10)
    combo= ttk.Combobox(frame22,value=city,state='readonly')
    combo.current(0)
    combo.place(x=140,y=30)
    combo1= ttk.Combobox(frame22,value=roomtypes,state='readonly')
    combo1.current(0)
    combo1.place(x=540,y=30)
    b1=Button(main,text="SEARCH",command=searchhotels,width=177).place(x=10,y=300)
    
    def cal():      
            def selectdate():
                    mydate=mycal.get_date()
                    global CheckInDate
                    CheckInDate = mydate
                    l2=Label(frame22,text=CheckInDate,font=font3)
                    l2.place(x=750,y=60)
                    mycal.destroy()
                    opencal.destroy()
                    return CheckInDate
            mycal=Calendar(main, setmode= "day",date_pattern="dd/mm/yyyy")
            mycal.place(x=700,y=300)
            opencal= Button(frame22,text="Select Date",command=selectdate)
            opencal.place(x=890,y=30)

    def cal2():
            def selectdate2():
                    mydate=mycal1.get_date()
                    global CheckOutDate
                    CheckOutDate = mydate
                    l3=Label(frame22,text=CheckOutDate,font=font3)
                    l3.place(x=1020,y=60)
                    mycal1.destroy()
                    opencal1.destroy()
                    return CheckOutDate
            mycal1=Calendar(main, setmode= "day",date_pattern="dd/mm/yyy")
            mycal1.place(x=890,y=300)
            opencal1= Button(frame22,text="Select Date",command=selectdate2)
            opencal1.place(x=1180,y=30)
    l5=Label(frame22,text="CHECK IN",font=bigfont2).place(x=700,y=10)        
    b2=Button(frame22,text="DATE",command=cal).place(x=890,y=30)
    l6=Label(frame22,text="CHECK OUT",font=bigfont2).place(x=960,y=10)       
    b3=Button(frame22,text="DATE",command=cal2).place(x=1180,y=30)

    main.mainloop()

if __name__ == '__main__':
    hotel('titan')       
        

