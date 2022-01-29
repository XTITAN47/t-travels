# t-travels

Requirements:
pillow
tkinter
mysql-connector

To use this project:
   Go to project.py and open it
   
#Database Bug
From this code snippet:

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Titan@1067",
  database = 'titan_travels'
)

try removing 
  database = 'titan_travels'after that make sure you do not have a database as titan_travels, then run the project.py file. Now check if the database is created. Then undo the database code database = 'titan_travels'.
  (rewrite it).
