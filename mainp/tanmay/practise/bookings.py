from email.mime import image
from tkinter import *
from tkinter import messagebox
import csv
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.font import Font
import mysql.connector
from tkinter import messagebox



def loginsuccessful():
    
        logmain=Tk()
        logmain.geometry("500x600+400+100")
        
        #--------------------- for train --------------------------------------------------------
        def train_booking():
            logmain.destroy()
            train_tickets.train()

        #-------------------------- for air ------------------------------------------------------

        def air():
            logmain.destroy()
            air_tickets.mainair()

#########-----------------------------------main window showing different opions-----------------------------------#############

        air=Button(logmain,text="FLIGHT BOOKING",image=r"C:\Users\vimar\Desktop\t-travels\mainp\tanmay\download.png").grid(row="1",column="1")
        tr=Button(logmain,text="TRAIN TICKETS",command=train_booking).grid(row="1",column="2")
        bus=Button(logmain,text="BUS TICKETS").grid(row="1",column="3")
        hotel=Button(logmain,text="HOTEL BOOKING").grid(row="2",column="1")
        flight=Button(logmain,text="FLIGHT BOOKING").grid(row="2",column="2")
        package=Button(logmain,text="COMPLETE PACKAGES ").grid(row="2",column="3")
        logmain.mainloop()
loginsuccessful()        