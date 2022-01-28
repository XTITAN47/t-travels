from tkinter import *
from tkinter import messagebox
import csv
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.font import Font
import mysql.connector
from tkinter import messagebox
def train():
        
#================================================== SEARCH and DISPLAY ===================================================

    def search():
        dep=combo.get()
        arr=combo1.get()
        frame23=Frame(trainmain,width=700,height=400,highlightbackground="black",highlightthickness=2)
        frame23.place(x=200,y=350)

        tt=open(r"mainp\tanmay\data\csvfiles\trains.csv","r",newline="\r\n")
        trains=csv.reader(tt)
        AVAILABLE=[]
        
        for i in trains:
            a=str(i[0]) ; b=str(i[1])

            if a!=str(dep) and b!=str(arr):
                pass
            else:
                AVAILABLE.append(i)
        
        def display():
            def ticket_box():
                train=var.get()
                classs=clas.get()
                
                T=Text(frame23,height=10,width=100)
                data="<<<----YOU HAVE SUCCESSFULLY BOOKED YOUR TRAIN TICKET ---->>"+"\n"+AVAILABLE[train][0]+"   TO   "+"\t"+AVAILABLE[train][1]+"\nTRAIN NAME : "+AVAILABLE[train][2]+"\nDEPARTURE : "+AVAILABLE[train][3]+"\tARRIVAL : "+AVAILABLE[train][4]+"\nYOU HAVE TO PAY Rs.  "+AVAILABLE[train][classs]
                T.insert(END,data)
                T.grid(row=15,column=10)
                            
            clas=IntVar()
            r1=Radiobutton(frame23,text="ECONOMY",variable=clas,value=5,command=ticket_box).grid(row=str(x),column=10)
            r1=Radiobutton(frame23,text="SLEEPER",variable=clas,value=6,command=ticket_box).grid(row=str(x+1),column=10)
            r1=Radiobutton(frame23,text="FIRST CLASS",variable=clas,value=7,command=ticket_box).grid(row=str(x+2),column=10)
                      
        var=IntVar()
        x=70
        for i in AVAILABLE:
            a=i[0]+'  TO  ,'+i[1]+"  TRAIN NAME   : "+i[2]+"  DEPRATURE  : "+i[3]+"  ARRIVAL  : "+i[4]+'\n\nECONOMY  :  '+i[5]+'\t  SLEEPER    :  '+i[6]+'\tFIRST CLASS   :   '+i[7]
            r1=Radiobutton(frame23,text=a,variable=var,value=AVAILABLE.index(i),command=display).grid(row=str(x),column=10)
            x=x+10

#===============================================================================================================================                                             
                    
    trainmain=Tk()
    trainmain.geometry("1280x720")
    trainmain.resizable(0,0)
    trainmain.title("INDIAN RAILWAYS")

    bigfont= Font(family="segoe script",
                size=30,
                weight="bold")
    bigfont2= Font(family="segoe script",
                size=25,
                weight="bold")
    img = Image.open(r"mainp\tanmay\static\photo.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(trainmain,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)
    frame21=Frame(trainmain,width=800,height=100,highlightbackground="#adefff",bg="#adefff",highlightthickness=0)
    frame21.place(x=250,y=30)
    l3=Label(frame21,text="Way to your dream destinations........",font=bigfont,fg="black",bg="#adefff").place(x=10,y=10)
    frame22=Frame(trainmain,width=900,height=100,highlightbackground="black",bg="white",highlightthickness=1)
    frame22.place(x=200,y=180)
    l1=Label(frame22,text="FROM",font=bigfont2,bg="white").place(x=30,y=20)
    l2=Label(frame22,text="TO",font=bigfont2,bg="white").place(x=500,y=20)
    combo= ttk.Combobox(frame22,value=["Departure","DELHI ","JAIPUR ","MUMBAI ","AGRA"])
    combo.current(0)
    combo.place(x=180,y=40)
    combo1= ttk.Combobox(frame22,value=["Destination","DELHI","JAIPUR","MUMBAI","AGRA"])
    combo1.current(0)
    combo1.place(x=600,y=40)
    #====================================================================================================================
  
    
    
    
    #============================================================================================================================
    button=Button(trainmain,text="SEARCH",command=search).place(x=500,y=300) 
    button22=Button(trainmain,text="BACK").place(x=600,y=300)
    trainmain.mainloop()
 