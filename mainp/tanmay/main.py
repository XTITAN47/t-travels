from cgitb import text
from tkinter import *
from tkinter import messagebox
import csv
from tkinter import ttk
from distutils import command
from distutils.util import execute
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox 
import air_tickets_final,train_tickets,bus_ticket,hotel_booking,time



def train_bookingframe22():
    train_tickets.train()           
#=============================================================================TRAIN BOOKINGS ==================================================                                                    
                                
####+++++++++++++++++++++++++++++++++++++++++AIR TICKETS BOOKING+++++++++++++++++++++++++++++++++++++++########

def airframe22():
    main.destroy()
    air_tickets_final.air()
            
            
    ####################################################-------TRAIN TICKET BOOKING------###################################
        
##########################---------------------------BUS TICKET BOOKING--------------------------------------------##############################
def busframe22():
    
    bus_ticket.bus()
#=================================================HOTEL_BOOKINGS======================================================================        
def hotelframe22():
    
    hotel_booking.hotel()    
                
main=Tk()
main.title("TRAVEL AGENCY")
main.config(bg="#868787")
main.resizable(0,0)
main.geometry("1280x720")
img = Image.open(r"C:\Users\vimar\Desktop\t-travels\mainp\tanmay\main.jpg")
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
label_name.place(x=100,y=5)
#==========================================================================================================================================================

#================================================____FRAME2____============================================================================
def open():
    def close():
        frame22.destroy()
    frame22=Frame(main,width=400,height=700,highlightbackground="#364145",highlightthickness=5)
    frame22.place(x=10,y=10)
    b2=Button(frame22,text="CLOSE",command=close).place(x=0,y=0)
    air1=Button(frame22,text="FLIGHT BOOKING",height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=30)
    tr=Button(frame22,text="TRAIN TICKETS",height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=120)
    bus1=Button(frame22,text="BUS TICKETS",height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=210)
    hotel1=Button(frame22,text="HOTEL BOOKING",height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=300)
    package=Button(frame22,text="COMPLETE PACKAGES ",height=5,width=53,bg="#364145",fg="#1bc2f5").place(x=0,y=390)
#=============================____CLOCK___=======================================================================================================
def start():
    text= time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(100,start)
frame23=Frame(main,width=250,height=70,highlightbackground="black",bg="#364145",highlightthickness=2)
frame23.place(x=1000,y=150)    
label = Label(frame23,font=("ds-digital",30,"bold"),bg="#364145",fg="#1bc2f5")
label.place(x=10,y=4)
start()
b1=Button(main,command=open,text="OPEN",height=5,width=30,bg="#364145",fg="#1bc2f5").place(x=10,y=10)
label21=Label(text="PACK YOUR BAGS AND GET READY FOR THE ",font=bigfont).place(x=190,y=400)
label22=Label(text=" TRIP TO REACH YOUR DREAM DESTINATIONS",font=bigfont).place(x=220,y=500)
main.mainloop()