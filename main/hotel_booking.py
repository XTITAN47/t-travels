from calendar import Calendar
from tkinter import *
from tkinter import ttk
import csv
from tkcalendar import *
from tkinter.font import Font
def hotel():
        def search_rooms():
                city=combo.get()
                room_type=combo1.get()
                
                cat=0
                if room_type=="FAMILY ROOM(4)":
                        cat=cat+4
                if room_type=="SINGLE BED(1)":
                        cat=cat+5
                else:
                        cat=6        
                file=open(r"mainp\tanmay\data\csvfiles\hotels.csv","r",newline='\r\n')
                hotels=csv.reader(file)
                AVAILABLE_HOTELS=[]
                x=10
                var=IntVar()   
                for i in hotels:
                        if i[0]==city:
                                AVAILABLE_HOTELS.append(i)                               
                        else:
                                pass
                        
                def text_box():
                        hotel_booked=var.get()
                        
                        for i in AVAILABLE_HOTELS:
                                if i[7]==str(hotel_booked):
                                        T=Text(main,height="10",width="80")
                                        data="<<<----YOU HAVE SUCCESSFULLY BOOKED HOTEL ROOM ---->>>"+"\n"+"\nHOTEL NAME : "+i[1]+"\nHOTEL ADDRESS : "+i[2]+"\nCONTACT NUMBER : "+i[3]+"\nYOU HAVE TO PAY RS. "+i[cat]+"\n\n*PLEASE ENSURE BRINGING PHOTO IDENTITY PROOF OF ALL STAYING MEMBERS\n\t\tTHANK YOU"
                                        T.insert(END,data)
                                        T.grid(row="15",column="1")
                                else:
                                        pass

                for j in AVAILABLE_HOTELS:
                        t=int(j[7])
                        a=j[1]+"- - & - - STAYING COST FOR - - "+room_type+" - - - >  Rs. "+j[cat]                           
                        r1=Radiobutton(main,text=a,variable=var,value=t,command=text_box).grid(row=str(x),column="1")
                        x=x+1
                             
                
                    
        main=Tk()
        main.geometry("1280x720")
        main.resizable(0,0)
        bigfont= Font(family="segoe script",
                size=30,
                weight="bold")
        bigfont2= Font(family="segoe script",
                size=25,
                weight="bold")
        l1=Label(main,text="TT' HOTELS ",font=bigfont).grid(row="1",column="1")
        l2=Label(main,text="SELECT CITY FOR STAY",font="aerial 25 bold").grid(row="2",column="1")
        l3=Label(main,text="SELECT ROOM TYPE",font="aerial 25 bold").grid(row="3",column="1")
        combo= ttk.Combobox(main,value=["- -SELECT CITY - -","DELHI","JAIPUR","MUMBAI","AGRA","ETAH"])
        combo.current(0)
        combo.grid(row="2",column="2")
        combo1= ttk.Combobox(main,value=["SELECT ROOM","FAMILY ROOM(4)","SINGLE BED(1)","DOUBLE BED(2)"])
        combo1.current(0)
        combo1.grid(row="3",column="2")
        b1=Button(main,text="SEARCH",command=search_rooms).grid(row="4",column="2")
       
        def cal(): 
                       
                def selectdate():
                        mydate=mycal.get_date()
                        print(mydate)  
                        mycal.destroy()
                        opencal.destroy()
                mycal=Calendar(main, setmode= "day",date_pattern="d/m/yy")
                mycal.place(x=370,y=300)
                opencal= Button(main,text="Select Date",command=selectdate)
                opencal.place(x=370,y=200)
        def cal2():
                def selectdate2():
                        mydate=mycal1.get_date()
                        print(mydate)  
                        mycal1.destroy()
                        opencal1.destroy()
                mycal1=Calendar(main, setmode= "day",date_pattern="d/m/yy")
                mycal1.place(x=370,y=500)
                opencal1= Button(main,text="Select Date",command=selectdate2)
                opencal1.place(x=370,y=400)
                        
        l5=Label(main,text="CHECK IN",font=bigfont2).place(x=150,y=200)        
        b2=Button(main,text="DATE",command=cal).place(x=370,y=200)
        l6=Label(main,text="CHECK OUT",font=bigfont2).place(x=150,y=400)        
        b3=Button(main,text="DATE",command=cal2).place(x=370,y=400)
        
        
        
        
        
        
        main.mainloop()

        

