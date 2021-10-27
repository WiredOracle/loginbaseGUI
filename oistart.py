from tkinter import *
import os
from PIL import ImageTk

root = Tk()

def data():
    username = e1.get()
    password = e2.get()
    if(username == "admin" and password == "123" or username == "gamer123" and password == "qwerty"):
        print("Welcome to the Astro Database 2.3")
        window = Tk()
        def show():
            Label(window, text=f"Username: {username}").place(x=10, y=40)
            Label(window, text=f"Password: {password}").place(x=10, y=60)
    
        window.geometry('600x400')
        window.title('Database!')
        Button(window, text="Show your credentials", command=show).place(x=10, y=10)
        window.mainloop()
    else:
        Label(root, text="Incorrect Password. Please try again.").place(x=10, y=60)

def create():
    win = Tk()

    def acc():
        user = e3.get()
        passs = e4.get()
        confirm_pass = e5.get()
        outfile = open('data1.txt')

        
        if len(passs) < 2 and len(confirm_pass) < 2 and len(passs) and len(confirm_pass) >= 1:
          print("Your password is less than 8 characters.")
        elif passs != confirm_pass:
          print("Type the password correctly.")
        elif user == "" or passs == "" or confirm_pass == "":
          print("Information is required.")
        else:
            print("Welcome!")
    
    Label(win, text="Create account").place(x=250, y=2)
    global e3
    global e4
    global e5
    e3 = Entry(win)
    e3.place(x=10, y=30)
    e4 = Entry(win)
    e4.place(x=10, y=80)
    e5 = Entry(win)
    e5.place(x=10, y=130)
    e4.config(show="*")
    e5.config(show="*")
    
    Label(win, text="Username").place(x=10, y=0)
    Label(win, text="Password").place(x=10, y=50)
    Label(win, text="Confirm password").place(x=10, y=105)
    Button(win, text="Create account", command=acc).place(x=10, y=170)
    
    win.geometry('600x400')
    win.mainloop()


global e1
global e2
e1 = Entry(root)
e1.place(x=10, y=10)
e2 = Entry(root)
e2.place(x=10, y=40)
e2.config(show="*")
button_1 = Button(root, text="LOGIN", command=data, height=3, width=22).place(x=10, y=80)
button_2 = Button(root, text="Or if you do not have an account already", command=create).place(x=10, y=200)

img = PhotoImage(file='lock.png')
Label(root,image=img).place(x=400, y=50)



root.title('Login')
root.geometry('600x400')
root.mainloop()

