from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox
from PIL import ImageTk ,Image
from subprocess import call
import mysql.connector
mysqldb = mysql.connector.connect(host="localhost", user="root", password="jpnsloveforever26", database="cse")
mycursor = mysqldb.cursor()
window=Tk()
def menu_callbb():
    def disp():
        Reg_no = e1.get()
        Name = e2.get()
        gender = e3.get()
        dob=e4.get()
        Age = e5.get()
        blood = e6.get()
        father_name = e7.get()
        mother_name = e8.get()
        Mobile_no = e9.get()
        Address = e10.get()
        fees_total = e11.get()
        fees_paid = e12.get()
        fees_due = e13.get()
        dept = e16.get()
        sem = e17.get()
        proctor = e19.get()
        attendence = e20.get()
        branch = e21.get()
        arrear = e23.get()
        remarks = e24.get()
        if (e1.get()==""):
            messagebox.showinfo("Fetch status","Reg_no is compulsory")
        else:
            sql="select*from vjs where Reg_no=%s"
            mycursor.execute(sql,[(Reg_no)])
            rows=mycursor.fetchall()

            for row in rows:

                e3.insert(0, row[13])
                e4.insert(0, row[6])
                e5.insert(0, row[5])
                e6.insert(0, row[7])
                e7.insert(0, row[14])
                e8.insert(0, row[15])
                e9.insert(0, row[3])
                e10.insert(0, row[4])
                e11.insert(0, row[9])
                e12.insert(0, row[10])
                e13.insert(0, row[11])
                e16.insert(0, row[2])
                e17.insert(0, row[16])
                e19.insert(0, row[8])
                e20.insert(0, row[12])
                e21.insert(0, row[18])
                e23.insert(0, row[17])
                e24.insert(0, row[19])

                mysqldb.close()
    def submit():
        Name = entry_name.get()
        Reg_no = entry_reg.get()

        sql = "select* from vjs where Name=%s and Reg_no = %s "
        mycursor.execute(sql, [(Name), (Reg_no)])
        results = mycursor.fetchall()

        if results:
            messagebox.showinfo("", "Login success")
        else:
            messagebox.showinfo("", "Incorrect Name/Register number")
            return False
        root1 = Tk()
        root.destroy()




        def update():
            Reg_no = e1.get()
            Name = e2.get()
            gender = e3.get()

            Age = e5.get()
            blood = e6.get()
            father_name = e7.get()
            mother_name = e8.get()
            Mobile_no = e9.get()
            Address = e10.get()
            fees_total = e11.get()
            fees_paid = e12.get()
            fees_due = e13.get()
            dept= e16.get()
            sem = e17.get()
            proctor = e19.get()
            attendence = e20.get()
            branch = e21.get()
            arrear = e23.get()
            remarks = e24.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="jpnsloveforever26",
                                              database="cse")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  vjs set Name= %s,gender= %s,Age= %s,blood= %s,father_name = %s,mother_name = %s,Mobile_no=%s,Address=%s,fees_total =%s,fees_paid =%s ,fees_due=%s,dept=%s,sem =%s,proctor =%s,attendence=%s,branch=%s,arrear=%s,remarks=%s where Reg_no= %s"
                val = (Name, gender, Age, blood, father_name, mother_name,Mobile_no,Address,fees_total,fees_paid ,fees_due,dept,sem ,proctor,attendence,branch,arrear,remarks,Reg_no)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid= mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully...")


                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e9.delete(0, END)
                e10.delete(0, END)
                e11.delete(0, END)
                e12.delete(0, END)
                e13.delete(0, END)
                e16.delete(0, END)
                e17.delete(0, END)
                e19.delete(0, END)
                e20.delete(0, END)
                e21.delete(0, END)
                e23.delete(0, END)
                e24.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()




        root1.geometry("800x500")

        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        global e7
        global e8
        global e9
        global e10
        global e11
        global e12
        global e13
        global e16
        global e17
        global e19
        global e20
        global e21
        global e23
        global e24

        s1 = Label(root1, text="VJS ENGINEERING COLLEGE", bd=20, relief=RAISED, fg="black", background="#FFAEB9",
                   font=('times new roman', 20))
        s1.grid(row=0, column=3, padx=2, pady=2)
        s2 = Label(root1, text="Personal Details", bd=20, relief=RIDGE, fg="black", background="#FFAEB9",
                   font=('times new roman', 16))
        s2.grid(row=1, column=0, padx=2, pady=2)
        s3 = Label(root1, text=" Register number:", bd=10, relief=FLAT, fg="black", background="#EE9572",
                   font=('Arial bold', 12))
        s3.grid(row=2, column=0, padx=2, pady=2)
        s4 = Label(root1, text=" Name", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s4.grid(row=3, column=0, padx=2, pady=2)
        s5 = Label(root1, text="Gender", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s5.grid(row=4, column=0, padx=2, pady=2)
        s6 = Label(root1, text="Date of birth", bd=10, relief=FLAT, fg="black", background="#EE9572",
                   font=('Arial bold', 12))
        s6.grid(row=5, column=0, padx=2, pady=2)
        s7 = Label(root1, text="Age", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s7.grid(row=6, column=0, padx=2, pady=2)
        s8 = Label(root1, text="Blood Group", bd=10, relief=FLAT, fg="black", background="#EE9572",
                   font=('Arial bold', 12))
        s8.grid(row=7, column=0, padx=2, pady=2)
        s9 = Label(root1, text="Father Name", bd=10, relief=FLAT, fg="black", background="#EE9572",
                   font=('Arial bold', 12))
        s9.grid(row=8, column=0, padx=2, pady=2)
        s10 = Label(root1, text="Mother Name", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s10.grid(row=9, column=0, padx=2, pady=2)
        s11 = Label(root1, text="Mobile Number", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s11.grid(row=10, column=0, padx=2, pady=2)
        s12 = Label(root1, text="Address", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s12.grid(row=11, column=0, padx=2, pady=2)
        s13 = Label(root1, text="Total Fees", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s13.grid(row=12, column=0, padx=2, pady=2)
        s14 = Label(root1, text="Fees Paid", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s14.grid(row=13, column=0, padx=2, pady=2)
        s15 = Label(root1, text="Fees Due", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s15.grid(row=9, column=5, padx=2, pady=2)
        s16 = Label(root1, text="Academic Details", bd=20, relief=RIDGE, fg="black", background="#FFAEB9",
                    font=('times new roman', 16))
        s16.grid(row=1, column=5, padx=2, pady=2)

        s19 = Label(root1, text="Department Name", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s19.grid(row=2, column=5, padx=2, pady=2)

        s22 = Label(root1, text="Semester", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s22.grid(row=3, column=5, padx=2, pady=2)
        s23 = Label(root1, text="Proctor", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s23.grid(row=4, column=5, padx=2, pady=2)
        s24 = Label(root1, text="CGPA", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s24.grid(row=5, column=5, padx=2, pady=2)

        s26 = Label(root1, text="Grade", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s26.grid(row=6, column=5, padx=2, pady=2)
        s27 = Label(root1, text="Arrear", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s27.grid(row=7, column=5, padx=2, pady=2)
        s28 = Label(root1, text="Remarks", bd=10, relief=FLAT, fg="black", background="#EE9572",
                    font=('Arial bold', 12))
        s28.grid(row=8, column=5, padx=2, pady=2)

        e1 = Entry(root1)
        e1.grid(row=2, column=1, padx=2, pady=2)

        e2 = Entry(root1)
        e2.grid(row=3, column=1, padx=2, pady=2)

        e3 = Entry(root1)
        e3.grid(row=4, column=1, padx=2, pady=2)

        e4 = Entry(root1)
        e4.grid(row=5, column=1, padx=2, pady=2)

        e5 = Entry(root1)
        e5.grid(row=6, column=1, padx=2, pady=2)

        e6 = Entry(root1)
        e6.grid(row=7, column=1, padx=2, pady=2)

        e7 = Entry(root1)
        e7.grid(row=8, column=1, padx=2, pady=2)

        e8 = Entry(root1)
        e8.grid(row=9, column=1, padx=2, pady=2)

        e9 = Entry(root1)
        e9.grid(row=10, column=1, padx=2, pady=2)

        e10 = Entry(root1)
        e10.grid(row=11, column=1, padx=2, pady=2)

        e11 = Entry(root1)
        e11.grid(row=12, column=1, padx=2, pady=2)

        e12 = Entry(root1)
        e12.grid(row=13, column=1, padx=2, pady=2)

        e13 = Entry(root1)
        e13.grid(row=9, column=6, padx=2, pady=2)

        e16 = Entry(root1)
        e16.grid(row=2, column=6, padx=2, pady=2)

        e17 = Entry(root1)
        e17.grid(row=3, column=6, padx=2, pady=2)

        e19 = Entry(root1)
        e19.grid(row=4, column=6, padx=2, pady=2)

        e20 = Entry(root1)
        e20.grid(row=5, column=6, padx=2, pady=2)

        e21 = Entry(root1)
        e21.grid(row=6, column=6, padx=2, pady=2)

        e23 = Entry(root1)
        e23.grid(row=7, column=6, padx=2, pady=2)

        e24 = Entry(root1)
        e24.grid(row=8, column=6, padx=2, pady=2)

        x2 = Button(root1, text="update", command=update, height=3, width=13)
        x2.grid(row=11, column=5, padx=2, pady=2)

        z1 = Button(root1, text="DISPLAY", command=disp, height=3, width=13)
        z1.grid(row=12, column=6, padx=2, pady=2)



    root = Tk()

    root.title("VJS ENGINEERING COLLEGE")

    root.geometry("1200x640")

    vjs = Label(root, bd=20, relief=RAISED, text="VJS ENGINEERING COLLEGE", fg="red", background="#FFF0F5",
                font=('times new roman', 18))
    vjs.grid(row=0, column=1, padx=2, pady=2)
    title = Label(root, bd=10, relief=RIDGE, text="Student Login ", fg="red", background="#FFE4E1",
                  font=('times new roman', 12))
    title.grid(row=1, column=1, padx=5, pady=5)
    name = Label(root, bd=10, relief=FLAT, text="NAME:", background="#00E5EE", font=('Arial bold', 10))
    name.grid(row=3, column=0, padx=2, pady=2)
    entry_name = Entry(root)
    entry_name.grid(row=3, column=1)
    reg = Label(root, bd=10, relief=FLAT, text="REGISTER NUMBER:", background="#00E5EE", font=('Arial bold', 10))
    reg.grid(row=4, column=0, padx=2, pady=2)
    entry_reg = Entry(root)
    entry_reg.grid(row=4, column=1)
    dept = Label(root, bd=10, relief=FLAT, text="DEPARTMENT:", background="#00E5EE", font=('Arial bold', 10))
    dept.grid(row=5, column=0, padx=2, pady=2)
    n = StringVar()
    scroll_box = ttk.Combobox(root, textvariable=n)
    scroll_box['values'] = ("SELECT", "CSE", "IT", "BME", "EEE", "ECE")
    scroll_box.current(0)
    scroll_box.grid(row=5, column=1, padx=2, pady=2)
    sub = Button(root, bd=10, relief=GROOVE, text="SUBMIT", command=submit, bg="#FFFF00", width=5, height=2,
                 background='#FFE4E1', activebackground='red',
                 font=('Arial bold', 10))
    sub.grid(row=6, column=1, padx=2, pady=2)
def Add():
            Reg_no = e1.get()
            Name = e2.get()
            gender = e3.get()
            dob = e4.get()
            Age = e5.get()
            blood = e6.get()
            father_name = e7.get()
            mother_name = e8.get()
            Mobile_no = e9.get()
            Address = e10.get()
            fees_total = e11.get()
            fees_paid = e12.get()
            fees_due = e13.get()
            dept = e16.get()
            sem = e17.get()
            proctor = e19.get()
            attendence = e20.get()
            branch = e21.get()
            arrear = e23.get()
            remarks = e24.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="jpnsloveforever26",
                                              database="cse")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  vjs (Reg_no,Name, gender, Age, dob, blood, father_name, mother_name,Mobile_no,Address,fees_total,fees_paid ,fees_due,dept,sem ,proctor,attendence,branch,arrear,remarks) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s, %s, %s, %s,%s,%s,%s, %s, %s, %s,%s,%s)"
                val = (Reg_no,Name, gender, Age, dob, blood, father_name, mother_name,Mobile_no,Address,fees_total,fees_paid ,fees_due,dept,sem ,proctor,attendence,branch,arrear,remarks)
                mycursor.execute(sql, val)
                mysqldb.commit()
                messagebox.showinfo("information", "Student inserted successfully...")
                show()
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e9.delete(0, END)
                e10.delete(0, END)
                e11.delete(0, END)
                e12.delete(0, END)
                e13.delete(0, END)
                e16.delete(0, END)
                e17.delete(0, END)
                e19.delete(0, END)
                e20.delete(0, END)
                e21.delete(0, END)
                e23.delete(0, END)
                e24.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

def menu_callback():

    def  submitad():
        Name =entry_nameadm.get()
        Id = entry_regadm.get()

        sqll = "select* from admin where Name=%s and Id = %s "
        mycursor.execute(sqll, [(Name), (Id)])
        results = mycursor.fetchall()

        if results:
            messagebox.showinfo("", "Login success")
        else:
            messagebox.showinfo("", "Incorrect Name/ID number")
            return False

        adm1 = Tk()
        adm.destroy()
        adm1.geometry("500x600")


        def delete():
            Reg_no = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="jpnsloveforever26",
                                              database="cse")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from vjs where Reg_no = %s"
                val = (Reg_no,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Deleted successfully...")
                show()
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                e7.delete(0, END)
                e8.delete(0, END)
                e9.delete(0, END)
                e10.delete(0, END)
                e11.delete(0, END)
                e12.delete(0, END)
                e13.delete(0, END)
                e16.delete(0, END)
                e17.delete(0, END)
                e19.delete(0, END)
                e20.delete(0, END)
                e21.delete(0, END)
                e23.delete(0, END)
                e24.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()



        x3 = Button(adm1, text="Delete", command=delete, height=3, width=13)
        x3.grid(row=12, column=3, padx=2, pady=2)

        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        global e7
        global e8
        global e9
        global e10
        global e11
        global e12
        global e13
        global e16
        global e17
        global e19
        global e20
        global e21
        global e23
        global e24

        s1 = Label(adm1, text="VJS ENGINEERING COLLEGE", bd=20, relief=RAISED, fg="black", background="#FFAEB9",
               font=('times new roman', 20))
        s1.grid(row=0, column=3, padx=2, pady=2)
        s2 = Label(adm1, text="Personal Details", bd=20, relief=RIDGE, fg="black", background="#FFAEB9",
               font=('times new roman', 16))
        s2.grid(row=1, column=0, padx=2, pady=2)
        s3 = Label(adm1, text=" Register number:", bd=10, relief=FLAT, fg="black", background="#EE9572",
               font=('Arial bold', 12))
        s3.grid(row=2, column=0, padx=2, pady=2)
        s4 = Label(adm1, text=" Name", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s4.grid(row=3, column=0, padx=2, pady=2)
        s5 = Label(adm1, text="Gender", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s5.grid(row=4, column=0, padx=2, pady=2)
        s6 = Label(adm1, text="Date of birth", bd=10, relief=FLAT, fg="black", background="#EE9572",
               font=('Arial bold', 12))
        s6.grid(row=5, column=0, padx=2, pady=2)
        s7 = Label(adm1, text="Age", bd=10, relief=FLAT, fg="black", background="#EE9572", font=('Arial bold', 12))
        s7.grid(row=6, column=0, padx=2, <
