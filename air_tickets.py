from tkinter import *
from tkinter import ttk
import csv
from PIL import Image, ImageTk
from tkinter.font import Font
import mysql.connector

def air():
    cu = mydb.cursor()
    cu.execute('SELECT * FROM AEROPLANES;')
    data = cu.fetchall()
    noOfAvFlights = 0
    departure=[]
    destination=[]
    for i in data:
        noOfAvFlights +=1
        if i[2] not in departure:
            departure.append(i[2])
        if i[3] not in destination:
            destination.append(i[3])
        print(i)

#================================================== SEARCH and DISPLAY ===================================================
    def search():
        frame23=Frame(airwin,width=900,height=300,highlightbackground="black",highlightthickness=2)
        frame23.place(x=200,y=300)
        l1=Label(frame22,text="FROM",font=bigfont2)

        

        pass

#===============================================================================================================================                                             
                    
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
                size=25,
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
    button=Button(airwin,text="SEARCH",command=search,width=126)
    button.place(x=202,y=280)
    airwin.mainloop()

if __name__ == '__main__':
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Titan@1067",
    database='titan_travels')
    air()
