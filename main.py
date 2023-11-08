from tkinter import *
import mysql.connector
import time
from time import strftime
from PIL import ImageTk,Image
import datetime as dt


root=Tk()
root.title('JH MOBILE')
root.attributes('-fullscreen', True)
# root.wm_iconbitmap('store.ico')
root.configure(background='#00FFFF')

# -----------creating the heading for the GUI-----------------
f1=Frame(root,bg='#00FFFF')
f1.pack(fill=X)
Label(f1,text="  JH MOBILE  ",font='Sans 40 bold',fg='white',bg='#1E90FF',relief=RIDGE,borderwidth=5,padx=5,pady=5).pack()

# ---------------creating the clse button--------------

Button(f1,text="Close",command=root.destroy,font="lucida 15 bold",fg="white",bg='blue').pack(side=RIGHT,anchor="ne",padx=10,pady=10)


# ------------------createing the date widget------------------
date = dt.datetime.now()
# print (date)
# Create Label to display the Date
label = Label(f1, text=f"\t{date:%A, %B %d, %Y}", font="Calibri 20 bold",bg='#00FFFF')
label.pack(pady=5,padx=10)

# ----------------Footer for gui-------------
Label(text='Developed By: Chandan Kr.',relief=GROOVE,fg='white',bg='grey',font='lucida 20 bold').pack(side=BOTTOM,anchor='s',fill=X)

# ------------clock for gui-----------------

label=Label(root,font='lucida 20 bold')
label.pack()
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input,bg='#00FFFF')
   label.after(200, digitalclock)
digitalclock()


#---------------clock closed--------------





# Connect to the MySQL database
db = mysql.connector.connect(
        host="<host-name>",
        user="<user-name>",
        password="<your-password>"
    )
dd= mysql.connector.connect(
        host="<host-name>",
        user="<user-name>",
        password="<your-password>"
    )
cur = db.cursor()
cur1 = dd.cursor()

cur.execute('create database if not exists Purchase')
cur1.execute('create database if not exists Sales')

cur.execute('use Purchase')
cur.execute('create table if not exists Addpurchase(Date varchar(30),Company varchar(100),Brand varchar(50),Model varchar(50),IMIE varchar(50))')
cur1.execute('use Sales')
cur1.execute('create table if not exists AddSales(Date varchar(30),Brand varchar(100),Model varchar(100),IMIE varchar(200))')

#------------making functions for the buttons-------------------------

#------Add to saless functions -------------------------
def addtosales():
    
    
    da = Dateentry.get()
    brand = Brandentry.get()
    model = Modelentry.get()
    imie= IMIEentry.get()
    
    # Insert values into the 'mobiles' table
    sql = "INSERT INTO AddSales (date,Brand,Model,IMIE) VALUES (%s, %s, %s,%s)"
    values = (da,brand,model,imie)
    
    cur1.execute(sql, values)
    dd.commit()

    # Clear the input fields after adding
    Dateentry.delete(0, END)
    companyentry.delete(0, END)
    Brandentry.delete(0, END)
    Modelentry.delete(0, END)
    IMIEentry.delete(0, END)
    
# --------Show sales functions-----------------
def showsales():
    
    
    from tkinter import ttk
    import tkinter as tk

    import mysql.connector

    # Creating tkinter window
    window = tk.Tk()
    window.title('Sales Report')
    window.resizable(width=10,height=10)

    # Using treeview widget
    treev = ttk.Treeview(window, selectmode ='browse',show='headings',height=50)

    # Calling pack method w.r.to treeview
    treev.pack(side ='right')


    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(window, orient ="vertical", command = treev.yview)

    # Calling pack method w.r.to vertical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')

    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3","4")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to the
    # respective columns
    treev.column("1", width = 200, anchor ='c')
    treev.column("2", width = 200, anchor ='c')
    treev.column("3", width = 200, anchor ='c')
    treev.column("4", width = 300, anchor ='c')

    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Date")
    treev.heading("2", text ="Brand")
    treev.heading("3", text ="Model")
    treev.heading("4", text ="IMIE")


    db=mysql.connector.connect(host='<host-name>',user='<user-name>',password="<your-password>")
    cur=db.cursor()
    cur.execute('use sales')
    cur.execute('select * from addsales')

    # Inserting the items and their features to the 
    # columns built
    i=0
    for sale in cur:
        treev.insert("", 'end', text =f'L{i}', values =sale)
        i+=1

    s = ttk.Style()
    s.theme_use('clam')

#    Configure the style of Heading in Treeview widget
    s.configure('Treeview.Heading', background="green3")
    # Calling mainloop
    window.mainloop()


# ----------------------add purchase function -------------------------------

def addpurchase():
    
    da = Dateentry.get()
    comp=companyentry.get()
    brand = Brandentry.get()
    model = Modelentry.get()
    imie= IMIEentry.get()
    
    # Insert values into the 'mobiles' table
    sql = "INSERT INTO addpurchase(date,company,Brand,Model,IMIE) VALUES (%s,%s, %s, %s,%s)"
    values = (da,comp,brand,model,imie)
    
    cur.execute(sql, values)
    db.commit()

    # Clear the input fields after adding
    Dateentry.delete(0, END)
    companyentry.delete(0, END)
    Brandentry.delete(0, END)
    Modelentry.delete(0, END)
    IMIEentry.delete(0, END)
    
# ---------------------------show purchase functions------------------------
def showpurchase():
    
    from tkinter import ttk
    import tkinter as tk

    import mysql.connector

    # Creating tkinter window
    window = tk.Tk()
    window.title('Sales Report')
    window.resizable(width=10,height=100)

    # Using treeview widget
    treev = ttk.Treeview(window, selectmode ='browse',show='headings',height=30)

    # Calling pack method w.r.to treeview
    treev.pack(side ='right')


    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(window, orient ="vertical", command = treev.yview)

    # Calling pack method w.r.to vertical 
# scrollbar
    verscrlbar.pack(side ='right', fill ='x')

    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)

# Defining number of columns
    treev["columns"] = ("1", "2", "3","4")

# Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to the
    # respective columns
    treev.column("1", width = 200, anchor ='c')
    treev.column("2", width = 200, anchor ='c')
    treev.column("3", width = 200, anchor ='c')
    treev.column("4", width = 300, anchor ='c')

    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Date")
    treev.heading("2", text ="Brand")
    treev.heading("3", text ="Model")
    treev.heading("4", text ="IMIE")


    db=mysql.connector.connect(host='<host-name>',user='<user-name>',password="<your-password>")
    cur=db.cursor()
    cur.execute('use purchase')
    cur.execute('select * from addpurchase')

    # Inserting the items and their features to the 
    # columns built
    i=0
    for purchase in cur:
        treev.insert("", 'end', text =f'L{i}', values =purchase)
        i+=1


    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    
    window.mainloop()



# --------------------------print the sales to store in a txt file for printing------------------
def printsales():
    with open('salesrecord.txt','w') as f:
        
        cur1.execute("SELECT * FROM addsales ")
    
        
    
        i=1
        f.write('Date \t\t||\t Brand \t   \t||\t Model \t||\t\t IMIE\t\t\t|| \n')
    
        for sale in cur1:
            # f.write(f'{purchase}\n')
            for j in range(len(sale)):
                f.write(f'{sale[j]} ||\t\t ')
                # e.insert(END, sale[j])
            f.write('\n')
            i+=1
    


# --------------------------printing the purchase -------------------------------

def printpurchase():
    with open('purchaserecords.txt','w') as f:
        
        cur.execute("SELECT * FROM addpurchase ")
    
        
        i=1
        f.write('Date \t\t||\t\t Company \t\t\t\t\t||\t\t Brand \t||\t\t Model \t\t||\t\t IMIE\t\t\t|| \n')
    
        for purchase in cur:
            # f.write(f'{purchase}\n')
            for j in range(len(purchase)):
                f.write(f'{purchase[j]} ||\t\t ')
                # e.insert(END, sale[j])
            f.write('\n')
            i+=1
    

    

ff=Frame(root,width=50,relief=SUNKEN,borderwidth=10,bg='#00BFFF')
ff.pack(side=LEFT,anchor='nw',padx=20,pady=10,fill=Y)




Label(ff,text="Date : ",font="Times 20 bold",bg='#00BFFF').grid(row=1,column=2,pady=8,padx=10)
Label(ff,text="Company : ",font="Times 20 bold",bg='#00BFFF').grid(row=2,column=2,pady=8,padx=10)
Label(ff,text="Brand : ",font="Times 20 bold",bg='#00BFFF').grid(row=3,column=2,pady=8,padx=10)
Label(ff,text="Model : ",font="Times 20 bold",bg='#00BFFF').grid(row=4,column=2,pady=8,padx=10)
Label(ff,text="IMIE : ",font="Times 20 bold",bg='#00BFFF').grid(row=5,column=2,pady=8,padx=10)

# ------------making user entry------------------

Dateentry=Entry(ff,font="Times 20 bold")
companyentry=Entry(ff,font="Times 20 bold")
Brandentry=Entry(ff,font="Times 20 bold")
Modelentry=Entry(ff,font="Times 20 bold")
IMIEentry=Entry(ff,font="Times 20 bold")

Dateentry.grid(row=1,column=3,pady=8,padx=10)
companyentry.grid(row=2,column=3,pady=8,padx=10)
Brandentry.grid(row=3,column=3,pady=8,padx=10)
Modelentry.grid(row=4,column=3,pady=8,padx=10)
IMIEentry.grid(row=5,column=3,pady=8,padx=10)




# ------------------------------------purchase section -------------------------------

f2=Frame(root,bg='#00BFFF',relief=SUNKEN,borderwidth=5)
f2.pack(padx=10,pady=20,anchor='sw',fill=X)

Label(f2,text="Purchase",font='lucida 30 bold',fg='#8B0000',bg="#00BFFF").pack()

b=Button(f2,text='Add Purchase',command=addpurchase,bg='grey',fg='white',font="lucida 20",relief=RAISED,borderwidth=5)
b.pack(anchor='w',side=LEFT,padx=50,pady=10)

b=Button(f2,text='Show Purchase',command=showpurchase,bg='grey',fg='white',font="lucida 20",relief=RAISED,borderwidth=5)
b.pack(anchor='w',side=LEFT,padx=100,pady=10)

b=Button(f2,text='Print',command=printpurchase,bg='grey',fg='white',font="lucida 20",relief=RAISED,borderwidth=5)
b.pack(anchor='w',side=LEFT,padx=50,pady=10)



# ------------------------Sales section-----------------------

f3=Frame(root,bg='#00BFFF',relief=SUNKEN,borderwidth=5)
f3.pack(padx=10,pady=20,anchor='sw',fill=X)

Label(f3,text="Total Sales",font='lucida 30 bold',fg='#8B0000',bg="#00BFFF").pack()

b=Button(f3,text='Add Sales',command=addtosales,bg='grey',fg='white',font="lucida 20",relief=RAISED,borderwidth=5)
b.pack(anchor='w',side=LEFT,padx=50,pady=10)

b=Button(f3,text='Show Sales',command=showsales,bg='grey',fg='white',font="lucida 20",relief=RAISED,borderwidth=5)
b.pack(anchor='w',side=LEFT,padx=160,pady=10)

b=Button(f3,text='Print',command=printsales,bg='grey',fg='white',font="lucida 20",relief=RAISED,borderwidth=5)
b.pack(anchor='w',side=LEFT,padx=50,pady=10)


# -------------------------making the stocks sales ---------------

f5=Frame(root,borderwidth=10,relief=SUNKEN,bg='#00BFFF')
f5.pack(side=LEFT,anchor='w',padx=10)

Label(f5,text='Sales',font='Times 30 bold',fg='#8B0000',bg='#00BFFF').grid(row=0,column=10,pady=5)
cur1.execute('Select * from addsales')
sam=0
opp=0
tec=0
vivo=0
red=0
real=0
infix=0
itel=0
moto=0
nokia=0
poco=0

for sale in cur1:
    
    if(sale[1].lower()=='samsung'):
        sam+=1
    elif(sale[1].lower()=='oppo'):
        opp+=1
    elif(sale[1].lower()=='tecno'):
        tec+=1
    elif(sale[1].lower()=='vivo'):
        vivo+=1
    elif(sale[1].lower()=='redmi'):
        red+=1
    elif(sale[1].lower()=='realme'):
        real+=1
    elif(sale[1].lower()=='infinix'):
        infix+=1
    elif(sale[1].lower()=='itel'):
        itel+=1
    elif(sale[1].lower()=='nokia'):
        nokia+=1
    elif(sale[1].lower()=='poco'):
        poco+=1
    elif(sale[1].lower()=='moto'):
        moto+=1
    Label(f5,text='Samsung = ',font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=1,padx=5)
    Label(f5,text=sam,font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=2,padx=5)
    
    Label(f5,text='OPPO = ',font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=1,padx=5)
    Label(f5,text=opp,font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=2,padx=5)
    
    Label(f5,text='Vivo = ',font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=1,padx=5)
    Label(f5,text=vivo,font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=2,padx=5)
    
    Label(f5,text='tecno = ',font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=1,padx=5)
    Label(f5,text=tec,font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=2,padx=5)
    
    Label(f5,text='Redmi = ',font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=1,padx=5)
    Label(f5,text=red,font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=2,padx=5)
    
    Label(f5,text='Realme = ',font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=20,padx=5)
    Label(f5,text=real,font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=21,padx=5)
    
    Label(f5,text='Infinix = ',font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=20,padx=5)
    Label(f5,text=infix,font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=21,padx=5)
    
    Label(f5,text='Nokia = ',font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=20,padx=5)
    Label(f5,text=nokia,font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=21,padx=5)
    
    Label(f5,text='POCO= ',font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=20,padx=5)
    Label(f5,text=poco,font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=21,padx=5)
    
    Label(f5,text='Moto= ',font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=20,padx=5)
    Label(f5,text=moto,font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=21,padx=5)


# ------------------for purchase stokes---------------

f6=Frame(root,relief=SUNKEN,borderwidth=10,bg='#00BFFF')
f6.pack(side=LEFT,anchor='e',padx=20)

Label(f6,text='Total Purchase',font='Times 30 bold',fg='#8B0000',bg='#00BFFF').grid(row=0,column=25,pady=5)
cur.execute('Select * from Addpurchase')

sam1=0
opp1=0
tec1=0
vivo1=0
red1=0
real1=0
infix1=0
itel1=0
moto1=0
nokia1=0
poco1=0

for purchase in cur:
    
    if(purchase[2].lower()=='samsung'):
        sam1+=1
    elif(purchase[2].lower()=='oppo'):
        opp1+=1
    elif(purchase[2].lower()=='tecno'):
        tec1+=1
    elif(purchase[2].lower()=='vivo'):
        vivo1+=1
    elif(purchase[2].lower()=='redmi'):
        red1+=1
    elif(purchase[2].lower()=='realme'):
        real1+=1
    elif(purchase[2].lower()=='infinix'):
        infix1+=1
    elif(purchase[2].lower()=='itel'):
        itel1+=1
    elif(purchase[2].lower()=='nokia'):
        nokia1+=1
    elif(purchase[2].lower()=='poco'):
        poco1+=1
    elif(purchase[2].lower()=='moto'):
        moto11+=1
    Label(f6,text='Samsung = ',font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=20,padx=5)
    Label(f6,text=sam1,font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=21,padx=5)
    
    Label(f6,text='OPPO = ',font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=20,padx=5)
    Label(f6,text=opp1,font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=21,padx=5)
    
    Label(f6,text='Vivo = ',font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=20,padx=5)
    Label(f6,text=vivo1,font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=21,padx=5)
    
    Label(f6,text='tecno = ',font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=20,padx=5)
    Label(f6,text=tec1,font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=21,padx=5)
    
    Label(f6,text='Redmi = ',font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=20,padx=5)
    Label(f6,text=red1,font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=21,padx=5)
    
    Label(f6,text='Realme = ',font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=30,padx=5)
    Label(f6,text=real1,font='lucida 12 bold',bg='#00BFFF').grid(row=1,column=31,padx=5)
    
    Label(f6,text='Infinix = ',font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=30,padx=5)
    Label(f6,text=infix1,font='lucida 12 bold',bg='#00BFFF').grid(row=2,column=31,padx=5)
    
    Label(f6,text='Nokia = ',font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=30,padx=5)
    Label(f6,text=nokia1,font='lucida 12 bold',bg='#00BFFF').grid(row=3,column=31,padx=5)
    
    Label(f6,text='POCO= ',font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=30,padx=5)
    Label(f6,text=poco1,font='lucida 12 bold',bg='#00BFFF').grid(row=4,column=31,padx=5)
    
    Label(f6,text='Moto= ',font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=30,padx=5)
    Label(f6,text=moto1,font='lucida 12 bold',bg='#00BFFF').grid(row=5,column=31,padx=5)
    
    
root.mainloop()
