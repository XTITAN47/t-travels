from tkinter import *
import tkinter
from PIL import Image, ImageTk
import time
from tkinter import ttk
import datetime
import random
import tkinter.messagebox
from views import *

#------------------------------------------------------------------------------------------------------------------------
root = Tk()
    
#settings
root.geometry("1540x800")
root.title("TITAN TRAVELS")
#img = Image.open("static\\image.jpg").resize((800,600),)
#photo = ImageTk.PhotoImage(img)
#Label(root,image=photo,borderwidth='2',bg='black').place(x=0,y=0)
root.resizable(width=False, height=False)

#functions 

def home():
    def login():
        def profile():
            name=name_var.get()
            password=passw_var.get()
            if name is not None:
                userauth = authenticate(name,password)
                if userauth ==True:
                    f3 = Frame(root,background='lightblue',width=1350,height=1350)
                    f3.grid()
                    DateOfOrder=StringVar()
                    DateOfOrder.set(time.strftime("%d/%m/%y"))
                    Receipt_Re=StringVar()
                    PaidTax=StringVar()
                    SubTotal=StringVar()
                    TotalCost=StringVar()
                    var1=IntVar()
                    var2=IntVar()
                    var3=IntVar()
                    var4=IntVar()
                    var5=IntVar()
                    var6=IntVar()
                    var7=IntVar()
                    var8=IntVar()
                    var9=IntVar()
                    var10=StringVar()
                    var11=StringVar()
                    var12=StringVar()
                    var13=StringVar()
                    FirstName=StringVar()
                    LastName=StringVar()
                    Address=StringVar()
                    PostCode=StringVar()
                    Telephone=StringVar()
                    phone=StringVar()
                    Email=StringVar()
                    AirportTax=StringVar()
                    Mile=StringVar()
                    Insurance=StringVar()
                    Luggage=StringVar()
                    Standard=StringVar()
                    Economy=StringVar()
                    FirstClass=StringVar()
                    AirportTax.set('0')
                    Mile.set('0')
                    Insurance.set('0')
                    Luggage.set('0')
                    Standard.set('0')
                    Economy.set('0')
                    FirstClass.set('0')

                    Tops = Frame(f3,bd=20,width=1350,relief=RIDGE)
                    Tops.pack(side=TOP)
                    TitleLbl = Label(Tops,width=22, font=('arial',70,'bold'),text=" Titan Travels ",padx=1)
                    TitleLbl.grid()

                    UserDetailsFrame=Frame(f3,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
                    UserDetailsFrame.pack(side=BOTTOM)
                    FrameDetails=Frame(UserDetailsFrame,width=880,height=400,bd=10,relief=RIDGE)
                    FrameDetails.pack(side=LEFT)


                    CustomerName=LabelFrame(FrameDetails,width=150,height=250,bd=20,font=('arial',12,'bold'),text='Customer Name',relief=RIDGE)
                    CustomerName.grid(row=0,column=0)
                    TravelFrame=LabelFrame(FrameDetails,width=300,height=250,bd=10,font=('arial',12,'bold'),text='Travel Details',relief=RIDGE)
                    TravelFrame.grid(row=0,column=1)
                    TicketFrame=LabelFrame(FrameDetails,width=300,height=150,relief=RIDGE)
                    TicketFrame.grid(row=1,column=0)
                    CostFrame=LabelFrame(FrameDetails,width=150,height=150,relief=RIDGE)
                    CostFrame.grid(row=1,column=1)

                    ReceiptButtonFrame=Frame(UserDetailsFrame,width=450,height=400,bd=10,pady=5,relief=RIDGE)
                    ReceiptButtonFrame.pack(side=RIGHT)
                    ReceiptFrame=LabelFrame(ReceiptButtonFrame,width=350,height=300,font=('arial',12,'bold'),text='Receipt',relief=RIDGE)
                    ReceiptFrame.grid(row=0,column=0)
                    ButtonFrame=LabelFrame(ReceiptButtonFrame,width=350,height=100,relief=RIDGE)
                    ButtonFrame.grid(row=1,column=0)

                    FirstNameLbl = Label(CustomerName, font=('arial',14,'bold'),text="First Name",bd=7)
                    FirstNameLbl.grid(row=0,column=0,sticky=W)
                    FirstNameTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=FirstName,bd=7,insertwidth=2,justify=RIGHT)
                    FirstNameTxt.grid(row=0,column=1)

                    LastNameLbl = Label(CustomerName, font=('arial',14,'bold'),text="Last  Name",bd=7)
                    LastNameLbl.grid(row=1,column=0)
                    LastNameTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=LastName,bd=7,insertwidth=2,justify=RIGHT)
                    LastNameTxt.grid(row=1,column=1)

                    AddressLbl = Label(CustomerName, font=('arial',14,'bold'),text="Address",bd=7)
                    AddressLbl.grid(row=2,column=0)
                    AddressTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
                    AddressTxt.grid(row=2,column=1)

                    PostalLbl = Label(CustomerName, font=('arial',14,'bold'),text="Postal Code",bd=7)
                    PostalLbl.grid(row=3,column=0)
                    PostalTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=PostCode,bd=7,insertwidth=2,justify=RIGHT)
                    PostalTxt.grid(row=3,column=1)

                    TelephoneLbl = Label(CustomerName, font=('arial',14,'bold'),text="Telephone",bd=7)
                    TelephoneLbl.grid(row=4,column=0)
                    TelephoneTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
                    TelephoneTxt.grid(row=4,column=1)

                    MobileLbl = Label(CustomerName, font=('arial',14,'bold'),text="Mobile No.",bd=7)
                    MobileLbl.grid(row=5,column=0)
                    MobileTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=phone,bd=7,insertwidth=2,justify=RIGHT)
                    MobileTxt.grid(row=5,column=1)

                    EmailLbl = Label(CustomerName, font=('arial',14,'bold'),text="E-mail",bd=7)
                    EmailLbl.grid(row=6,column=0)
                    EmailTxt = Entry(CustomerName, font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
                    EmailTxt.grid(row=6,column=1)

                    DepartureLbl = Label(TravelFrame, font=('arial',14,'bold'),text="Departure",bd=7)
                    DepartureLbl.grid(row=0,column=0,sticky=W)
                    DepartureCbo=ttk.Combobox(TravelFrame,textvariable=var11,state='readonly',font=('arial',20,'bold'),width=14)
                    DepartureCbo['values'] = ('','Delhi','Mumbai')
                    DepartureCbo.current(0)
                    DepartureCbo.grid(row=0,column=1)

                    DestinationLbl = Label(TravelFrame, font=('arial',14,'bold'),text="Destination",bd=7)
                    DestinationLbl.grid(row=1,column=0,sticky=W)
                    DestinationCbo=ttk.Combobox(TravelFrame,textvariable=var12,state='readonly',font=('arial',20,'bold'),width=14)
                    DestinationCbo['values'] = ('','Delhi','Mumbai','USA','France')
                    DestinationCbo.current(0)
                    DestinationCbo.grid(row=1,column=1)

                    AccommodationLbl = Label(TravelFrame, font=('arial',14,'bold'),text="Accomodation",bd=7)
                    AccommodationLbl.grid(row=2,column=0,sticky=W)
                    AccommodationCbo=ttk.Combobox(TravelFrame,textvariable=var13,state='readonly',font=('arial',20,'bold'),width=14)
                    AccommodationCbo['values'] = ('','1','2','3','4')
                    AccommodationCbo.current(0)
                    AccommodationCbo.grid(row=2,column=1)

                    AirportTaxChk=Checkbutton(TravelFrame,text='Airport Tax',variable=var1,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=3,column=0,sticky=W)
                    AirportTaxTxt = Entry(TravelFrame, font=('arial',14,'bold'),textvariable=AirportTax,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    AirportTaxTxt.grid(row=3,column=1)

                    MileTaxChk=Checkbutton(TravelFrame,text='Air Mile',variable=var2,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=4,column=0,sticky=W)
                    MileTaxTxt = Entry(TravelFrame, font=('arial',14,'bold'),textvariable=Mile,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    MileTaxTxt.grid(row=4,column=1)

                    InsuranceChk=Checkbutton(TravelFrame,text='Insurance',variable=var3,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=5,column=0,sticky=W)
                    InsuranceTxt = Entry(TravelFrame, font=('arial',14,'bold'),textvariable=Insurance,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    InsuranceTxt.grid(row=5,column=1)

                    LuggageChk=Checkbutton(TravelFrame,text='Extra Luggage',variable=var4,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=6,column=0,sticky=W)
                    LuggageTxt = Entry(TravelFrame, font=('arial',14,'bold'),textvariable=Luggage,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    LuggageTxt.grid(row=6,column=1)

                    PaidTaxLbl = Label(CostFrame, font=('arial',14,'bold'),text="Paid Tax\t\t",bd=7)
                    PaidTaxLbl.grid(row=0,column=2,sticky=W)
                    PaidTaxTxt = Entry(CostFrame, font=('arial',14,'bold'),textvariable=PaidTax,bd=7,width=26,justify=RIGHT)
                    PaidTaxTxt.grid(row=0,column=3)

                    SubTotalLbl = Label(CostFrame, font=('arial',14,'bold'),text="Sub Total",bd=7)
                    SubTotalLbl.grid(row=1,column=2,sticky=W)
                    SubTotalTxt = Entry(CostFrame, font=('arial',14,'bold'),textvariable=SubTotal,bd=7,width=26,justify=RIGHT)
                    SubTotalTxt.grid(row=1,column=3)

                    TotalCostLbl = Label(CostFrame, font=('arial',14,'bold'),text="Total Cost",bd=7)
                    TotalCostLbl.grid(row=2,column=2,sticky=W)
                    TotalCostTxt = Entry(CostFrame, font=('arial',14,'bold'),textvariable=TotalCost,bd=7,width=26,justify=RIGHT)
                    TotalCostTxt.grid(row=2,column=3)

                    StandardChk=Checkbutton(TicketFrame,text='Standard',variable=var5,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=0,column=0,sticky=W)
                    StandardTxt = Entry(TicketFrame, font=('arial',14,'bold'),textvariable=Mile,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    StandardTxt.grid(row=0,column=1)

                    SingleChk=Checkbutton(TicketFrame,text='Single',variable=var6,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=0,column=2,sticky=W)


                    EconomyChk=Checkbutton(TicketFrame,text='Economy',variable=var7,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=1,column=0,sticky=W)
                    EconomyTxt = Entry(TicketFrame, font=('arial',14,'bold'),textvariable=Mile,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    EconomyTxt.grid(row=1,column=1)

                    ReturnChk=Checkbutton(TicketFrame,text='Return',variable=var8,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=1,column=2,sticky=W)


                    FirstClassChk=Checkbutton(TicketFrame,text='First Class',variable=var9,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=2,column=0)
                    FirstClassTxt = Entry(TicketFrame, font=('arial',14,'bold'),textvariable=Mile,bd=7,insertwidth=2,justify=RIGHT,state=DISABLED)
                    FirstClassTxt.grid(row=2,column=1)

                    SpecialNeedsChk=Checkbutton(TicketFrame,text='Special Needs',variable=var10,onvalue=1,offvalue=0,font=('arial',16,'bold')).grid(row=2,column=2,sticky=W)


                    #Receipt----------------------
                    ReceiptTxt=Text(ReceiptFrame,width=60,height=21,font=('arial',8,'bold'))
                    ReceiptTxt.grid(row=0,column=0)

                    Totalbtn=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Total').grid(row=0,column=0)
                    Receiptbtn=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Receipt').grid(row=0,column=1)
                    Resetbtn=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Reset').grid(row=0,column=2)
                    Exitbtn=Button(ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=4,text='Exit').grid(row=0,column=3)

                    



        '''login'''
        f2 = Frame(root,background="black")
        f2.place(x=0,y=0,height=600,width=800)
        name_var = StringVar()
        passw_var = StringVar()
        name_label = Label(f2, text = 'Username', font=('calibre',10, 'bold')).pack()
        name_entry = Entry(f2,textvariable = name_var, font=('calibre',10,'normal')).pack()
        passw_label = Label(f2, text = 'Password', font = ('calibre',10,'bold')).pack()
        passw_entry= Entry(f2, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*').pack()
        sub_btn=Button(f2,text = 'Submit', command = profile).pack()
        back_btn=Button(f2,text = 'Back', command = profile).pack()
        f2.pack_forget()
    
    def register():
        '''register'''
        f2 = Frame(root,background="black")
        f2.place(x=0,y=0,height=600,width=800)
        Label(f2, text="LOGIN", font="comicsansms 13 bold",foreground="white",background="black", pady=15,).pack() 
        userl= Label(f2, text="UserID",background="black",foreground="white").pack()
        user = Entry(f2,bd =2,bg='white').pack
        phonel= Label(f2, text="Phone Number",background="black",foreground="white").pack()
        phone = Entry(f2,bd =2,bg='white').pack
        emaill= Label(f2, text="Email ID",background="black",foreground="white").pack()
        email = Entry(f2,bd =2,bg='white').pack
        psw1l = Label(f2, text="Password",background="black",foreground="white").pack()
        psw1 = Entry(f2,bd =2,bg='white').pack
        psw2l = Label(f2, text="Confirm Password",background="black",foreground="white").pack()
        psw2 = Entry(f2,bd =2,bg='white').pack
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
