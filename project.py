import random
from datetime import date
import mysql.connector
import datetime
from tabulate import tabulate
con=mysql.connector.connect(user='root',
                            passwd='titan@1067',
                            host='localhost')
cur=con.cursor()
cur.execute('create database if not exists Mylibrary')
cur.execute('use Mylibrary')
cur.execute("create table if not exists study(book_CODE int primary key,book_name varchar(20),SUBJECT varchar(20),CLASS int,PUBLICATION VARCHAR(40),stock int)")
cur.execute("create table if not exists issuers_data(ISSUERS INT,book_CODE int,date varchar(20),late_by int,charges int)")
def addbook():
    print('''
          
          ADD BOOK
          ''')
    bookname=input("Enter book name:")
    subject=input("Enter subject of book:")
    CLASS=int(input("Enter class of book:"))
    PUBLICATION=input("Enter the name of publication:")
    stock=int(input("Enter the quantity of books:"))
    bookno=random.randint(0,100000)
    cur.execute("insert into STUDY values({},'{}','{}',{},'{}',{})".format(bookno,bookname,subject,CLASS,PUBLICATION,stock))
    con.commit()
def deletebook():
    bookno=int(input("Enter BOOK CODE number:"))
    cur.execute("select * from issuers_data where book_code='{}'".format(bookno))
    data=cur.fetchall()
    l=[]
    for i in data:
        l.append(i)
    if l==[]:
        q = "delete from study where book_CODE='{}'".format(bookno)
        cur.execute(q)
        con.commit()
    else:
        cur.execute("update study set stock=0")
def show_all():
    query="select * from STUDY"
    cur.execute(query)
    data=cur.fetchall()
    l=[]
    l2=['BOOK CODE','NAME','SUBJECT','CLASS','PUBLICATION','STOCKS']
    for i in data:
        l.append(i)
    print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
def search_by_name():
    n=input("Enter Name of the book:")
    query="select * from STUDY where book_name='{}'".format(n)
    cur.execute(query)
    data=cur.fetchall()
    l=[]
    l2=['BOOK CODE','NAME','SUBJECT','CLASS','PUBLICATION','STOCKS']
    for i in data:
        l.append(i)
    if l==[]:
        print('NO BOOK AVAILABLE BY GIVEN NAME')
    else:
        print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
def search_by_SUBJECT():
    n=input("Enter SUBJECT of the book:")
    query="select * from STUDY where SUBJECT='{}'".format(n)
    cur.execute(query)
    data=cur.fetchall()
    l=[]
    l2=['BOOK CODE','NAME','SUBJECT','CLASS','PUBLICATION','STOCKS']
    for i in data:
        l.append(i)
    if l==[]:
        print('NO BOOK AVAILABLE BY GIVEN SUBJECT')
    else:
        print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
def search_by_PUBLICATION():
    n=input("Enter PUBLICATION of the book:")
    query="select * from STUDY where PUBLICATION='{}'".format(n)
    cur.execute(query)
    data=cur.fetchall()
    l=[]
    l2=['BOOK CODE','NAME','SUBJECT','CLASS','PUBLICATION','STOCKS']
    for i in data:
        l.append(i)
    if l==[]:
        print('NO BOOK AVAILABLE BY GIVEN PUBLICATION')
    else:
        print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
def search_by_CLASS():
    n=int(input("Enter PUBLICATION of the book:"))
    query="select * from STUDY where CLASS='{}'".format(n)
    cur.execute(query)
    data=cur.fetchall()
    l=[]
    l2=['BOOK CODE','NAME','SUBJECT','CLASS','PUBLICATION','STOCKS']
    for i in data:
        l.append(i)
    if l==[]:
        print('NO BOOK AVAILABLE BY GIVEN CLASS')
    else:
        print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
def issuebook():
    book_code=int(input("Enter book code to issue:"))
    cur.execute("Select * from study where book_code='{}'".format(book_code))
    data=cur.fetchall()
    if data[0][5]==0:
        print("not in stock right now...")
    else:
        stock=data[0][5]-1
        USER=int(input("Enter the issuer admission number:"))
        today=datetime.date.today()
        q="Update STUDY set stock={} where book_code={}".format(stock,book_code)
        qu="insert into ISSUERS_DATA VALUES({},'{}','{}',0,0)".format(USER,book_code,today)
        cur.execute(qu)
        cur.execute(q)
        con.commit()
def add_stocks():
    book=int(input("Enter the name of book code:"))
    stock=int(input("Enter stocks for the book:"))
    cur.execute("select * from study where book_code={}".format(book))
    data=cur.fetchall()
    newstock=stock+int(data[0][5])
    cur.execute("update study set stock={} where book_code={}".format(newstock,book))
    con.commit()
def show_issuers():
    query="select issuers,book_code,date from ISSUERS_DATA"
    cur.execute(query)
    data=cur.fetchall()
    l=[]
    l2=['ADM NO. OF ISSUER','BOOK CODE','DATE OF ISSUE']
    for E in data:
        l.append(E)
    print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
def issuers_SEARCH():
    n=int(input("Enter issuer's admission number:"))
    query="select * from ISSUERS_DATA where ISSUERS={}".format(n)
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        INITIAL=str(datetime.date.today())
        a=INITIAL.split('-')
        y1=int(a[0])
        m1=int(a[1])
        d1=int(a[2])
        initialdate=date(y1,m1,d1)
        FINAL=str(i[2])
        a1=FINAL.split('-')
        y2=int(a1[0])
        m2=int(a1[1])
        d2=int(a1[2])
        finaldate=date(y2,m2,d2)
        d=initialdate-finaldate
        DAYS=(d.days)-7
        fine=DAYS*20
        if DAYS<=0:
            l=[]
            l2=['ADM NO. OF ISSUER','BOOK CODE','DATE OF ISSUE','LATE BY DAYS','CHARGES']
            for E in data:
                l.append(E)
            if l==[]:
                print('NO BOOK IS ISSUED BY GIVEN ADMISSION NUMBER')
            else:
                print(tabulate(l,headers=l2,tablefmt="fancy_grid",numalign='center'))
        else:
            cur.execute("update issuers_data set late_by='{}',CHARGES='{}'".format(DAYS,fine))
            con.commit()
            query="select * from ISSUERS_DATA where ISSUERS='{}'".format(n)
            cur.execute(query)
            dat=cur.fetchall()
            l3=[]
            l4=['ADM NO. OF ISSUER','BOOK CODE','DATE OF ISSUE','LATE BY DAYS','CHARGES']
            cur.execute("select sum(charges) from issuers_data")
            da=cur.fetchall()
            total=['Total fine--------->       ',da[0][0]]
            for E in dat:
                l3.append(E)
            if l3==[]:
                print('NO BOOK IS ISSUED BY GIVEN ADMISSION NUMBER')
            else:
                print(tabulate(l3,headers=l4,tablefmt="fancy_grid",numalign='center'))
                print(tabulate([total],tablefmt="fancy_grid",numalign='center'))
def returnbook():
    issuer=int(input("Enter issuer's admission number:"))
    book=int(input("Enter the book code to return:"))
    cur.execute("select * from study where book_code={}".format(book))
    data=cur.fetchall()
    a=data[0][5]+1
    cur.execute("update study set stock={} where book_code={}".format(a,book))
    con.commit()
    cur.execute("delete from issuers_data where book_code={} and issuers={}".format(book,issuer))
    con.commit()
def Change_book_name():
    book=int(input("Enter the book code to edit:"))
    n=input("Enter the new name for book:")
    cur.execute("update study set book_name='{}' where book_code={}".format(n,book))
    con.commit()
def Change_book_SUBJECT():
    book=int(input("Enter the book code to edit:"))
    n=input("Enter the new subject for book:")
    cur.execute("update study set subject='{}' where book_code={}".format(n,book))
    con.commit()
def Change_book_CLASS():
    book=int(input("Enter the book code to edit:"))
    n=input("Enter the new class for book:")
    cur.execute("update study set class={} where book_code={}".format(n,book))
    con.commit()
def Change_book_PUBLICATION():
    book=int(input("Enter the book code to edit:"))
    n=input("Enter the new publication for book:")
    cur.execute("update study set publication='{}' where book_code={}".format(n,book))
    con.commit()
w='y'
while w in ('y','Y'):
    print(tabulate([['1-> SHOW ALL BOOKS'],
                    ['2-> ADD BOOKS TO OUR LIBRARY'],
                    ['3-> ISSUE BOOK'],
                    ['4-> CHANGE BOOK DETAILS'],
                    ['5-> RETURN BOOK'],
                    ['6-> ISSUER\'S DATA'],
                    ['7-> DELETE BOOK'],
                    ['8-> EXIT']],
                   headers=['           MENU           '],tablefmt="fancy_grid"))
    q=int(input("ENTER YOUR CHOICE:"))
    if q==1:
        show_all()
    elif q==2:
        addbook()
    elif q==3:
        wh='y'
        while wh in ('y','Y'):
            print(tabulate([['1-> SEARCH BY NAME OF BOOK'],
                            ['2-> SEARCH BY SUBJECT OF BOOK'],
                            ['3-> SEARCH BY CLASS OF BOOK'],
                            ['4-> SEARCH BY PUBLICATION OF BOOK'],
                            ['5-> ALL BOOKS'],
                            ['6->EXIT']],
                           headers=['           SEARCH BOOKS TO ISSUE           '],tablefmt="fancy_grid"))
            qu=int(input("ENTER YOUR CHOICE:"))
            if qu==1:
                search_by_name()
                t=input("Do you want to issue any book from here(y/n):")
                if t in ('y','Y'):
                    issuebook()
                    print("BOOK ISSUED SUCCESSFULLY...")
            elif qu==2:
                search_by_SUBJECT()
                t=input("Do you want to issue any book from here(y/n):")
                if t in ('y','Y'):
                    issuebook()
                    print("BOOK ISSUED SUCCESSFULLY...")
            elif qu==3:
                search_by_CLASS()
                t=input("Do you want to issue any book from here(y/n):")
                if t in ('y','Y'):
                    issuebook()
                    print("BOOK ISSUED SUCCESSFULLY...")
            elif qu==4:
                search_by_PUBLICATION()
                t=input("Do you want to issue any book from here(y/n):")
                if t in ('y','Y'):
                    issuebook()
                    print("BOOK ISSUED SUCCESSFULLY...")
            elif qu==5:
                show_all()
                t=input("Do you want to issue any book from here(y/n):")
                if t in ('y','Y'):
                    issuebook()
                    print("BOOK ISSUED SUCCESSFULLY...")
            elif que==6:
                wh=='D'
            else:
                print('Invalid Input.....')
            wh=input("Do you want to issue another book(y/n):")
    elif q==4:
        wha='y'
        while wha in ('y','Y'):
            print(tabulate([['1-> SEARCH BY NAME OF BOOK'],
                            ['2-> SEARCH BY SUBJECT OF BOOK'],
                            ['3-> SEARCH BY CLASS OF BOOK'],
                            ['4-> SEARCH BY PUBLICATION OF BOOK'],
                            ['5-> ALL BOOKS'],
                            ['6->EXIT']],
                            headers=['      SEARCH BOOKS TO EDIT DETAILS       '],tablefmt="fancy_grid"))
            que=int(input("ENTER YOUR CHOICE:"))
            if que==1:
                search_by_name()
                te=input("Do you want to edit details of books from here(y/n):")
                if te in ('y','Y'):
                    print(tabulate([['1-> CHANGE NAME OF BOOK'],
                                    ['2-> CHANGE NAME OF SUBJECT OF BOOK'],
                                    ['3-> CHANGE NAME OF CLASS OF BOOK'],
                                    ['4-> CHANGE NAME OF PUBLICATION OF BOOK'],
                                    ['5->EXIT']],
                                   headers=['             EDIT BOOK DETAILS               '],tablefmt="fancy_grid"))
                    ques=int(input("ENTER YOUR CHOICE:"))
                    if ques==1:
                        Change_book_name()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==2:
                        Change_book_SUBJECT()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==3:
                        Change_book_CLASS()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==4:
                        Change_book_PUBLICATION()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==5:
                        print('')
                    else:
                        print('Invalid Input.....')
            elif que==2:
                search_by_SUBJECT()
                te=input("Do you want to edit details of books from here(y/n):")
                if te in ('y','Y'):
                    print(tabulate([['1-> CHANGE NAME OF BOOK'],
                                    ['2-> CHANGE NAME OF SUBJECT OF BOOK'],
                                    ['3-> CHANGE NAME OF CLASS OF BOOK'],
                                    ['4-> CHANGE NAME OF PUBLICATION OF BOOK'],
                                    ['5->EXIT']],
                                   headers=['             EDIT BOOK DETAILS               '],tablefmt="fancy_grid"))
                    ques=int(input("ENTER YOUR CHOICE:"))
                    if ques==1:
                        Change_book_name()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==2:
                        Change_book_SUBJECT()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==3:
                        Change_book_CLASS()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==4:
                        Change_book_PUBLICATION()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==5:
                        print('')
                    else:
                        print('Invalid Input.....')
            elif que==3:
                search_by_CLASS()
                te=input("Do you want to edit details of books from here(y/n):")
                if te in ('y','Y'):
                    print(tabulate([['1-> CHANGE NAME OF BOOK'],
                                    ['2-> CHANGE NAME OF SUBJECT OF BOOK'],
                                    ['3-> CHANGE NAME OF CLASS OF BOOK'],
                                    ['4-> CHANGE NAME OF PUBLICATION OF BOOK'],
                                    ['5->EXIT']],
                                   headers=['             EDIT BOOK DETAILS               '],tablefmt="fancy_grid"))
                    ques=int(input("ENTER YOUR CHOICE:"))
                    if ques==1:
                        Change_book_name()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==2:
                        Change_book_SUBJECT()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==3:
                        Change_book_CLASS()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==4:
                        Change_book_PUBLICATION()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==5:
                        print('')
                    else:
                        print('Invalid Input.....')
            elif que==4:
                search_by_PUBLICATION()
                te=input("Do you want to edit details of books from here(y/n):")
                if te in ('y','Y'):
                    print(tabulate([['1-> CHANGE NAME OF BOOK'],
                                    ['2-> CHANGE NAME OF SUBJECT OF BOOK'],
                                    ['3-> CHANGE NAME OF CLASS OF BOOK'],
                                    ['4-> CHANGE NAME OF PUBLICATION OF BOOK'],
                                    ['5->EXIT']],
                                   headers=['             EDIT BOOK DETAILS               '],tablefmt="fancy_grid"))
                    ques=int(input("ENTER YOUR CHOICE:"))
                    if ques==1:
                        Change_book_name()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==2:
                        Change_book_SUBJECT()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==3:
                        Change_book_CLASS()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==4:
                        Change_book_PUBLICATION()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==5:
                        print('')
                    else:
                        print('Invalid Input.....')
            elif que==5:
                show_all()
                t=input("Do you want to edit details of books from here(y/n):")
                if te in ('y','Y'):
                    print(tabulate([['1-> CHANGE NAME OF BOOK'],
                                    ['2-> CHANGE NAME OF SUBJECT OF BOOK'],
                                    ['3-> CHANGE NAME OF CLASS OF BOOK'],
                                    ['4-> CHANGE NAME OF PUBLICATION OF BOOK'],
                                    ['5->EXIT']],
                                   headers=['             EDIT BOOK DETAILS               '],tablefmt="fancy_grid"))
                    ques=int(input("ENTER YOUR CHOICE:"))
                    if ques==1:
                        Change_book_name()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==2:
                        Change_book_SUBJECT()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==3:
                        Change_book_CLASS()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==4:
                        Change_book_PUBLICATION()
                        print("DETAILS CHANGED SUCCESSFULLY...")
                    elif ques==5:
                        print('')
                    else:
                        print('Invalid Input.....')
            elif que==6:
                wha=='D'
            else:
                print('Invalid Input.....')
            wha=input("Do you want to edit details of another book(y/n):")
    elif q==6:
        show_issuers()
    elif q==5:
        issuers_SEARCH()
        returnbook()
        print("BOOK RETURNED SUCCESSFULLY")
    elif q==7:
        deletebook()
    elif q==8:
        print(":)")
    else:
        print('Invalid Input.....')
    w=input('Do you want to continue to Main Menu(y/n):')
