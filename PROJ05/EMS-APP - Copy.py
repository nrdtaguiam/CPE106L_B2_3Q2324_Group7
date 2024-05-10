from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
import tkinter.messagebox
from datetime import datetime

def Database():
    global conn, cursor
    conn = sqlite3.connect('EMSDatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Employee` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, age INTEGER, address TEXT, department TEXT, username TEXT, password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Attendance` (att_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, date TEXT, time TEXT)''')

def signup():
    def action():
       if  first.get() == "" or last.get() == "" or a.get() == "" or add.get() == "" or d.get() == "" or u.get() == "" or p.get() == "" or cp.get() == "":
            messagebox.showerror("Error", "Please complete the required field!", parent = winsignup)
        elif p.get() != cp.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            Database()
            query = "SELECT * FROM Employee WHERE username LIKE ?"
            cursor.execute(query, (("'"+str(u.get())+"%"+"'"),))
            existing_users = cursor.fetchall()
            if existing_users:
                messagebox.showerror("Error", "Username taken!", parent=winsignup)
            else:
                cursor.execute("INSERT INTO `Employee` (firstname, lastname, age, address, department, username, password) VALUES(?, ?, ?, ?, ?, ?, ?)",
                               (str(first.get()), str(last.get()), int(a.get()), str(add.get()), str(d.get()), str(u.get()), str(p.get())))
                cursor.execute("SELECT emp_id FROM Employee ORDER BY emp_id DESC LIMIT 1;")
                lastRowId = cursor.fetchone()[0]
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful", parent=winsignup)
                messagebox.showinfo("Employee ID", "Your Employee ID is " + str(lastRowId))
                winsignup.destroy()
                win.deiconify()

    def signupswitch():
        winsignup.withdraw()
        win.deiconify()

    def clear():
        first.delete(0, END)
        last.delete(0, END)
        a.delete(0, END)
        d.delete(0, END)
        add.delete(0, END)
        u.delete(0, END)
        p.delete(0, END)
        cp.delete(0, END)

    winsignup = Tk()
    winsignup.title("Sign Up")
    winsignup.configure(bg='lightgray')
    win.withdraw()

    heading = Label(winsignup, text="Signup", font="Helvetica 20 bold")
    heading.pack(pady=20)
    heading.configure(bg='lightgray')

    form_frame = Frame(winsignup, bg='lightgray')
    form_frame.pack(pady=20)

    labels = ["First Name:", "Last Name:", "Age:", "Department:", "Address:", "Username:", "Password:", "Confirm Password:"]
    entries = []

    for i, label in enumerate(labels):
        lbl = Label(form_frame, text=label, font="Helvetica 10 bold", bg='lightgray')
        lbl.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = Entry(form_frame, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries.append(entry)

    btn_frame = Frame(winsignup, bg='lightgray')
    btn_frame.pack(pady=20)

    btn_signup = Button(btn_frame, text="Signup", font="Helvetica 10 bold", command=action)
    btn_signup.grid(row=0, column=0, padx=10)

    btn_clear = Button(btn_frame, text="Clear", font="Helvetica 10 bold", command=clear)
    btn_clear.grid(row=0, column=1, padx=10)

    btn_back = Button(btn_frame, text="Back", font="Helvetica 10 bold", command=signupswitch)
    btn_back.grid(row=0, column=2, padx=10)

    winsignup.mainloop()

def login():
    if user_name.get() == "" or password.get() == "" or employee_id.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    elif user_name.get() == "AdminGroup" and password.get() == "123" and employee_id.get() == "0":
        adminfunctions()
    else:
        global conn, cursor
        conn = sqlite3.connect('EMSDatabase.db')
        cursor = conn.cursor()

        cursor.execute("select * from Employee where username=? and password = ? and emp_id = ?", (str(userentry.get()), str(passentry.get()), int(identry.get())))
        row = cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Invalid ID, User Name, or Password", parent=win)
        else:
            messagebox.showinfo("Success", "Successfully Login", parent=win)
            main()

def clear(main=None):
    userentry.delete(0, END)
    passentry.delete(0, END)

def Exit():
    result = tkinter.messagebox.askquestion('Employee Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        win.destroy()
        exit()

def get_username():
    return user_name.get()

def main():
    win.withdraw()
    main = Tk()
    main.title("Employee Management System")
    main.configure(bg='burlywood1')
    main.minsize(width=1000, height=700)

    main_exit = Button(main, width=10, text="Exit", command=mainswitch)
    main_exit.place(x=30, y=650)

    viewprof_button = Button(main, width=30, text="View Profile", font='"Century Gothic" 20 bold', command=viewprof)
    viewprof_button.pack(side=BOTTOM, pady=4)
    viewprof_button.configure(bg='aquamarine4')

    viewatt_button = Button(main, width=30, text="View Attendance", font='"Century Gothic" 20 bold', command=viewatt)
    viewatt_button.pack(side=TOP, pady=2)
    viewatt_button.configure(bg='aquamarine4')

    main.mainloop()

def adminfunctions():
    def adminswitch():
        result = tkinter.messagebox.askquestion('Admin Functions', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes':
            admin.withdraw()
            win.deiconify()

    win.withdraw()
    admin = Tk()
    admin.title("Admin Functions")
    admin.configure(bg='SkyBlue1')
    admin.minsize(width=1000, height=700)
    admin_exit = Button(admin, width=10, text="Exit", command=adminswitch)
    admin_exit.place(x=30, y=650)

win = Tk()

# App title
win.title("Employee Management System")

# Main window design
win.maxsize(width=450, height=450)
win.minsize(width=450, height=450)
win.configure(bg='#FFFFFF')

heading = Label(win, text="Employee Management System", font=("Arial", 20, "bold"), bg='#FFFFFF')
heading.place(x=20, y=80)

ID = Label(win, text="ID:", font=("Arial", 12, "bold"), bg='#FFFFFF')
ID.place(x=50, y=160)

username = Label(win, text="User Name:", font=("Arial", 12, "bold"), bg='#FFFFFF')
username.place(x=50, y=200)

userpass = Label(win, text="Password:", font=("Arial", 12, "bold"), bg='#FFFFFF')
userpass.place(x=50, y=240)

date_time = Label(win, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), font=("Arial", 10, "bold"), bg='#FFFFFF')
date_time.place(x=300, y=400)

user_name = StringVar()
password = StringVar()
employee_id = StringVar()

identry = Entry(win, width=40, textvariable=employee_id)
identry.focus()
identry.place(x=170, y=163)

userentry = Entry(win, width=40, textvariable=user_name)
userentry.place(x=170, y=203)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=170, y=247)

button_frame = Frame(win, bg='#FFFFFF')
button_frame.place(relx=0.5, rely=0.8, anchor=CENTER)

btn_login = Button(button_frame, text="Login", font=("Arial", 12, "bold"), command=login, bd=0, highlightthickness=0)
btn_login.grid(row=0, column=0, padx=5)

sign_up_btn = Button(button_frame, text="Sign Up", font=("Arial", 12, "bold"), command=signup, bd=0, highlightthickness=0)
sign_up_btn.grid(row=0, column=1, padx=5)

btn_clear = Button(button_frame, text="Clear", font=("Arial", 12, "bold"), command=clear, bd=0, highlightthickness=0)
btn_clear.grid(row=1, column=0, columnspan=2, pady=10)

btn_exit = Button(button_frame, text="Exit", font=("Arial", 12, "bold"), command=win.quit, bd=0, highlightthickness=0)
btn_exit.grid(row=2, column=0, columnspan=2, pady=10)

win.mainloop()
