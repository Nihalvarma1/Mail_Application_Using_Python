from tkinter import *
import smtplib
from tkinter import filedialog

#Global Variables
attachments=[]

#Main Screen
master = Tk()
master.title('Custom Python Email App')
master.geometry("570x600+300+100")
master.configure(bg="#EDF4F2")

#Functions

    
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_reciever.get()
        subject = temp_subject.get()
        body = body_text.get(1.0,"end")
        
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notify_label.configure(text="All Fields are Required!!",fg="red")
        else:
            finalMessage = "Subject: {}\n\n{}".format(subject,body)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            server.sendmail(username,to,finalMessage)
            notify_label.configure(text="Email has been sent successfully",fg="green")
    except Exception as e:
        print(e)
        notify_label.configure(text="Error sending email",fg="red")
            
def reset():
    username_entry.delete(0,"end")
    password_entry.delete(0,"end")
    reciever_entry.delete(0,"end")
    subject_entry.delete(0,"end")
    body_text.delete(1.0,"end")
    notify_label.configure(text="",fg="red")

#Graphics
title_label=Label(master,text="Custom Email App",font=('Calibri',20,'bold'),bg="#EDF4F2",fg="#D32626",justify='center')
#title_label.grid(row=0, sticky=N)
title_label.place(x=200,y=10)

info_label=Label(master,text="Use the form below to send an email",font=('Calibri',12,'bold'),bg="#EDF4F2",justify='center',fg="#79D70F")
#info_label.grid(row=1, sticky=W, padx=5)
info_label.place(x=185,y=60)

email_label=Label(master,text="Email : ",font=('Calibri',13,'bold'),bg="#EDF4F2",fg="#F5A31A")
#email_label.grid(row=2, sticky=W, padx=5)
email_label.place(x=60,y=120)

password_label=Label(master,text="Password : ",font=('Calibri',13,'bold'),bg="#EDF4F2",fg="#F5A31A")
#password_label.grid(row=3, sticky=W, padx=5)
password_label.place(x=60,y=160)

to_label=Label(master,text="To : ",font=('Calibri',13,'bold'),bg="#EDF4F2",fg="#F5A31A")
#to_label.grid(row=4, sticky=W, padx=5)
to_label.place(x=60,y=200)

subject_label=Label(master,text="Subject : ",font=('Calibri',13,'bold'),bg="#EDF4F2",fg="#F5A31A")
#subject_label.grid(row=5, sticky=W, padx=5)
subject_label.place(x=60,y=240)

body_label=Label(master,text="Body : ",font=('Calibri',13,'bold'),bg="#EDF4F2",fg="#F5A31A")
#body_label.grid(row=6, sticky=W, padx=5)
body_label.place(x=60,y=280)

notify_label=Label(master,text="",font=('Calibri',15,'bold'),justify='center',width=46,bg="#EDF4F2")
#notify_label.grid(row=7, sticky=S, padx=5)
notify_label.place(x=50,y=550)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_reciever = StringVar()
temp_subject = StringVar()
#the body value is taken immediately after pressing send

#Entries
username_entry = Entry(master,font=('Calibri',13,'bold'),textvariable=temp_username,bg="#F1F0E8",fg="#4F4A45")
#username_entry.grid(row=2,column=0)
username_entry.place(x=150,y=120,width=380, height=30)

password_entry = Entry(master,font=('Calibri',13,'bold'),textvariable=temp_password,show="*",bg="#F1F0E8",fg="#4F4A45")
#password_entry.grid(row=3,column=0)
password_entry.place(x=150,y=160,width=380, height=30)

reciever_entry = Entry(master,font=('Calibri',13,'bold'),textvariable=temp_reciever,bg="#F1F0E8",fg="#4F4A45")
#reciever_entry.grid(row=4,column=0)
reciever_entry.place(x=150,y=200,width=380, height=30)

subject_entry = Entry(master,font=('Calibri',13,'bold'),textvariable=temp_subject,bg="#F1F0E8",fg="#4F4A45")
#subject_entry.grid(row=5,column=0)
subject_entry.place(x=150,y=240,width=380, height=30)

#Text area for Body to enter paragraphs of messages
body_text = Text(master, font=('Calibri',13,'bold'),width=20,fg="#4F4A45", height=3,bg="#F1F0E8")
body_text.place(x=150,y=280,width=380, height=180)

#Buttons
send_button=Button(master,font=('Calibri',13,'bold'),text="Send",fg="white",bg="#00A9FF",command=send)
#send_button.grid(row=7,sticky=W,padx=5,pady=15)
send_button.place(x=220,y=490)

reset_button = Button(master,font=('Calibri',13,'bold'),text="Reset",fg="white",bg="#00A9FF",command=reset)
#reset_button.grid(row=7,sticky=W,padx=45,pady=45)
reset_button.place(x=380,y=490)



master.mainloop()
