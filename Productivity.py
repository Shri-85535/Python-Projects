from tkinter import *
from tkinter import messagebox
import mysql.connector
#import pyodbc
import sqlite3
#reset values
def clear():
    entry_empid.delete(0,END)
    #entry_worktype.delete(0,END)
    entry_ztid.delete(0,END)
    entry_delivered.delete(0,END)
    entry_rejects.delete(0,END)
    entry_comments.delete(0,END)
    #clear checkbox and radiobutton

def submit():
    employee_empid = empid.get()
    employee_worktype = worktype.get()
    employee_portal = portal.get()
    employee_ztid = ztid.get()
    employee_delivered = delivered.get()
    employee_rejects = rejects.get()
    employee_comments = comments.get()
    conn = sqlite3.connect(r'Test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS record (empid int, worktype varchar(200), portal varchar(200), ztid int, delivered int, rejects int, comments varchar(200))""")
    val = (employee_empid,employee_worktype,employee_portal,employee_ztid,employee_delivered,employee_rejects,employee_comments)
    c.executemany('INSERT INTO record VALUES (?, ?, ?, ?, ?, ?, ?)',(val,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Result", "Data Inserted!")
root=Tk()
root.geometry("550x600")
root.title("Productivity Tracker")
root["bg"]="lightgreen"
root.resizable = (False,False)

global empid
global worktype
global portal
global ztid
global delivered
global rejects
global comments

#creating data selection variable on gui
empid = IntVar()
worktype = StringVar()
portal = StringVar()
ztid = IntVar()
delivered = IntVar()
rejects = IntVar()
comments = StringVar()


#Form Title
label_title = Label(root,text = "Productivity Tracker",width = 20,font = ("bold",20)).place(x=90,y=20)


#create fields
label_empid = Label(root,text = "Employee ID",width = 20).place(x=80,y=130)
entry_empid = Entry(root,width = 20,textvariable = empid)
entry_empid.place(x = 260,y = 130)


label_worktype = Label(root,text = "Work Type",width = 20).place(x=80,y=180)
list1 = ["Client Delivery","Client Rejects","Mapping","Update Google Sheets","Update Tracker","Working on BDM's Request",
         "Working on Ops Request", "Working on Finance's Request", "Others"]
droplist=OptionMenu(root,worktype,*list1,)
droplist.config(width=15)
worktype.set('Select Worktype')
droplist.place(x=260,y=180)


label_portal = Label(root,text = "Portal",width = 20).place(x=80,y=230)
list1 = ["Portal 1","Portal 2","NA"]
droplist=OptionMenu(root,portal,*list1)
droplist.config(width=15)
portal.set('Select Portal')
droplist.place(x=260,y=230)

label_ztid = Label(root,text = "ZT ID",width = 20).place(x=80,y=280)
entry_ztid = Entry(root,width = 20,textvariable = ztid)
entry_ztid.place(x = 260,y = 280)


label_delivered = Label(root,text = "Leads Delivered",width = 20).place(x=80,y=330)
entry_delivered = Entry(root, width = 20, textvariable = delivered)
entry_delivered.place(x = 260,y = 330)


label_rejects = Label(root,text = "Leads Rejected",width = 20).place(x=80,y=380)
entry_rejects = Entry(root, width = 20, textvariable = rejects)
entry_rejects.place(x=260,y=380)



label_comments = Label(root,text = "Comments",width = 20).place(x=80,y=420)
entry_comments = Entry(root, width = 20, textvariable = comments)
entry_comments.place(x=260,y=420)


Button(root,text='Clear Data',width=10,bg='blue',fg='white',command = clear).place(x=150,y=480)
Button(root,text='Submit',width=10,bg='blue',fg='white',command = lambda:[submit(),clear()]).place(x=250,y=480)
#Button(root,text='Check',width=10,bg='blue',fg='white').place(x=320,y=520)
root.mainloop()

