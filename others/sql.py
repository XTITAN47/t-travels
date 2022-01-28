import mysql.connector

#sql working:_________________________

mydb = mysql.connector.connect(host="localhost", user="root",passwd="titan@1067",database="vimarsh")


#_________________________________________________________
mycursor = mydb.cursor()
mycursor.execute("select * from titan_login")
mycursor.Commit()

for i in mycursor:
    print(i)
    
"""   cursor=db.cursor()
        cursor.execute("create table if not exist registration(USERNAME VARCHAR(20), PASSWORD VARCHAR(20), MOBILE_NUMBER INTEGER(10), ADRESS VARCHAR(50), AGE INTEGER(2), GENDER VARCHAR(20)")
        insert="INSERT INTO REGISTRATION VALUES(%s,%s)"
        cursor.execute(insert,list_of_data)
        cursor.execute("select * from registration")
        
        messagebox.showinfo(title="SUCCESSFUL!",message="YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY, LOGIN TO PROCEED.")    """