#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import pandas as pd
import random
import csv
import os

os.chdir('C://Users//91807//Desktop//DATA ANALYTICS PROJECT') #File address
result_file = pd.read_csv("high_acc_results.csv")  
info_file = pd.read_csv("test.csv")

root = Tk()
root.geometry('500x500')
root.title("Result Portal")

Employee_ID=StringVar()
Password=StringVar()
gen = IntVar()
dept_val=StringVar()


global n

def otp():
    global n
    n = random.randint(1000,10000)
    label_5 = Label(root, text="OTP sent to your registered mobile number.",fg='green',font=("bold", 8))
    label_5.place(x=180,y=300)
    phone = Tk()
    phone.geometry('300x400')
    phone.title("Mobile Phone - OTP")
    otpinfo = Label(phone, text="Your OTP is {otp}".format(otp=n))
    otpinfo.place(x=20,y=53)
    phone.mainloop()


def authenticate():
    global n
    os.chdir('C://Users//91807//Desktop//DATA ANALYTICS PROJECT')
    result_file = pd.read_csv("sub.csv")  
    info_file = pd.read_csv("test.csv")
    employee_id=Employee_ID.get()
    gender=gen.get()
    department=dept_val.get()
    password=Password.get()
    if gender==1:
        gender='m'
    else:
        gender='f'
    
    info_file=info_file[(info_file['employee_id']==int(employee_id)) & (info_file['gender']==gender)
                        & (info_file['department']==department)]
    if not info_file.empty and int(password)==n:
        result_file=result_file[result_file['employee_id']==int(employee_id)]
        if not result_file.empty:
            res_win = Tk()
            res_win.geometry('500x500')
            res_win.title("Result Portal - Authentication Successful - Status")
            if (result_file['is_promoted']==int(1)).bool():
                cw=['Congratulations on your well-deserved promotion!','Good luck in your new position.',
                    'You should be really happy and proud of your success.',
                    'Hope this promotion brings all kinds of new challenges and opportunities for you.',
                    'Way to climb that corporate ladder.',
                    'You worked hard for this and you deserve it.']
                result_p=('YES! '+cw[random.randint(0,5)])
            else:
                if (result_file['is_promoted']==int(0)).bool():
                    cf=['Every obstacle is a hidden step on the path to promotion.',
                    'Promotions will come and go, but your hard work will always shine and show.',
                    'Your effort is deeply, deeply appreciated.',
                    'I’m so grateful for all of your hard work. It definitely hasn’t gone unnoticed!',
                    'The difference between winning and losing is most often not quitting.']
                result_p=('No, '+cf[random.randint(0,4)]+' Better luck next time!')
            msg = Label(res_win, text="PROMOTION STATUS - {x}".format(x=result_p),font=("bold", 10))
            msg.place(x=20,y=53)
            msg.mainloop()              
            
    else:
        fwin = Tk()
        fwin.geometry('400x150')
        fwin.title("Result Portal - Authentication Failed")
        msg = Label(fwin, text="Authentication Failed - Retry again or contact us: admin@xyz.com")
        msg.place(x=20,y=53)
        msg.mainloop()
       

Disp_head = Label(root, text="Result Portal",width=20,font=("bold", 20))
Disp_head.place(x=90,y=53)


emp_lab = Label(root, text="Employee_ID",width=20,font=("bold", 10))
emp_lab.place(x=80,y=130)

emp_ent = Entry(root,textvar=Employee_ID)
emp_ent.place(x=240,y=130)

gen_lab = Label(root, text="Gender",width=20,font=("bold", 10))
gen_lab.place(x=80,y=180)

Radiobutton(root, text="Male",padx = 5, variable=gen, value=1).place(x=235,y=180)
Radiobutton(root, text="Female",padx = 20, variable=gen, value=2).place(x=290,y=180)

dept_lab = Label(root, text="Department",width=20,font=("bold", 10))
dept_lab.place(x=70,y=230)

dep_list = info_file.department.unique()

department_dropdown=OptionMenu(root,dept_val, *dep_list)
department_dropdown.config(width=15)
dept_val.set('select your dept.') 
department_dropdown.place(x=240,y=230)


pwd_lab = Label(root, text="Password",width=20,font=("bold", 10))
pwd_lab.place(x=80,y=280)

pwd_ent = Entry(root,textvar=Password,show='*')
pwd_ent.place(x=240,y=280)

Button(root, text='Request OTP',width=20,bg='navy',fg='white',command=otp).place(x=180,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=authenticate).place(x=180,y=380)

root.mainloop()


# 

# In[ ]:





# In[ ]:




