from tkinter import *
from tkinter import ttk
import csv
from PIL import Image, ImageTk
from tkinter.font import Font
import mysql.connector
a=1
def air():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="titan@1067",
    database='titan_travels')
    cu = mydb.cursor()
    cu.execute('SELECT * FROM AIRTICKETS;')
    data = cu.fetchall()
    noOfAvFlights = 0
    departure=[]
    destination=[]
    airticketid=[]
    price=[]
    username=[]
    flightname=[]
    flightno=[]

    for i in data:
        noOfAvFlights +=1
        if i[0] not in airticketid:
            airticketid.append(i[0])
        if i[2] not in flightno:
            flightno.append(i[2])
        if i[3] not in username:
            username.append(i[3])
        if i[4] not in flightname:
            flightname.append(i[4])
        if i[5] not in departure:
            departure.append(i[5])
        if i[6] not in destination:
            destination.append(i[6])
        if i[7] not in price:
            price.append(i[7])
        print(i)
    
#================================================== SEARCH and DISPLAY ===================================================
    def search():
        frame23=Frame(airwin,width=900,height=300,highlightbackground="black",highlightthickness=2)
        frame23.place(x=200,y=300)
        l1=Label(frame23,text="USERNAME:-",font=bigfont2).place(x=50,y=30)
        #=============================USERNAME ENTRY=============================================================
        use=StringVar()
        username=Entry(frame23,textvariable=use,bd=2).place(x=280,y=50)
        #==================================FILGHT NAME (LABEL+ENTRY)=============================================
        l2=Label(frame23,text="FLIGHT NAME:-",font=bigfont2).place(x=50,y=100)
        flight_name=StringVar()
        filght_nm=Entry(frame23,textvariable=flight_name,bd=2).place(x=280,y=110)
        #====================================AIRTICKET ID ========================================================
        l3=Label(frame23,text="AIRTICKET ID:-",font=bigfont2).place(x=50,y=160)
        flight_id=StringVar()
        filght_id1=Entry(frame23,textvariable=flight_id,bd=2).place(x=280,y=170)
        #========================================BUTTON===========================================================
        button2=Button(frame23,text="NEXT",command=next,width=127,bg="black",fg="white",bd=2).place(x=0,y=269)

        # def form():
        #     search()
        #     a=use.get()
        #     b=flight_name.get()
        #     list=[a,b]
        #     cu=mydb.cursor()
        #     sql=("insert into airtickets(username,flightname) values(%s,%s)")
        #     cu.execute(sql,list)
        pass
#===============================================================================================================================
    def next():
        
        frame24=Frame(airwin,width=900,height=300,highlightbackground="black",highlightthickness=2)
        frame24.place(x=200,y=300)
        #==============================================================================================
        l9=Label(frame24,text="===============YOUR FLIGHT BOOKING============",font="arial 18 bold").place(x=100,y=10)
        l10=Label(frame24,text=text,font="arial 15 bold").place(x=90,y=40)
        l11=Label(frame24,text="===============================================",font="arial 18 bold").place(x=100,y=190)
        pass    
    text="""         
                     USERNAME:-    {}
                     DEPARTURE :-  {}
                     DESTINATION:- {}
                     FLIGHT NO.:-  {}
                     FLIGHT NAME:- {}
                     PRICE:-       {} 
                        

    
        """.format(i[3],i[5],i[6],i[2],i[4],i[7])  
#===============================================================================================================================                                             
    def home():
        airwin.destroy()
        while a==1:
            import project
        pass                
    airwin=Tk()
    airwin.geometry("1280x720")
    airwin.resizable(0,0)
    airwin.title("INDIAN AIRWAYS")
    img = Image.open(r"static\planes.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(airwin,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)
    #=====================================================================================================
    bigfont= Font(family="segoe script",
                size=30,
                weight="bold")
    bigfont2= Font(family="segoe script",
                size=20,
                weight="bold")
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
   
    combo= ttk.Combobox(frame22,value=departure)
    combo.current(0)
    combo.place(x=200,y=45)
    combo1= ttk.Combobox(frame22,value=destination)
    combo1.current(0)
    combo1.place(x=700,y=45)
    button=Button(airwin,text="SEARCH",command=search,width=126,bg="black",fg="white")
    button.place(x=202,y=280)
    button2 = Button(airwin,command=home,bg="#d6d689")
    img2 = PhotoImage(file=r"static\button_home.gif")
    button2.config(image=img2)
    button2.place(x=10,y=10)
    
    airwin.mainloop()

if __name__ == '__main__':
    air()
