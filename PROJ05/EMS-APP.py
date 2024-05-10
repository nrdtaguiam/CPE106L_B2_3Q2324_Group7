from tkinter import*
import sqlite3
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from datetime import datetime

def Database():
    global conn, cursor
    conn = sqlite3.connect('EMSDatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Employee` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, age INTEGER, address TEXT, department TEXT, username TEXT, password TEXT)''')


def signup():
    def action():
        if  first == "" or last == "" or a == "" or add == "" or d == "" or u == "" or p == "" or cp == "":
            messagebox.showerror("Error", "Please complete the required field!", parent = winsignup)
        elif p.get() != cp.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            Database()
            cursor.execute("INSERT INTO `Employee` (firstname, lastname, age, address, department, username, password) VALUES(?, ?, ?, ?, ?, ?, ?)",
                       (str(first.get()), str(last.get()), int(a.get()), str(add.get()), str(d.get()),str(u.get()), str(p.get())))
            cursor.execute("SELECT emp_id FROM Employee ORDER BY emp_id DESC LIMIT 1;")
            lastRowId=cursor.fetchone()[0]
             
            conn.commit()
            FIRSTNAME.set(FIRSTNAME)
            LASTNAME.set(LASTNAME)
            AGE.set(AGE)
            ADDRESS.set(ADDRESS)
            DEPARTMENT.set(DEPARTMENT)
            USERNAME.set(USERNAME)
            PASSWORD.set(PASSWORD)
            cursor.close()
            conn.close()
        

            messagebox.showinfo("Success" , "Registration Successfull" , parent = winsignup)
            messagebox.showinfo("Employee ID","Your Employee ID is "+str(lastRowId))

            winsignup.destroy()
            win.deiconify()

            
    
    
        
    def signupswitch():
        winsignup.withdraw()
        win.deiconify()

    def clear():
        first.delete(0,END)
        last.delete(0,END)
        a.delete(0,END)
        d.delete(0,END)
        add.delete(0,END)
        u.delete(0,END)
        p.delete(0,END)
        cp.delete(0,END)        


    winsignup = Tk()
    winsignup.title("Sign Up")
    winsignup.maxsize(width=500 ,  height=600)
    winsignup.minsize(width=500 ,  height=600)
    winsignup.configure(bg='burlywood1')
    win.withdraw()

    #heading label
    heading = Label(winsignup , text = "Signup" , font = '"Century Gothic" 20 bold')
    heading.place(x=80 , y=60)
    heading.configure(bg='burlywood1')

    # form data label
    FIRST_NAME = Label(winsignup, text= "First Name: " , font='"Century Gothic" 10 bold')
    FIRST_NAME.place(x=80,y=130)
    FIRST_NAME.configure(bg='burlywood1')

    LAST_NAME = Label(winsignup, text= "Last Name: " , font='"Century Gothic" 10 bold')
    LAST_NAME.place(x=80,y=160)
    LAST_NAME.configure(bg='burlywood1')

    AGE_LBL = Label(winsignup, text= "Age: " , font='"Century Gothic" 10 bold')
    AGE_LBL.place(x=80,y=190)
    AGE_LBL.configure(bg='burlywood1')

    DEP_LBL = Label(winsignup, text= "Department: " , font='"Century Gothic" 10 bold')
    DEP_LBL.place(x=80,y=260)
    DEP_LBL.configure(bg='burlywood1')

    ADD_LBL = Label(winsignup, text= "Address: " , font='"Century Gothic" 10 bold')
    ADD_LBL.place(x=80,y=290)
    ADD_LBL.configure(bg='burlywood1')

    USER_LBL = Label(winsignup, text= "User Name: " , font='"Century Gothic" 10 bold')
    USER_LBL.place(x=80,y=320)
    USER_LBL.configure(bg='burlywood1')

    PASS_LBL = Label(winsignup, text= "Password: " , font='"Century Gothic" 10 bold')
    PASS_LBL.place(x=80,y=350)
    PASS_LBL.configure(bg='burlywood1')

    CONF_LBL = Label(winsignup, text= "Confirm Password: " , font='"Century Gothic" 10 bold')
    CONF_LBL.place(x=80,y=380)
    CONF_LBL.configure(bg='burlywood1')

	
    FIRSTNAME = StringVar()
    LASTNAME = StringVar()
    AGE = IntVar(winsignup, value=' ')
    DEPARTMENT= StringVar()
    ADDRESS = StringVar()
    USERNAME = StringVar()
    PASSWORD = StringVar()
    CONFPASS = StringVar()


    first = Entry(winsignup, width=40 , textvariable = FIRSTNAME)
    first.place(x=200 , y=133)
    
    last = Entry(winsignup, width=40 , textvariable = LASTNAME)
    last.place(x=200 , y=163)

    a = Entry(winsignup, width=10, textvariable=AGE)
    a.place(x=200 , y=193)

        
    d = Entry(winsignup, width=40,textvariable = DEPARTMENT)
    d.place(x=200 , y=263)

    add = Entry(winsignup, width=40 , textvariable = ADDRESS)
    add.place(x=200 , y=293)

    u = Entry(winsignup, width=40,textvariable = USERNAME)
    u.place(x=200 , y=323)

    p = Entry(winsignup, width=40, show="*",  textvariable = PASSWORD)
    p.place(x=200 , y=353)
    
    cp= Entry(winsignup, width=40 ,show="*" , textvariable = CONFPASS)
    cp.place(x=200 , y=383)

    
    btn_signup = Button(winsignup, text = "Signup" ,font='"Century Gothic" 10 bold', command = action)
    btn_signup.place(x=200, y=413)

    btn_clear = Button(winsignup, text = "Clear" ,font='"Century Gothic" 10 bold' , command = clear)
    btn_clear.place(x=280, y=413)


    btn_back = Button(winsignup , text="Back" , command = signupswitch )
    btn_back.place(x=350 , y =20)

    
    winsignup.mainloop()

def login():
    if user_name.get() == "" or password.get() == "" or employee_id.get() == "":
        messagebox.showerror("Error", "Enter User Name, Password, and Employee ID")
    elif user_name.get() == "AdminGroup" and password.get() == "123" and employee_id.get() == "0":
        # Close the login window
        win.destroy()
        # Open the main_2 window
        import main_2
        main_2.main()
    else:
            global conn, cursor
            conn = sqlite3.connect('EMSDatabase.db')
            cursor = conn.cursor()

            cursor.execute("select * from Employee where username=? and password = ? and emp_id = ?",(str(userentry.get()),str(passentry.get()),int(identry.get())))
            row = cursor.fetchone()

            if row==None:
                messagebox.showerror("Error" , "Invalid ID, User Name, or Password", parent = win)

            else:
                messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                main()
                
    def get_username():
        return user_name.get()
    
    conn = sqlite3.connect('EMSDatabase.db')
    cursor = conn.cursor()

    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Attendance` (att_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, date TEXT, time TEXT)''')


                
    def get_username():
        return user_name.get()
    
    conn = sqlite3.connect('EMSDatabase.db')
    cursor = conn.cursor()

    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')
    cursor.execute('''CREATE TABLE IF NOT EXISTS `Attendance` (att_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, date TEXT, time TEXT)''')
    
    
                
                
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)
	
def Exit():
    result = tkMessageBox.askquestion('Employee Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        win.destroy()
        exit()
        
def main():
    def mainswitch():
        result = tkMessageBox.askquestion('Main Menu', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes':
            main.withdraw()
            win.deiconify()


    def viewprof():
        def back():
            Prof_Right.pack_forget()
            viewprof_button.pack(side=BOTTOM,pady=6)
            viewatt_button.pack(side=TOP,pady=6)
            btn_back.pack_forget()
            
        def profile_info():
            for i in tree.get_children():
                tree.delete(i)
            conn = sqlite3.connect('EMSDatabase.db')
            cursor = conn.cursor()
            query = "SELECT * FROM Employee WHERE username = ?"
            cursor.execute(query, [(user_name.get())])
            
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('','end',values=(data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            cursor.close()
            conn.close()
            
        viewprof_button.pack_forget()
        viewatt_button.pack_forget()
        Prof_Right = Frame(main, width=500, height=500, bd=8, relief="raise")
        Prof_Right.pack(side=RIGHT)
        scrollbary = Scrollbar(Prof_Right, orient=VERTICAL)
        scrollbarx = Scrollbar(Prof_Right, orient=HORIZONTAL)
        tree = ttk.Treeview(Prof_Right, columns=("Firstname", "Lastname", "Age", "Address", "Department", "Username", "Password"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        profile_info()
        tree.heading('Firstname', text="Firstname", anchor=W)
        tree.heading('Lastname', text="Lastname", anchor=W)
        tree.heading('Age', text="Age", anchor=W)
        tree.heading('Address', text="Address", anchor=W)
        tree.heading('Department', text="Department", anchor=W)
        tree.heading('Username', text="Username", anchor=W)
        tree.heading('Password', text="Password", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=120)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=90)
        tree.column('#7', stretch=NO, minwidth=0, width=90)
        tree.pack()
        
        btn_back = Button(main , text="Back" , font = '"Century Gothic" 20 bold', command = back)
        btn_back.pack(side=LEFT)
        btn_back.configure(bg='aquamarine4')
        
    def viewatt():
        def back():
            Att_Right.pack_forget()
            viewprof_button.pack(side=BOTTOM,pady=6)
            viewatt_button.pack(side=TOP,pady=6)
            btn_back.pack_forget()
            
        def att_info():
            for i in tree.get_children():
                tree.delete(i)
            conn = sqlite3.connect('EMSDatabase.db')
            cursor = conn.cursor()
            query = "SELECT * FROM Attendance WHERE username = ?"
            cursor.execute(query, [(user_name.get())])
            
            fetch = cursor.fetchall()
            for data in fetch:
                messagebox.showerror("Success" , "Meron" , parent = main)
                tree.insert('','end',values=(data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            cursor.close()
            conn.close()    
        viewprof_button.pack_forget()
        viewatt_button.pack_forget()

        Att_Right = Frame(main, width=500, height=500, bd=8, relief="raise")
        Att_Right.pack(side=RIGHT)
        scrollbary = Scrollbar(Att_Right, orient=VERTICAL)
        scrollbarx = Scrollbar(Att_Right, orient=HORIZONTAL)
        tree = ttk.Treeview(Att_Right, columns=("Firstname", "Lastname", "Age", "Address", "Department", "Username", "Password"), selectmode="none", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        
        btn_back = Button(main , text="Back" , font = '"Century Gothic" 20 bold', command = back)
        btn_back.pack(side=LEFT)
        btn_back.configure(bg='aquamarine4')

        
    win.withdraw()
    main = Tk()
    main.title("Employee Management System")
    main.configure(bg='burlywood1')
    main.minsize(width=1000 ,  height=700)
    
    main_exit = Button(main, width=10, text="Exit", command=mainswitch)
    main_exit.place(x=30, y=650)

    viewprof_button = Button(main, width=30, text="View Profile", font = '"Century Gothic" 20 bold', command=viewprof)
    viewprof_button.pack(side=BOTTOM,pady=4)
    viewprof_button.configure(bg='aquamarine4')

    viewatt_button = Button(main, width=30, text="View Attendance", font = '"Century Gothic" 20 bold', command=viewatt)
    viewatt_button.pack(side=TOP,pady=2)
    viewatt_button.configure(bg='aquamarine4')
    
#admin functions
        
def adminfunctions():
    def adminswitch():
        result = tkMessageBox.askquestion('Admin Functions', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes':
            admin.withdraw()
            win.deiconify()
    
        
    win.withdraw()
    admin = Tk()
    admin.title("Admin Functions")
    admin.configure(bg='SkyBlue1')
    admin.minsize(width=1000 ,  height=700)
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
