import sqlite3
from tkinter import *
from tkinter import messagebox

class Login:

    def new(self):
        roott = Tk()
        roott.title('Database!')

        def function():
            ## INSERT INTO users VALUES (x,y,z)
            ## CREATE TABLE users (x text, y integer, z text)
            ## SELECT * FROM users  WHERE y=int(y) (e.g fixed amount of money e.g £50000)
            ## fetchmany, fetch, fetchall

            username = e3.get()
            password = e4.get()
            confirm_pass = e5.get()
            pay = e6.get()

            if password == confirm_pass:
                
                conn = sqlite3.connect('databased.db')
                c = conn.cursor()

                c.execute("INSERT INTO users VALUES (:username, :password, :confirm_pass, :pay)", 
                {
                        'username': username,
                        'password': password,
                        'confirm_pass': confirm_pass,
                        'pay': pay
                        })

                print("Successfully executed...")
                conn.commit()

                c.execute('SELECT *, oid FROM users')

                users = c.fetchall()

                for user in users:
                    print(user)

                conn.commit()
                conn.close()

                outfile = open('data.txt', 'a')
                outfile.write(f'\nUsername: {username}\nPassword: {password}\nPay: £{pay}\n')

                rooott = Tk()

                def shade():
                    Label(rooott, text=f"Username: {username}").place(x=10, y=40)
                    Label(rooott, text=f"Password: {password}").place(x=10, y=70)
                    Label(rooott, text=f"Pay: £{pay}").place(x=10, y=100)


                Button(rooott, text="Show your credentials", command=shade).place(x=10, y=10)

                rooott.geometry('600x400')
                rooott.mainloop()
            else:
                messagebox.showwarning('Warning.', 'Please confirm your password.')

        Label(roott, text="Welcome! To continue create an account to store in the database").grid()

        e3 = Entry(roott, width=20)
        e3.place(x=80, y=40)
        e4 = Entry(roott, width=20)
        e4.place(x=80, y=90)
        e5 = Entry(roott, width=20)
        e5.place(x=120, y=140)
        e6 = Entry(roott, width=20)
        e6.place(x=80, y=190)

        e4.config(show='*')
        e5.config(show='*')

        Label(roott, text="Username").place(x=0, y=40)
        Label(roott, text="Password").place(x=0, y=90)
        Label(roott, text="Confirm password").place(x=0, y=140)
        Label(roott, text="Pay").place(x=0, y=190)

        Button(roott, text="Create account", command=function).place(x=10, y=250)

        roott.geometry('600x400')
        roott.mainloop()


    def __init__(self):
        root = Tk()
        root.geometry('600x400')
        root.title('Login')

        bg = PhotoImage(file="images/Screenshot_1554.png")
        my_canvas = Canvas(root, width=600, height=400)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0, image=bg, anchor="nw")
        
        def button():
            username = e1.get()
            password = e2.get()

            if username == "jimmy" and password == "123":
                self.new()
            else:
                messagebox.showwarning('Warning.', 'Incorrect password or username. Please try again.') 
                ## all messagebox commands 
                ## messsagebox.showerror('', '')
                ## messagebox.showwarning('', '')
                ## messagebox.showinfo('', '')

        e1 = Entry(root, width=30)
        e1.place(x=70, y=10)

        e2 = Entry(root, width=30)
        e2.place(x=70, y=60)
        e2.config(show="*")

        Button(root, text="LOGIN", command=button).place(x=10, y=100)

        Label(root, text="Username").place(x=0, y=10)
        Label(root, text="Password").place(x=0, y=60)

        root.mainloop()

Login()



        
