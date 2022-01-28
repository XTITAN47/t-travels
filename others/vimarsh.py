from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()    
#settings
root.geometry("800x600")
root.title("TITAN TRAVELS")
img = Image.open("material\\image.jpg").resize((800,600),)
photo = ImageTk.PhotoImage(img)
#Label(root,image=photo,borderwidth='2',bg='black').place(x=0,y=0)
root.resizable(width=False, height=False)
#functions
def home():
    def login():
        def profile():
            pass
        '''login'''
        f2 = Frame(root,background="black")
        f2.place(x=0,y=0,height=600,width=800)
        Label(f2, text="LOGIN", font="comicsansms 13 bold",foreground="white",background="white", pady=15,).pack() 
        userid= Label(f2, text="User ID",background="black",foreground="white").pack()
        userid = Entry()
        psw= Label(f2, text="Password",background="black",foreground="white").pack()
        psw = Entry()
        Button(f2,text="Back", command=home).pack()
        Button(f2,text="Submit", command=profile).pack()
        f2.pack_forget()    
    def register():
        '''register'''
        f2 = Frame(root,background="black")
        f2.place(x=0,y=0,height=600,width=800)
        Label(f2, text="LOGIN", font="comicsansms 13 bold",foreground="white",background="black", pady=15,).pack() 
        name= Label(f2, text="Name",background="black",foreground="white").pack()
        name = Entry()
        phone= Label(f2, text="Phone Number",background="black",foreground="white").pack()
        phone = Entry()
        email= Label(f2, text="Email ID",background="black",foreground="white").pack()
        email = Entry()
        psw1 = Label(f2, text="Password",background="black",foreground="white").pack()
        psw1 = Entry()
        psw2 = Label(f2, text="Confirm Password",background="black",foreground="white").pack()
        psw2 = Entry()
        Button(f2,text="Back", command=home).pack()
        Button(f2,text="Submit", command=login).pack()
        f2.pack_forget()
    '''home'''
    f1 = Frame(root,background="black")
    f1.place(x=0,y=0,height=600,width=800)
    Label(f1, text="TITAN TRAVELS", font="comicsansms 13 bold",foreground="white",background='black').pack(pady=40)
    Button(f1,text="Login", command=login).pack()
    Button(f1,text="Register", command=register).pack()
    f1.pack_forget()
home()
root.mainloop()