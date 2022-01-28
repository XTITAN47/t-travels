from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import BOLD, Font
import mysql.connector
from tkinter import messagebox
#=============================================================================================================
def LOG_1():
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
#===========================================================================================================================
    ul1value=StringVar()
    ul4value=StringVar()
    ul1entry=Entry(log,textvariable=ul1value)
    ul4entry=Entry(log,textvariable=ul4value)  
    ul1entry.place(x=190,y=240)
    ul4entry.place(x=190,y=270)  
#===========================================BUTTON=====================================================================================    
        


    b1=Button(log,text="LOGIN",command=loginsuccessful,fg="#fc8c03",bg="#262626").place(x=150,y=325)
    
    
    
    log.mainloop()
  
