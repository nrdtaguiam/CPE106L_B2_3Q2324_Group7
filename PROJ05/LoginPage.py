from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
			con = mysql.connect(host="localhost",user="root",password="",database="docterapp")
			cur = con.cursor()

			cur.execute("select * from user_information where username=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
				deshboard()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)


def deshboard():

	def book():
		if docter_var.get() =="" or day.get() =="" or month.get() == "" or year.get() == "":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = des)

		else:
			con = mysql.connect(host="localhost",user="root",password="",database="docterapp")
			cur = con.cursor()

			cur.execute("update user_information set docter ='" + docter_var.get() + "', day ='" +  day.get() + "', month = '" + month.get() + "', year = '" + year.get() + "' where username ='"+ user_name.get() +"'")
			con.commit()	
			con.close()
			messagebox.showinfo("Success" , "Booked Appointment " , parent = des)

	



	des = Tk()
	des.title("Admin Panel Employee Management System")	
	des.maxsize(width=800 ,  height=500)
	des.minsize(width=800 ,  height=500)		

		#heading label
	heading = Label(des , text = f"Username : {user_name.get()}" , font = '"Century Gothic" 20 bold',bg='red')
	heading.place(x=220 , y=50)

	f=Frame(des,height=1,width=800,bg="green")
	f.place(x=0,y=95)

	con = mysql.connect(host="localhost",user="root",password="",database="docterapp")
	cur = con.cursor()

	cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
	row = cur.fetchall()

	a=Frame(des,height=1,width=400,bg="green")
	a.place(x=0,y=195)

	b=Frame(des,height=100,width=1,bg="green")
	b.place(x=400,y=97)

	for data in row: 
		first_name = Label(des, text= f"First Name : {data[1]}" , font='"Century Gothic" 10 bold')
		first_name.place(x=20,y=100)

		last_name = Label(des, text= f"Last Name : {data[2]}" , font='"Century Gothic" 10 bold')
		last_name.place(x=20,y=130)

		age = Label(des, text= f"Age : {data[3]}" , font='"Century Gothic" 10 bold')
		age.place(x=20,y=160)

		gender = Label(des, text= f"ID : {data[0]}" , font='"Century Gothic" 10 bold')
		gender.place(x=250,y=100)

		Department = Label(des, text= f"Department : {data[5]}" , font='"Century Gothic" 10 bold')
		Department.place(x=250,y=130)

		add = Label(des, text= f"Address : {data[6]}" , font='"Century Gothic" 10 bold')
		add.place(x=250,y=160)

	# Book Docter Appointment App
	heading = Label(des , text = "Book Appointment" , font = '"Century Gothic" 20 bold')
	heading.place(x=470 , y=100)	

	# Book DocterLabel 
	Docter= Label(des, text= "Docter:" , font='"Century Gothic" 10 bold')
	Docter.place(x=480,y=145)

	Day = Label(des, text= "Day:" , font='"Century Gothic" 10 bold')
	Day.place(x=480,y=165)

	Month = Label(des, text= "Month:" , font='"Century Gothic" 10 bold')
	Month.place(x=480,y=185)

	Year = Label(des, text= "Year:" , font='"Century Gothic" 10 bold')
	Year.place(x=480,y=205)


	# Book Docter Entry Box



	docter_var = tk.StringVar()
	day = StringVar()
	month = tk.StringVar()
	year = StringVar()

	Docter_box= ttk.Combobox(des, width=30, textvariable= docter_var, state='readonly')
	Docter_box['values']=('Andy','Charlie','Shetal','Danish','Sunil')
	Docter_box.current(0)
	Docter_box.place(x=550,y=145)

	Day = Entry(des, width=33 , textvariable = day)
	Day.place(x=550 , y=168)

	Month_Box= ttk.Combobox(des, width=30, textvariable=month, state='readonly')
	Month_Box['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
	Month_Box.current(0)
	Month_Box.place(x=550,y=188)

	Year = Entry(des, width=33 , textvariable = year)
	Year.place(x=550 , y=208)

	# button 

	btn= Button(des, text = "Search" ,font='"Century Gothic" 10 bold', width = 20, command = book)
	btn.place(x=553, y=230)




	con = mysql.connect(host="localhost",user="root",password="",database="docterapp")
	cur = con.cursor()

	cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
	rows = cur.fetchall()
	# book Appoitment Details
	heading = Label(des , text = f"{user_name.get()} Appointments" , font = '"Century Gothic" 15 bold')
	heading.place(x=20 , y=250)	

	for book in rows:
		d1 = Label(des, text= f"Docter: {book[9]}" , font='"Century Gothic" 10 bold')
		d1.place(x=20,y=300)

		d2 = Label(des, text= f"Day: {book[10]}" , font='"Century Gothic" 10 bold')
		d2.place(x=20,y=320)

		d3 = Label(des, text= f"Month: {book[11]}" , font='"Century Gothic" 10 bold')
		d3.place(x=20,y=340)

		d4 = Label(des, text= f"Year: {book[12]}" , font='"Century Gothic" 10 bold')
		d4.place(x=20,y=360)		




					
#-----------------------------------------------------End Deshboard Panel -------------------------------------
#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or age.get()=="" or Department.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = mysql.connect(host="localhost",user="root",password="",database="docterapp")
				cur = con.cursor()
				cur.execute("select * from user_information where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
					cur.execute("insert into user_information(first_name,last_name,age,gender,Department,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						age.get(),
						var.get(),
						Department.get(),
						add.get(),
						user_name.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

	# close signup function			
	def switch():
		winsignup.destroy()
		win.deiconify()
                
	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		age.delete(0,END)
		var.set("Male")
		Department.delete(0,END)
		add.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)


	# start Signup Window	

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
	first_name = Label(winsignup, text= "First Name :" , font='"Century Gothic" 10 bold')
	first_name.place(x=80,y=130)
	first_name.configure(bg='burlywood1')

	last_name = Label(winsignup, text= "Last Name :" , font='"Century Gothic" 10 bold')
	last_name.place(x=80,y=160)
	last_name.configure(bg='burlywood1')

	age = Label(winsignup, text= "Age :" , font='"Century Gothic" 10 bold')
	age.place(x=80,y=190)
	age.configure(bg='burlywood1')

	Gender = Label(winsignup, text= "Gender :" , font='"Century Gothic" 10 bold')
	Gender.place(x=80,y=220)
	Gender.configure(bg='burlywood1')

	Department = Label(winsignup, text= "Department :" , font='"Century Gothic" 10 bold')
	Department.place(x=80,y=260)
	Department.configure(bg='burlywood1')

	add = Label(winsignup, text= "Address :" , font='"Century Gothic" 10 bold')
	add.place(x=80,y=290)
	add.configure(bg='burlywood1')

	user_name = Label(winsignup, text= "User Name :" , font='"Century Gothic" 10 bold')
	user_name.place(x=80,y=320)
	user_name.configure(bg='burlywood1')

	password = Label(winsignup, text= "Password :" , font='"Century Gothic" 10 bold')
	password.place(x=80,y=350)
	password.configure(bg='burlywood1')

	confirm_pass = Label(winsignup, text= "Confirm Password:" , font='"Century Gothic" 10 bold')
	confirm_pass.place(x=80,y=380)
	confirm_pass.configure(bg='burlywood1')

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	age = IntVar(winsignup, value=' ')
	var= StringVar()
	Department= StringVar()
	add = StringVar()
	user_name = StringVar()
	password = StringVar()
	confirm_pass = StringVar()


	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)


	
	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)

	
	age = Entry(winsignup, width=10, textvariable=age)
	age.place(x=200 , y=193)

	
	Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
	Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)


	Department = Entry(winsignup, width=40,textvariable = Department)
	Department.place(x=200 , y=263)


	add = Entry(winsignup, width=40 , textvariable = add)
	add.place(x=200 , y=293)

	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=323)

	
	password = Entry(winsignup, width=40, show="*",  textvariable = password)
	password.place(x=200 , y=353)

	
	confirm_pass= Entry(winsignup, width=40 ,show="*" , textvariable = confirm_pass)
	confirm_pass.place(x=200 , y=383)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='"Century Gothic" 10 bold', command = action)
	btn_signup.place(x=200, y=413)


	btn_login = Button(winsignup, text = "Clear" ,font='"Century Gothic" 10 bold' , command = clear)
	btn_login.place(x=280, y=413)


	sign_up_btn = Button(winsignup , text="Back" , command = switch )
	sign_up_btn.place(x=350 , y =20)


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	


	

#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("Employee Management System")

# window size
win.maxsize(width=450 ,  height=450)
win.minsize(width=450 ,  height=450)
win.configure(bg='SkyBlue1')

#heading label
heading = Label(win , text = "Employee Management System" , font = '"Century Gothic" 20 bold', justify=CENTER)
heading.place(x=20,y=100)
heading.configure(bg='SkyBlue1')

username = Label(win, text= "User Name :" , font='"Century Gothic" 10 bold')
username.place(x=50,y=170)
username.configure(bg='SkyBlue1')

userpass = Label(win, text= "Password :" , font='"Century Gothic" 10 bold')
userpass.place(x=50,y=210)
userpass.configure(bg='SkyBlue1')

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=170 , y=173)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=170 , y=213)


# button login and clear

btn_login = Button(win, text = "Login" ,font='"Century Gothic" 10 bold',command = login)
btn_login.place(x=160, y=293)


btn_login = Button(win, text = "Clear" ,font='"Century Gothic" 10 bold', command = clear)
btn_login.place(x=220, y=293)

# signup button

sign_up_btn = Button(win , text="Sign Up Now!" , command = signup )
sign_up_btn.place(x=350 , y =20)



win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------
