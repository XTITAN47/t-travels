from tkinter import *
from PIL import Image, ImageTk
import os

#------------------------------------------------------------------------------------------------------------------------
root = Tk()
#function
def next_page():
    root.destroy()
    
    os.system(r"C:\Users\vimar\Desktop\t-travels\page2.py")

# ADDING CANVAS 


root.geometry("1280x720")

root.title("TITAN TRAVELS")
#ADDING BACKGROUND IMAGE 


#HEADING



img = Image.open("image.jpg").resize((1280,720),)
photo = ImageTk.PhotoImage(img)
Label(root,image=photo,borderwidth='2',bg='black').place(x=0,y=0)
root.resizable(width=False, height=False)   
    
Label(root, text="WELCOME TO TITAN TRAVELS", font="comicsansms 13 bold",foreground="white",background="black", pady=15,).grid(row=0, column=3)    
#TEXT FOR LOGIN PAGE
name= Label(root, text="Name",background="black",foreground="white")
phone= Label(root, text="Phone Number",background="black",foreground="white")
email= Label(root, text="Email ID",background="black",foreground="white")
adress = Label(root, text="Adress",background="black",foreground="white")

#packing TEXT

name.grid(row=2,column=2)
phone.grid(row=3,column=2)
email.grid(row=4,column=2)
adress.grid(row=5,column=2)

# TKINTER VARIABLE FOR STORING 

namevalue= StringVar()
phonevalue= StringVar()
emailvalue= StringVar()
adressvalue= StringVar()
Hotelbookingsvalue=IntVar() 

#ENTRY  FOR A FORM

nameentry= Entry(root, textvariable=namevalue)
phoneentry= Entry(root, textvariable=phonevalue)
emailentry= Entry(root, textvariable=emailvalue)
adressentry= Entry(root, textvariable=adressvalue)

#Entry packing

nameentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
adressentry.grid(row=5, column=3)

#CHECKBOX

#submit button
Button(text="Submit", command=next_page).grid(row=8,column=3,pady=16)


root.mainloop()
