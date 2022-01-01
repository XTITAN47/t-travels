from tkinter import*

root =Tk()

canvas = Canvas(width=400, height=250)
canvas.pack()

photo= PhotoImage(file='C:\\Users\\vimar\\Desktop\\python practise\\hz7dbu18hhn61.png')
Label(root, text="WELCOME TO TITAN TRAVELS", font="comicsansms 13 bold",foreground="white",background="black", pady=15,).grid(row=0, column=3) 
canvas.create_image(0,0, image=photo, anchor=NW)

root.mainloop()