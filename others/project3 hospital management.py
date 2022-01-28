import mysql.connector
from tabulate import *
mydb=mysql.connector.connect(
    user="root",
    host="localhost",
    password="titan@1067",
    database="vimarsh2"
)
cus=mydb.cursor()
def main():
    print("Welcome to the hospital")
    ch=int(input("Type 1 if you are hospital staff member\nType 2 if you are patient\nEnter:"))
    if ch==1:
        print("How may I assist you")
        staff()
    elif ch==2:
        p=int(input("enter patient ID:"))
        print("How can we serve you?")
        patient(p)
    else:
        print("inappropriate entry please try again......")
        main()
def staff():
    print("enter 1 for medicines info\nenter 2 for staff info\nType 3 to go back")
    stch=int(input("enter:"))#staff choice
    if stch==1:
        cus.execute("select * from medicines")
        x=cus.fetchall()
        a=[]
        for i  in x:
            a.append(i)
        h=["Sr_no.","Medicine","Price","Status"]
        print(tabulate(a,h,tablefmt="fancy_grid"))
        staff()
    elif stch==2:
        cus.execute("select * from staff")
        x=cus.fetchall()
        a=[]
        for i  in x:
            a.append(i)
        h=["Staff ID","Name","Post","Availability"]
        print(tabulate(a,h,tablefmt="fancy_grid"))
        staff()
    elif stch==3:
        main()
    else:
        print("inappropriate choice please try again.......")
        staff()
def patient(ID):
    print("type 1 for medical expenses\ntype 2 for checking availability of doctors\ntype 3 for initiallising discharge procedure\ntype 4 for checking medicines available currently")
    ptch=int(input("enter:"))#patient choice
    if ptch==1:
        act="select total_billing from patient where patient_id = %s"
        val=(ID,)
        cus.execute(act,val)
        x=cus.fetchall()
        for i in x:
            print("total billing : i")

    elif ptch==2:
        pass
    elif ptch==3:
        pass
    elif ptch==4:
        med=input("enter the name of the medicine:")
        act="select availability from medicines where medicine=%s"
        val=(med,)
        cus.execute(act,val)
        x=cus.fetchall()
        for i in x:
            print(i[0])
    else:
        print("inappropriate choice please try again.......")
        patient(ID)
def medicines():
    print("what you want to do?")
    n=int(input("type 1 for checking medicine availability and price\ntype 2 for updating stock and prices\ntype 3 for entering new medicine\ntype 4 to go back\nenter choice:"))
    if n==1:
        cus.execute("select * from medicines")
        x=cus.fetchall()
        a=[]
        for i  in x:
            a.append(i)
        h=["Sr_no.","Medicine","Price","Status"]
        print(tabulate(a,h,tablefmt="fancy_grid"))
        medicines()
    elif n==2:
        med=input("enter the name of the medicine:")
        sta=input("enter the status of the given medicine:")
        val=[sta,med]
        act="update medicines set availability=%s where medicine=%s"
        cus.execute(act,val)
        mydb.commit()
        print("stock updated")
        medicines()
    elif n==3:
        med=input("enter name of the medicine:")
        price=int(input("enter price of the medicine:"))
        act="insert into medicines (medicine,price,availability) values(%s,%s,%s)"
        val=(med,price,"available")
        cus.execute(act,val)
        mydb.commit()
        print("record entered successfully ;)")
        medicines()
    elif n==4:
        main()
    else:
        print("invalid entry please try again")
        medicines()
main()