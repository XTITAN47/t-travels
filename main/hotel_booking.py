from calendar import Calendar
from tkinter import *
from tkinter import ttk
import csv
from tkcalendar import *
from tkinter.font import Font
from PIL import Image, ImageTk
def hotel():
        def search_rooms():
                frame24=Frame(main,width=800,height=200,highlightbackground="black",highlightthickness=5)
                frame24.place(x=250,y=350)
                city=combo.get()
                room_type=combo1.get()
                
                cat=0
                if room_type=="FAMILY ROOM(4)":
                        cat=cat+4
                if room_type=="SINGLE BED(1)":
                        cat=cat+5
                else:
                        cat=6
                
                

                        
                        
                file=open(r"data\csvfiles\hotels.csv","r",newline='\r\n')
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
                                        T=Text(frame24,height="10",width="80")
                                        data="<<<----YOU HAVE SUCCESSFULLY BOOKED HOTEL ROOM ---->>>"+"\n"+"\nHOTEL NAME : "+i[1]+"\nHOTEL ADDRESS : "+i[2]+"\nCONTACT NUMBER : "+i[3]+"\nYOU HAVE TO PAY RS. "+i[cat]+"\n\n*PLEASE ENSURE BRINGING PHOTO IDENTITY PROOF OF ALL STAYING MEMBERS\n\t\tTHANK YOU"
                                        T.insert(END,data)
                                        T.grid(row="15",column="1")
                                else:
                                        pass

                for j in AVAILABLE_HOTELS:
                        t=int(j[7])
                        a=j[1]+"- - & - - STAYING COST FOR - - "+room_type+" - - - >  Rs. "+j[cat]                           
                        r1=Radiobutton(frame24,text=a,variable=var,value=t,command=text_box).grid(row=str(x),column="1")
                        x=x+1
                             
                
                    
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
        frame21=Frame(main,width=800,height=100,highlightbackground="black",bg="#adefff",highlightthickness=5)
        frame21.place(x=250,y=30)
        l1=Label(frame21,text="...HOTEL BOOKINGS... ",font=bigfont).place(x=10,y=10)
        frame22=Frame(main,width=1250,height=100,highlightbackground="black",highlightthickness=3)
        frame22.place(x=10,y=200)
        l2=Label(frame22,text="CITY",font=bigfont2).place(x=10,y=10)
        l3=Label(frame22,text="ROOM TYPE",font=bigfont2).place(x=300,y=10)
        combo= ttk.Combobox(frame22,value=["- -SELECT CITY - -","DELHI","JAIPUR","MUMBAI","AGRA","ETAH"])
        combo.current(0)
        combo.place(x=140,y=30)
        combo1= ttk.Combobox(frame22,value=["SELECT ROOM","FAMILY ROOM(4)","SINGLE BED(1)","DOUBLE BED(2)"])
        combo1.current(0)
        combo1.place(x=540,y=30)
        b1=Button(main,text="SEARCH",command=search_rooms).place(x=500,y=300)
       
        def cal(): 
                       
                def selectdate():
                        mydate=mycal.get_date()
                        print(mydate)  
                        mycal.destroy()
                        opencal.destroy()
                mycal=Calendar(main, setmode= "day",date_pattern="d/m/yy")
                mycal.place(x=700,y=300)
                opencal= Button(frame22,text="Select Date",command=selectdate)
                opencal.place(x=890,y=30)
        def cal2():
                def selectdate2():
                        mydate=mycal1.get_date()
                        print(mydate)  
                        mycal1.destroy()
                        opencal1.destroy()
                mycal1=Calendar(main, setmode= "day",date_pattern="d/m/yy")
                mycal1.place(x=890,y=300)
                opencal1= Button(frame22,text="Select Date",command=selectdate2)
                opencal1.place(x=1180,y=30)
                        
        l5=Label(frame22,text="CHECK IN",font=bigfont2).place(x=700,y=10)        
        b2=Button(frame22,text="DATE",command=cal).place(x=890,y=30)
        l6=Label(frame22,text="CHECK OUT",font=bigfont2).place(x=960,y=10)        
        b3=Button(frame22,text="DATE",command=cal2).place(x=1180,y=30)
       
        
        
        
        
        
        main.mainloop()

       
        
