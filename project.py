from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import air_tickets,train_tickets,bus_ticket,hotel_booking,time
import mysql.connector
from exclusives import *
import admin

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Titan@1067",
  database='titan_travels'
)
cu = mydb.cursor()
if checkDatabaseExists() == False:
    DatabaseDoesNotExist()

def AOF():        
#===== get fn=================================================================================================================
        a1=a.get()
        userid = a1
        b1=b.get()
        c1=c.get()        
        d1=d.get()
        e1=e.get()
        user = [a1,b1,c1,d1,e1,'False']
        if validateUserReg(user) == 1:
            if authenticateReg(user) == 1:
                LOGIN()

#===========ADMIN===============================================================================================================     
def ADMIN():
    w.destroy()
    log=Tk()
    log.geometry("400x500")
    log.config(bg="#25be7c")
    log.title("ADMIN LOGIN")
    log.resizable(0,0)
    frame2=Frame(log,width=399,height=10,highlightbackground="#e67402",bg="#25be7c",highlightthickness=7)
    frame2.place(x=0,y=30)
    frame3=Frame(log,width=399,height=10,highlightbackground="#e67402",bg="#25be7c",highlightthickness=7)
    frame3.place(x=0,y=50)
    l1=Label(log,text="ADMIN LOGIN",fg="#2a34f7",bg="#25be7c",font="Valentine 30 ")
    l1.place(x=70,y=10)

    frame2=Frame(log,width=380,height=180,highlightbackground="#02e659",bg="#25be7c",highlightthickness=2)
    frame2.place(x=10,y=190) 
    
    ul1=Label(log,text="USERNAME :-",font=("comic sans", 12, "bold"),fg="#fc8c03",bg="#25be7c")
    ul1.place(x=50,y=240)
    ul4=Label(log,text="PASSWORD :-",font=("comic sans", 12, "bold"),fg="#fc8c03",bg="#25be7c")
    ul4.place(x=50,y=270)

    user=StringVar()
    passwd=StringVar()

    le1=Entry(log,textvariable=user,bd=2)
    le1.place(x=190,y=240)
    le2=Entry(log,textvariable=passwd,bd=2,show="*")
    le2.place(x=190,y=270)

    def ret2():
        u=user.get()
        p=passwd.get()
        if authenticateLogin(u,p) == 2:
            log.destroy()
            admin.Home()
        

    btn4=Button(log,text="SUBMIT",command=ret2)
    btn4.place(x=150,y=325)                                                                    
    log.mainloop()

#=============================================================================================================================     

   
          
#======================== login =============================================================================================
def LOGIN():

    w.destroy() #=========== ye line add karni thi bas =======================================

    log=Tk()
    log.geometry("400x500")
    log.config(bg="#262626")
    log.title("LOGIN")
    log.resizable(0,0)
    frame2=Frame(log,width=399,height=10,highlightbackground="#e67402",bg="#262626",highlightthickness=7)
    frame2.place(x=0,y=30)
    frame3=Frame(log,width=399,height=10,highlightbackground="#e67402",bg="#262626",highlightthickness=7)
    frame3.place(x=0,y=50)
    l1=Label(log,text="LOGIN",fg="#02e659",bg="#262626",font="Valentine 50 ")
    l1.place(x=90,y=10)
#==========================================================================================================================
    frame2=Frame(log,width=380,height=180,highlightbackground="#02e659",bg="#262626",highlightthickness=2)
    frame2.place(x=10,y=190) 
    
    ul1=Label(log,text="USERNAME :-",font=("comic sans", 12, "bold"),fg="#fc8c03",bg="#262626")
    ul1.place(x=50,y=240)
    ul4=Label(log,text="PASSWORD :-",font=("comic sans", 12, "bold"),fg="#fc8c03",bg="#262626")
    ul4.place(x=50,y=270)

    user=StringVar()
    passwd=StringVar()

    le1=Entry(log,textvariable=user,bd=2)
    le1.place(x=190,y=240)  #ek kaam krte hain
    le2=Entry(log,textvariable=passwd,bd=2,show="*")
    le2.place(x=190,y=270)

    def loginsuccessful(userid):
                                                                    
                                
    ####+++++++++++++++++++++++++++++++++++++++++AIR TICKETS BOOKING+++++++++++++++++++++++++++++++++++++++########

        def air():
            main.destroy()
            air_tickets.air(userid)
            
            
    ####################################################-------TRAIN TICKET BOOKING------###################################
        
        def train_booking():
            main.destroy()    
            train_tickets.train(userid)  
            
            
##########################---------------------------BUS TICKET BOOKING--------------------------------------------##############################
        def bus():
            main.destroy()
            bus_ticket.bus(userid)
#=================================================HOTEL_BOOKINGS======================================================================        
        def hotel():
            main.destroy()
            hotel_booking.hotel(userid)    

###########################-----------------------------main window showing different opions--------------------------------###########################

        log.destroy()

        main=Tk()
        main.title("TRAVEL AGENCY")
        main.resizable(0,0)
        main.geometry("1280x720")
        img = Image.open(r"static\main.jpg")
        photo = ImageTk.PhotoImage(img)
        Label(main,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)
        bigfont= Font(family="segoe script",
                        size=30,
                        weight="bold")
        bigfont2= Font(family="segoe script",
                        size=10,
                        weight="bold")
        frame21=Frame(main,width=800,height=100,highlightbackground="black",highlightthickness=5)
        frame21.place(x=400,y=30)
        label_name=Label(frame21,text="TITAN TRAVEL AGENCY",font=bigfont)
        label_name.place(x=10,y=5)
    #==========================================================================================================================================================

    #================================================____FRAME2____============================================================================
        def open():
            def close():
                frame22.destroy()
            frame22=Frame(main,width=400,height=700,highlightbackground="#364145",highlightthickness=5)
            frame22.place(x=10,y=10)
            b2=Button(frame22,text="CLOSE",command=close).place(x=0,y=0)
            air1=Button(frame22,text="FLIGHT BOOKING",command=air,height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=30)
            tr=Button(frame22,text="TRAIN TICKETS",command=train_booking,height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=120)
            bus1=Button(frame22,text="BUS TICKETS",command=bus,height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=210)
            hotel1=Button(frame22,text="HOTEL BOOKING",command=hotel,height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=300)
            package=Button(frame22,text="COMPLETE PACKAGES ",height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=390)
        #=============================____CLOCK___=======================================================================================================
        def start():
            text= time.strftime("%H:%M:%S")
            label.config(text=text)
            label.after(100,start)
        frame23=Frame(main,width=250,height=70,highlightbackground="black",bg="#868787",highlightthickness=2)
        frame23.place(x=1000,y=150)    
        label = Label(frame23,font=("ds-digital",30,"bold"),bg="#868787",fg="#49c9c9")
        label.place(x=10,y=4)
        start()
        b1=Button(main,command=open,text="open").place(x=10,y=10)
        label21=Label(text="PACK YOUR BAGS AND GET READY FOR THE ",font=bigfont).place(x=190,y=400)
        label22=Label(text=" TRIP TO REACH YOUR DREAM DESTINATIONS",font=bigfont).place(x=220,y=500)
        main.mainloop()
       
       
#============================== Retrieve =====================================================================================
    
    def ret():
        u=user.get()
        p=passwd.get()
        if authenticateLogin(u,p) in (1,2):
            loginsuccessful(u)
        
#===============================================================================================================================

    btn1=Button(log,text="SUBMIT",command=ret)
    btn1.place(x=150,y=325)                                                                    
    log.mainloop()

#================================================================================================================================================
# ======================================== xxxxxxx _____main window_______xxxxxxxx ==================================================================================
                
w=Tk()
w.geometry("1280x720")
w.config(bg="#262626")
w.title("titan travels")
w.resizable(0,0)


#frames ================================================================================
f1=Frame(w,bg="#00FFFF",width=450,height=670)
f1.place(x=65,y=20)

l1=Label(w,text="TITAN TRAVEL",fg="#e0106a",bg="#262626",font="Valentine 50 underline")
l1.place(x=550,y=10)
l0=Label(w,text="======",fg="#fc8c03",bg="#262626")
l0.config(font=('Valentine', 40 ))
l0.place(x=1050,y=10)
#=========================CLOCK=======================================================================
def start():
    text= time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(100,start)
frame23=Frame(w,width=250,height=70,highlightbackground="#49c9c9",bg="#262626",highlightthickness=2)
frame23.place(x=1000,y=150)    
label = Label(frame23,font=("ds-digital",30,"bold"),bg="#262626",fg="#49c9c9")
label.place(x=10,y=4)
start()


#=FRAME 2=======================================================================================================
f2=Frame(f1,bg="#262626",width=410,height=630)
f2.place(x=20,y=20)
l2=Label(f2,text="REGISTER HERE.........",font=("comic sans", 20 , "bold"),fg="#fc8c03",bg="#262626")
l2.place(x=30,y=25)
#=========================================LABELS FOR ENTRIES IN REGISTRATION=================================================================

ul1=Label(f2,text="USERNAME",font=("comic sans", 15 , "bold"),fg="#fc8c03",bg="#262626")
ul1.place(x=30,y=100)
ul2=Label(f2,text="CONTACT ",font=("comic sans", 15 , "bold"),fg="#fc8c03",bg="#262626")
ul2.place(x=30,y=150)
ul3=Label(f2,text="EMAIL",font=("comic sans", 15 , "bold"),fg="#fc8c03",bg="#262626")
ul3.place(x=30,y=200)
ul4=Label(f2,text="PASSWORD",font=("comic sans", 15 , "bold"),fg="#fc8c03",bg="#262626")
ul4.place(x=30,y=250)
ul5=Label(f2,text="CONFIRM ",font=("comic sans", 15 , "bold"),fg="#fc8c03",bg="#262626")
ul5.place(x=30,y=300)

#=================================STRING VARIABLES===================================
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
#===============================ENTRY VALUE===============================================
ul1entry=Entry(f2,textvariable=a)
ul2entry=Entry(f2,textvariable=b)
ul3entry=Entry(f2,textvariable=c)
ul4entry=Entry(f2,textvariable=d,show="*")
ul5entry=Entry(f2,textvariable=e)
    #====================================PACKING===================================================
ul1entry.place(x=200,y=100)
ul2entry.place(x=200,y=150)
ul3entry.place(x=200,y=200)
ul4entry.place(x=200,y=250)
ul5entry.place(x=200,y=300)

#===================================BUTTON=======================================================
    
    
b1=Button(f2,text="SUBMIT",command=AOF,fg="#fc8c03",bg="#262626").place(x=150,y=350)
b2=Button(f2,text="LOGIN",command=LOGIN,fg="#fc8c03",bg="#262626").place(x=200,y=350)
b3=Button(f2,text="ADMIN",command=ADMIN,fg="#fc8c03",bg="#262626").place(x=175,y=400)

    
       
    
w.mainloop()


#========================================================================================================
                
                


