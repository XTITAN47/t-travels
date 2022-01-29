import mysql.connector
import pickle
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Titan@1067",
)
def pushDBtoDAT():
    cu = mydb.cursor()
    cu.execute('SELECT * FROM users;')
    data = cu.fetchall()
    with open(r'data\db\users.dat','wb') as f:
        for i in data:
            pickle.dump(i,f)

def pushDATtoDB():
    cu = mydb.cursor()
    temp =[]
    with open(r'data\db\users.dat','rb') as f:
        while True:
            try:
                i = pickle.load(f)
                temp.append(i)
            except EOFError:
                break

if __name__ =='__main__':
    pushDBtoDAT()