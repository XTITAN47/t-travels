from tkinter import *
from tkinter import ttk
import csv
from PIL import Image, ImageTk
from tkinter.font import Font
def bus():
#================================================== SEARCH and DISPLAY ===================================================

    def search():
        frame23=Frame(buswin,width=900,height=400,highlightbackground="black",highlightthickness=2)
        frame23.place(x=200,y=350)
        dep=combo.get()
        arr=combo1.get()

        tt=open(r"mainp\tanmay\data\csvfiles\buses.csv","r",newline="\r\n")
        buses=csv.reader(tt)
        AVAILABLE=[]
        
        for i in buses:
            a=str(i[0]) ; b=str(i[1])

            if a!=str(dep) and b!=str(arr):
                pass
            else:
                AVAILABLE.append(i)
        
        def ticket_box():
                bus=var.get()
                
                T=Text(frame23,height="10",width="80")
                data="<<<----YOU HAVE SUCCESSFULLY BOOKED YOUR BUS TICKET ---->>"+"\n"+AVAILABLE[bus][0]+"   TO   "+"\t"+AVAILABLE[bus][1]+"\nBUS NAME : "+AVAILABLE[bus][2]+"\nDEPARTURE : "+AVAILABLE[bus][3]+"\tARRIVAL : "+AVAILABLE[bus][4]+"\nYOU HAVE TO PAY Rs.  "+AVAILABLE[bus][5]
                T.insert(END,data)
                T.grid(row="15",column="1")
                      
        var=IntVar()
        x=7
        for i in AVAILABLE:
            a=i[0]+'  - -TO- -  '+i[1]+"  ---&---BUS NAME   : "+i[2]+"  ---&---DEPRATURE  : "+i[3]+"  ---&---ARRIVAL  : "+i[4]+"  ---&---FARE PRICE : "+i[5]
            r1=Radiobutton(frame23,text=a,variable=var,value=AVAILABLE.index(i),command=ticket_box).grid(row=str(x),column="1")
            x=x+1

#===============================================================================================================================                                             
                    
    buswin=Tk()
    buswin.geometry("1280x720")
    buswin.resizable(0,0)
    buswin.title("BUS BOOKING")
    bigfont= Font(family="segoe script",
                size=30,
                weight="bold")
    bigfont2= Font(family="segoe script",
                size=25,
                weight="bold")
    #=========================================IMAGE FOR BACKGROUND==============================================================================
    img = Image.open(r"mainp\tanmay\static\bus.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(buswin,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)
    #===============================FRAME1==================================================================================
    frame21=Frame(buswin,width=800,height=100,highlightbackground="black",bg="#adefff",highlightthickness=5)
    frame21.place(x=250,y=30)
    #===========================CONTENT OF FRAME ======================================================================================
    l3=Label(frame21,text="TITAN TOURS AND TRAVELS........",font=bigfont,bg="#adefff",fg="black").place(x=40,y=10)
    #===================================FRAME2====================================================================================================
    frame22=Frame(buswin,width=900,height=100,highlightbackground="black",highlightthickness=2)
    frame22.place(x=200,y=180)
    #======================================CONTENT OF FRAME2 ====================================================================================
    l1=Label(frame22,text="FROM :-",font=bigfont2).place(x=10,y=10)
    l2=Label(frame22,text="TO :-",font=bigfont2).place(x=550,y=10)
    combo= ttk.Combobox(frame22,value=["Departure","DELHI ","JAIPUR ","PATNA","AGRA"])
    combo.current(0)
    combo.place(x=190,y=40)
    combo1= ttk.Combobox(frame22,value=["Destination","DELHI","JAIPUR","PATNA","AGRA","ETAH","PATIYALI"])
    combo1.current(0)
    combo1.place(x=700,y=40)
    button=Button(buswin,text="SEARCH",command=search).place(x=600,y=300)
    buswin.mainloop()

