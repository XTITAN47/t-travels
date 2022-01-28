from tkinter import *
from tkinter import ttk
import csv
from PIL import Image, ImageTk
from tkinter.font import Font
def air():
#================================================== SEARCH and DISPLAY ===================================================

    def search():
        dep=combo.get()
        arr=combo1.get()
        frame23=Frame(airwin,width=590,height=400,highlightbackground="white",highlightthickness=2)
        frame23.place(x=400,y=350)

        tt=open(r"mainp\tanmay\data\csvfiles\airt.csv","r",newline="\r\n")
        all_flights=csv.reader(tt)
        AVAILABLE=[]
        
        for i in all_flights:
            a=str(i[0]) ; b=str(i[1])

            if a!=str(dep) and b!=str(arr):
                pass
            else:
                AVAILABLE.append(i)
        
        def display():
            def ticket_box():
                flight=var.get()
                classs=clas.get()
                
                T=Text(frame23,height="10",width="80")
                data="<<<----YOU HAVE SUCCESSFULLY BOOKED YOUR AIR TICKET ---->>"+"\n"+AVAILABLE[flight][0]+"   TO   "+"\t"+AVAILABLE[flight][1]+"\nDEPARTURE : "+AVAILABLE[flight][2]+"\tARRIVAL : "+AVAILABLE[flight][3]+"\nYOU HAVE TO PAY Rs.  "+AVAILABLE[flight][classs]
                T.insert(END,data)
                T.grid(row="15",column="1")
                            
            clas=IntVar()
            r1=Radiobutton(frame23,text="ECONOMY CLASS",variable=clas,value=4,command=ticket_box).grid(row=str(x),column="1")
            r1=Radiobutton(frame23,text="BUSSINESS CLASS",variable=clas,value=5,command=ticket_box).grid(row=str(x+1),column="1")
            r1=Radiobutton(frame23,text="FIRST CLASS",variable=clas,value=6,command=ticket_box).grid(row=str(x+2),column="1")
                      
        var=IntVar()
        x=7
        for i in AVAILABLE:
            a=i[0]+'  TO  ,'+i[1]+"  DEPRATURE  : "+i[2]+"  ARRIVAL  : "+i[3]+'\n\nECONOMY CLASS    ----&----'+i[4]+'\t  BUSSINESS CLASS    ----&---- '+i[5]+'\tFIRST CLASS   ----&----   '+i[6]
            r1=Radiobutton(frame23,text=a,variable=var,value=AVAILABLE.index(i),command=display).grid(row=str(x),column="1")
            x=x+1

#===============================================================================================================================                                             
                    
    airwin=Tk()
    airwin.geometry("1280x720")
    airwin.resizable(0,0)
    airwin.title("INDIAN AIRWAYS")
    img = Image.open(r"mainp\tanmay\static\planes.jpg")
    photo = ImageTk.PhotoImage(img)
    Label(airwin,image=photo,borderwidth='0',bg='white',height=720,width=1280).place(x=0,y=0)
    #=====================================================================================================
    bigfont= Font(family="segoe script",
                size=30,
                weight="bold")
    bigfont2= Font(family="segoe script",
                size=25,
                weight="bold")
    #============================================FRAMES==================================================================
    frame21=Frame(airwin,width=800,height=100,highlightbackground="black",bg="#4b2aa1",highlightthickness=5)
    frame21.place(x=250,y=30)
    frame22=Frame(airwin,width=900,height=100,highlightbackground="black",highlightthickness=2)
    frame22.place(x=200,y=180)
    l3=Label(frame21,text="....INDIAN AIRWAYS.....",font=bigfont,bg="#4b2aa1",fg="white").place(x=150,y=10)
    l1=Label(frame22,text="FROM",font=bigfont2).place(x=20,y=20)
    l2=Label(frame22,text="TO",font=bigfont2).place(x=600,y=30)
   
    combo= ttk.Combobox(frame22,value=["Departure","DELHI ","JAIPUR ","MUMBAI ","AGRA","KOLKATA"])
    combo.current(0)
    combo.place(x=200,y=45)
    combo1= ttk.Combobox(frame22,value=["Destination","DELHI","JAIPUR","MUMBAI","AGRA"])
    combo1.current(0)
    combo1.place(x=700,y=45)
    button=Button(airwin,text="SEARCH",command=search).place(x=550,y=300)
    airwin.mainloop()