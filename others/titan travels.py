from cgitb import text
from pickle import FRAME
from tkinter import *
import csv
from tkinter import messagebox
                




def AOF(): 
#===== get fn=================================================================================================================

    def GET():      
        data1=open("CUST.csv","a+",newline='')
        cw=csv.writer(data1)
        a1=a.get()
        b1=b.get()
        c1=c.get()
        d1=d.get()
        e1=e.get()
        f1=f.get()
        list_of_data=[a1,b1,c1,d1,e1,f1]
        cw.writerow(list_of_data)
        
        data1.close()
        messagebox.showinfo(title="SUCCESSFUL!",message="YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY, LOGIN TO PROCEED.")

#=========================================SUBMIT BUTTON ====================================================================================     
    
    b2=Button(window,text="SUBMIT",command=GET)
    b2.grid(row=8,column=2)
    
    x=Button(window,text="LOGIN",command=LOGIN)
    x.grid(row=9,column=2)
#===================================PACKING AND ALL==========================================================================================================
    l1=Label(window,text="USERNAME",font="aerial 10 bold").grid(row=1,column=1)
    l2=Label(window,text="PASSWORD",font="aerial 10 bold").grid(row=2,column=1)
    l3=Label(window,text="MOBILE NUMBER",font="aerial 10 bold").grid(row=3,column=1)
    l4=Label(window,text="ADDRESS",font="aerial 10 bold").grid(row=4,column=1)
    l5=Label(window,text="AGE",font="aerial 10 bold").grid(row=5,column=1)
    l6=Label(window,text="GENDER",font="aerial 10 bold").grid(row=6,column=1)
      
    a=StringVar()
    b=StringVar()
    c=StringVar()
    d=StringVar()
    e=StringVar()
    f=StringVar()       

    e1=Entry(window,textvariable=a) 
    e1.grid(row=1,column=2)
    e2=Entry(window,textvariable=b)
    e2.grid(row=2,column=2)
    e3=Entry(window,textvariable=c)
    e3.grid(row=3,column=2)
    e4=Entry(window,textvariable=d)
    e4.grid(row=4,column=2)
    e5=Entry(window,textvariable=e)
    e5.grid(row=5,column=2)
    e6=Entry(window,textvariable=f)
    e6.grid(row=6,column=2)
          
    





#======================== login =============================================================================================

def LOGIN():
    window.destroy() 

    log=Tk()
    
    log.title("LOGIN")
    log.geometry("1280x720")
    log.resizable(width=False, height=False)# don't want to resize --------------------------------
    l1=Label(log,text="LOGIN",font="aerial 30 bold").grid(row=0,column=3)
    l2=Label(log,text="Username",font="aerial 10 bold").grid(row=1,column=2) #login fxn dikh rha?
    l3=Label(log,text="Password",font="aerial 10 bold").grid(row=2,column=2)
    l9=Label(log,text="If you didn't sign in ",font="aerial 10 bold").grid(row=4,column=2,padx=2,pady=3)
    
    user=StringVar()
    passwd=StringVar()

    le1=Entry(log,textvariable=user,bd=2)
    le1.grid(row=1,column=3)  
    le2=Entry(log,textvariable=passwd,bd=2)
    le2.grid(row=2,column=3)

    def sp():
        print(user.get(),passwd.get())
        
#============================== Retrieve =====================================================================================
    
    def ret():
        u=user.get()
        p=passwd.get()
        print(u,p)
        
        data1=open("CUST.csv",'r',newline="\r\n") 
        cr=csv.reader(data1)
        authenticity=0
        for i in cr:
            if i[0]==u and i[1]==p:
                            authenticity+=1
            
            else:
                            authenticity=0
        current=authenticity

        if current ==1 :
            messagebox.showinfo(title="SUCCESSFUL!",message=f"YOU HAVE LOGGED IN SUCCESSFULLY,{u}")
                                        
        else:
            messagebox.showerror(title="ERROR!",message=" INCORRECT USERNAME/PASSWORD ")
        

    
    
    #====================================================================================================================================
    btn1=Button(log,text="SUBMIT",command=ret)
    btn1.grid(row=3,column=3,padx=2,pady=2)
    def back():
        log.destroy()
        AOF()
    
    btn2=Button(log,text="BACK",command=back)   
    btn2.grid(row=5,column=2)                                                             
    log.mainloop()
    
#======================================== main window==================================================
                
window=Tk() 
window.geometry("1280x720")
window.title("REGISTRATION")                              
window.resizable(width=False, height=False)                
f1=Frame(window,bg="grey",borderwidth=6)
f1.grid(row=0,column=3)                
l1=Label(window,text="WELCOME TO TT TRAVEL AGENCY",font="aerial 20 bold").grid(row=0,column=3)
mb1=Button(window,text="OPEN ACCOUNT",command=AOF)
mb1.grid(row=11,column=2)
mB3=Button(window,text="LOGIN",command=LOGIN)
mB3.grid(row=11,column=3)

window.mainloop()

#========================================================================================================
                
                


