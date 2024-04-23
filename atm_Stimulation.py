import tkinter as tk
import time

root=tk.Tk()
root.geometry('900x850')
root.title('ATM Stimulation')
root.configure(bg="black")

#top frame to add the title and the current 
Tops=tk.Frame(root,bg='white',width=800,height=50,relief=tk.SUNKEN)
Tops.pack(side='top')

localtime=time.asctime(time.localtime(time.time()))

#add title
lbl1=tk.Label(Tops,font=('arial',30,'bold'),text="ATM MACHINE",fg="Powder Blue",bg='Black',bd=10,anchor='w')
lbl1.grid(row=0,column=0)

#add current time
lbl2=tk.Label(Tops,text=localtime,font=('arial',20,'bold'),fg="Powder Blue",bg='Black',bd=10,anchor='w')
lbl2.grid(row=1,column=0)

#frame for entry boxes
f1=tk.Frame(root,bg='black',width=300,height=700,relief=tk.SUNKEN)
f1.pack(side='left')

#frame for buttons
f2=tk.Frame(root,bg='black',width=400,height=700,relief=tk.SUNKEN)
f2.pack(side='right')

#getting values of entry boxes
number=tk.StringVar() #account number
amount=tk.StringVar() #total amount
withd=tk.StringVar()  #withdrawn amount
acca= " "

#checking either user registered or not 
def bank():
    global acca
    accno=["0092","27833","78364"]
    account=number.get()
    if account in accno:
        label.config(text="Registered User")
        bank={"0092":10000,"27833":20000,"78364":30000}
        balance=bank[account]
        acca=balance
    else:
        label.config(text='Non Registered User')

#account label
lbl=tk.Label(f1,font=('arial',16,'bold'),text="Enter The Account Number",fg="Powder Blue",bg='Black',bd=10,anchor='w')
lbl.grid(row=0,column=3)
text=tk.Entry(f1,font=('arial',16,'bold'),bg="Powder Blue",fg='Black',bd=6,textvariable=number,insertwidth=4,justify='right')
text.grid(row=0,column=4)
label=tk.Label(f1,font=('arial',16,'bold'),fg="Powder Blue",bg='Black',bd=10,anchor='w')
label.grid(row=1,column=4)
btnsubmit=tk.Button(f2,padx=16,pady=4,bd=10,fg="black",font=('arial',16,'bold'),width=7,text='Submit',bg='Powder Blue',command=bank)
btnsubmit.grid(row=0,column=4)

lblTotal=tk.Label(f1,text="                            ",fg="white",bg='Black')
lblTotal.grid(row=3,columnspan=10)

#deposit the amount
def deposit():
    global acca
    amo=float(amount.get())
    bal=acca+amo
    label3.configure(text=("Net Balance:",str(bal)))





#account deposited
lbl=tk.Label(f1,font=('arial',16,'bold'),text="Enter The Amount To Be Deposited",fg="Powder Blue",bg='Black',bd=10,anchor='w')
lbl.grid(row=4,column=3)
text=tk.Entry(f1,font=('arial',16,'bold'),bg="Powder Blue",bd=6,textvariable=amount,insertwidth=4,justify='right')
text.grid(row=4,column=4)
label3=tk.Label(f1,font=('arial',16,'bold'),fg="white",bg='Black',bd=10,anchor='w')
label3.grid(row=5,column=4)
btndeposit=tk.Button(f2,padx=16,pady=4,bd=10,fg="black",font=('arial',16,'bold'),width=7,text='Deposit',bg='Powder Blue',command=deposit)
btndeposit.grid(row=4,column=4)

lblTotal=tk.Label(f1,text="                            ",fg="white",bg='Black')
lblTotal.grid(row=7,columnspan=10)

#withdrawn amount
lbl=tk.Label(f1,font=('arial',16,'bold'),text="Enter The Amount To Be withdrawn: ",fg="Powder Blue",bg='Black',bd=10,anchor='w')
lbl.grid(row=8,column=3)
text=tk.Entry(f1,font=('arial',16,'bold'),bg="Powder Blue",bd=6,textvariable=withd,insertwidth=4,justify='right')
text.grid(row=8,column=4)
label4=tk.Label(f1,font=('arial',16,'bold'),fg="white",bg='Black')
label4.grid(row=9,column=4)
label5=tk.Label(f1,font=('arial',16,'bold'),fg="white",bg='Black')
label5.grid(row=10,column=4)

#withdrawn amount
def withdrawn():
    global acca

    wd=float(withd.get())
    if acca>=wd:
        ace=acca-wd
        label4.configure(text=("Net Balance:",str(ace)))
    else:
        label4.config(text="Insufficient Balance")

btnwithdraw=tk.Button(f2,padx=16,pady=4,bd=10,fg="black",font=('arial',16,'bold'),width=7,text='WITHDRAW',bg='Powder Blue',command=withdrawn)
btnwithdraw.grid(row=8,column=4)

#check balance
def balance():
    global acca
    label5.config(text=("Net Balance:",str(acca)))

btnbal=tk.Button(f2,padx=16,pady=4,bd=10,fg="black",font=('arial',16,'bold'),width=7,text='BALANCE',bg='Powder Blue',command=balance)
btnbal.grid(row=10,column=4)

#reset all the details
def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")

#reset button
btnreset=tk.Button(f2,padx=16,pady=4,bd=10,fg="black",font=('arial',16,'bold'),width=7,text='RESET',bg='Powder Blue',command=reset)
btnreset.grid(row=11,column=4)

#exxit button
btnexit=tk.Button(f2,padx=16,pady=4,bd=10,fg="black",font=('arial',16,'bold'),width=7,text='EXIT',bg='Powder Blue',command=root.destroy)
btnexit.grid(row=12,column=4)



root.mainloop()