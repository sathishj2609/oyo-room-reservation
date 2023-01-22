from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import calendar
from mainoyoroom import Userdetail

win=Tk()
img=PhotoImage(file='C:/Users/Admin/Pictures/OYO-ROO.png')
Label(win,image=img,border=0,bg='white').place(x=0,y=0)
win.title('sign in')
win.geometry('2000x900')
win.configure(bg='#fff')
        
def signin():
    username=user.get()
    password=code.get()        
    #conform_password=conform_code.get()

    if username=='sathish' and password=='092000':
        
        f = open('oyofile.txt','w+')
        f.write('login password')
        f.write('\n')
        f.write(f"User name :{username}")
        f.write('\n')
        f.write(f"password :{password}")
        f.write('\n')
        f.close()
        oyo=Toplevel(win)
        sat=Userdetail(oyo)

    elif username!='sathish' and password!='092000':
        messagebox.showerror("Invalid ",'invalid username and password')

    elif username!='sathish':
        messagebox.showwarning("Error ",'Enter your username')

    else:
        messagebox.showwarning("Error ",'Enter your password')
        
lbl1=Label(win,text='OYO ROOM BOOKING SIGNIN PAGE',fg='#57a1f8',bg='white',font=('arial',25,'bold'))
lbl1.place(x=530, y=3)
    
frame=Frame(win,width=600,height=600,bg='#fff')
frame.place(x=1050,y=150)

heading=Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',30,'bold'))
heading.place(x=100,y=2)
#_____________________________________________________
def on_entry(self):
    code.delete(0,'end')
def on_leave(self):
    name=code.get()
    if name=='':
        code.insert(0,'password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',15))#,show=('*'))
code.place(x=30,y=160)
code.insert(0, 'password')
code.bind("<FocusIn>",on_entry)
code.bind("<FocusOut>",on_leave)
#code.Entry(show="*")

Frame(frame,width=295,height=2,bg='black').place(x=25,y=197)
#______________________________________________________
def on_entry(e):
    user.delete(0,'end')
def on_leave(e):
     name=user.get()
     if name=='':
        user.insert(0,'username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',15))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_entry)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
Button(frame,width=39,pady=7,text='sign in',font=('microsoft Yahei UI Light',10,'bold'),bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=280)
#________________________________________________________
'''def on_entry(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'conform password')

conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0, 'conform password')
conform_code.bind("<FocusIn>",on_entry)
conform_code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)'''
#__________________________________________________________
