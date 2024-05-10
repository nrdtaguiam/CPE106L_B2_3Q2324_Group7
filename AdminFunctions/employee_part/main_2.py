from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

empID = StringVar()
fname = StringVar()
lname = StringVar()
age = StringVar()
gender = StringVar()
contact = StringVar()
address = StringVar()
username = StringVar()
password = StringVar()
department = StringVar()


# Entries Frame
entry_frame = Frame(root, bg="#535c68")
entry_frame.pack(side=TOP, fill=X)
title = Label(entry_frame, text="Employee Management System", font=("arial", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, column=0,columnspan=2, padx=10, pady=20, sticky="w")

fname_lbl = Label(entry_frame, text="First Name", font=("Helvetica", 15), bg="#535c68", fg="white")
fname_lbl.grid(row=1, column=0,sticky='w', padx=10, pady=11)
fname_entry = Entry(entry_frame, bd=3, relief='ridge', font=("Helvetica", 13), textvariable=fname, width=20)
fname_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11) 

lname_lbl = Label(entry_frame, text="Last Name", font=("Helvetica", 15), bg="#535c68", fg="white")
lname_lbl.grid(row=2, column=0,sticky='w', padx=10, pady=11)
lname_entry = Entry(entry_frame, bd=3, relief='ridge', font=("Helvetica", 13), textvariable=lname, width=20)
lname_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11) 

age_lbl = Label(entry_frame, text="Age", font=("Helvetica", 15), bg="#535c68", fg="white")
age_lbl.grid(row=1, column=2,sticky='w', padx=10, pady=11)
age_entry = Entry(entry_frame, bd=3, relief='ridge', font=("Helvetica", 13), textvariable=age, width=20)
age_entry.grid(row=1, column=3, sticky='w', padx=10, pady=11)

dept_lbl = Label(entry_frame, text="Department", font=("Helvetica", 15), bg="#535c68", fg="white")
dept_lbl.grid(row=3,column=0,sticky='w',padx=10,pady=11)
dept_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=department)
dept_combo['values']=("Executives", "Sales","Finance", "Operations")
dept_combo.grid(row=3,column=1,sticky='w',padx=10,pady=12)

usn_lbl = Label(entry_frame, text="Username", font=("Helvetica", 15), bg="#535c68", fg="white")
usn_lbl.grid(row=2,column=2,sticky='w',padx=10,pady=11)
usn_entry = Entry(entry_frame, bd=3, relief='ridge', font=("Helvetica", 13), textvariable=username, width=20)
usn_entry.grid(row=2, column=3, sticky='w', padx=10, pady=11)

pass_lbl = Label(entry_frame, text="Password", font=("Helvetica", 15), bg="#535c68", fg="white")
pass_lbl.grid(row=3,column=2,sticky='w',padx=10,pady=11)
pass_entry = Entry(entry_frame, bd=3, relief='ridge', font=("Helvetica", 13), textvariable=password, width=20)
pass_entry.grid(row=3, column=3, sticky='w', padx=10, pady=11)

adr_lbl = Label(entry_frame, text="Address", font=("Helvetica", 15), bg="#535c68", fg="white")
adr_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
adr_entry = Text(entry_frame, width=60, height=5, font=("Helvetica", 15))
adr_entry.grid(row=5, column=0, columnspan=4, padx=10, pady=11, sticky='w')


def getData(event):
    selected_row = table.focus()
    data = table.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    fname.set(row[1])
    lname.set(row[2])
    age.set(row[3])
    username.set(row[4])
    department.set(row[5])
    password.set(row[6])
    adr_entry.delete(1.0, END)
    adr_entry.insert(END, row[7])

def dispalyAll():
    table.delete(*table.get_children())
    for row in db.fetch():
        table.insert("", END, values=row)


def add_employee():
    if fname_entry.get() == "" or lname_entry.get() == ""  or age_entry.get() == "" or usn_entry.get() == "" or dept_combo.get() == "" or pass_entry.get() == "" or adr_entry.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(fname_entry.get(), lname_entry.get(), age_entry.get(), usn_entry.get(), dept_combo.get(), pass_entry.get(), adr_entry.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if fname_entry.get() == "" or lname_entry.get() == "" or age_entry.get() == "" or usn_entry.get() == "" or dept_combo.get() == "" or pass_entry.get() == "" or adr_entry.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0], fname_entry.get(), lname_entry.get(), age_entry.get(), usn_entry.get(), dept_combo.get(), pass_entry.get(), adr_entry.get(1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    fname.set("")
    lname.set("")
    age.set("")
    department.set("")
    username.set("")
    password.set("")
    adr_entry.delete(1.0, END)



btn_frame = Frame(entry_frame, bg="#535c68")
btn_frame.grid(row=3, column=5, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=1, column=0, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=1, column=2, padx=10)


data_frame=Frame(root,bd=5,relief='ridge',bg='wheat')
data_frame.place(x=0,y=480,width=2020,height=600)

# Table Frame

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=10, y=500, width=1990, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Helvetica', 18))  # Modify the font of the headings
table = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
table.heading("1", text="ID")
table.heading("2", text="First Name")
table.heading("3", text="Last Name")
table.heading("4", text="Age")
table.heading("5", text="Username")
table.heading("6", text="Department")
table.heading("7", text="Password")
table.heading("8", text="Address")
table['show'] = 'headings'
table.bind("<ButtonRelease-1>", getData)
table.pack(fill=X)

dispalyAll()
root.mainloop()
