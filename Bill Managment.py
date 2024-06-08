import tkinter
from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_cookies.delete(0,END)
    entry_idly.delete(0,END)
    entry_puri.delete(0,END)
    entry_coffee.delete(0,END)
    entry_tea.delete(0,END)
    entry_juice.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(pancakes.get())
    except:a2=0

    try:a3=int(cookies.get())
    except:a3=0

    try:a4=int(Idly.get())
    except:a4=0

    try:a5=int(Puri.get())
    except:a5=0

    try:a6=int(coffee.get())
    except:a6=0

    try:a7=int(Tea.get())
    except:a7=0

    try:a8=int(juice.get())
    except:a8=0

    #define cost of each item per quantity
    c1=60*a1
    c2=40*a2
    c3=50*a3
    c4=30*a4
    c5=60*a5
    c6=10*a6
    c7=7*a7
    c8=20*a8


    lb1_total = Label(f2,font=("aria",18,"bold"),text="Total",width="16",fg="gold",bg="black")
    lb1_total.place(x=0,y=50)

    entry_total = Entry(f2,font=('aria',18,"bold"),textvariable=Total_bill,bd=6,width=15,bg="gold")
    entry_total.place(x=20,y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7+c8
    string_bill = "Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)
Label(text="BILL MANAGEMENT", bg="black",fg="white",font=("calibri",35),width="300",height="1").pack()

#MENU CARD
f=Frame(root,bg="orange",highlightbackground="black",highlightthickness=1,width=300,height=363)
f.place(x=10,y=128)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="orange").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa------ Rs.60/plate",fg="red",bg="orange").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancakes--- Rs.40/plate",fg="red",bg="orange").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies------ Rs.50/plate",fg="red",bg="orange").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Idly------ Rs.30/plate",fg="red",bg="orange").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Puri------ Rs.60/plate",fg="red",bg="orange").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Coffee------ Rs.10/cup",fg="red",bg="orange").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea------ Rs.7/cup",fg="red",bg="orange").place(x=10,y=260)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice------ Rs.20/glass",fg="red",bg="orange").place(x=10,y=290)

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=363)
f2.place(x=690,y=128)

Bill = Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#ENTRY WORK
f1=Frame(root,bd=5,height=363,width=300,relief=RAISED)
f1.pack()

dosa = StringVar()
pancakes = StringVar()
cookies = StringVar()
Idly = StringVar()
Puri = StringVar()
coffee = StringVar()
Tea = StringVar()
juice =StringVar()
Total_bill = StringVar()

#Label
lb1_dosa=Label(f1,font=("aria",16,"bold"),text="Dosa",width=12,fg="green4")
lb1_pancakes=Label(f1,font=("aria",16,"bold"),text="Pancakes",width=12,fg="green4")
lb1_cookies=Label(f1,font=("aria",16,"bold"),text="Cookies",width=12,fg="green4")
lb1_idly=Label(f1,font=("aria",16,"bold"),text="Idly",width=12,fg="green4")
lb1_puri=Label(f1,font=("aria",16,"bold"),text="Puri",width=12,fg="green4")
lb1_coffee=Label(f1,font=("aria",16,"bold"),text="Coffee",width=12,fg="green4")
lb1_tea=Label(f1,font=("aria",16,"bold"),text="Tea",width=12,fg="green4")
lb1_juice=Label(f1,font=("aria",16,"bold"),text="Juice",width=12,fg="green4")
lb1_dosa.grid(row = 1,column=0)
lb1_pancakes.grid(row = 2,column=0)
lb1_cookies.grid(row = 3,column=0)
lb1_idly.grid(row = 4,column=0)
lb1_puri.grid(row = 5,column=0)
lb1_coffee.grid(row = 6,column=0)
lb1_tea.grid(row = 7,column=0)
lb1_juice.grid(row = 8,column=0)

#ENTRY
entry_dosa=Entry(f1,font=("aria",16,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_pancakes=Entry(f1,font=("aria",16,"bold"),textvariable=pancakes,bd=6,width=8,bg="lightpink")
entry_cookies=Entry(f1,font=("aria",16,"bold"),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_idly=Entry(f1,font=("aria",16,"bold"),textvariable=Idly,bd=6,width=8,bg="lightpink")
entry_puri=Entry(f1,font=("aria",16,"bold"),textvariable=Puri,bd=6,width=8,bg="lightpink")
entry_coffee=Entry(f1,font=("aria",16,"bold"),textvariable=coffee,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",16,"bold"),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_juice=Entry(f1,font=("aria",16,"bold"),textvariable=juice,bd=6,width=8,bg="lightpink")

entry_dosa.grid(row=1,column=1)
entry_pancakes.grid(row=2,column=1)
entry_cookies.grid(row=3,column=1)
entry_idly.grid(row=4,column=1)
entry_puri.grid(row=5,column=1)
entry_coffee.grid(row=6,column=1)
entry_tea.grid(row=7,column=1)
entry_juice.grid(row=8,column=1)

#Buttons
btn_reset = Button(f1,bd=5,fg = "black",bg="lightblue",font=("ariel",16,"bold"),width=8,text="Reset",command=Reset)
btn_reset.grid(row=9,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=8,text="Total",command=Total)
btn_total.grid(row=9,column=1)



root.mainloop()