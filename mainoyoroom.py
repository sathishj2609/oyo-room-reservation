from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import time
import mysql.connector as mc
from oyoroomlist import Roomlist

class Userdetail():
    def __init__(self,win):
        self.win1=win
        self.win1.title('oyo_room')
        self.win1.geometry('2000x900+0+0')
        url=Image.open('pasted image 0.png')
        url=url.resize((2000,900),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(url)
        lbl=Label(self.win1,image=self.photo)
        lbl.place(x=0,y=0,width=2000,height=900)
        self.diff = None
    
        self.lbl1=Label(self.win1,text='PLEASE FILL THE DETAILS',bg='silver',font=('arial',25,'bold'))
        self.lbl1.place(x=600, y=10)
        #calander
        self.cus_name=StringVar()
        self.cus_address=StringVar()
        self.cus_emailid=StringVar()
        self.cus_pincode=StringVar()
        self.cus_Phoneno=StringVar()
        
        self.cus_checkin=StringVar()
        self.cus_checkout=StringVar()
        
        self.cus_adults=StringVar()
        self.cus_child=StringVar()
        self.cus_room=StringVar()
        self.cus_id=StringVar()
        
        self.lbl2=Label(self.win1,text='check-in date',bg='silver',font=('arial',26,'bold'))
        self.lbl2.place(x=100,y=130)
        self.lbl3=Label(self.win1,text='check-out date',bg='silver',font=('arial',25,'bold'))
        self.lbl3.place(x=500,y=130)
        self.calin = DateEntry(self.win1,width=15 , selectmode='day',font=('arial',18,'bold'),bg='darkblue',fg='white',borderwidth = 1)
        self.calin.place(x=100,y=180)
        #print(self.calin.get_date())
        self.calout = DateEntry(self.win1,width=16 , selectmode='day',font=('arial',18,'bold'),bg='darkblue',fg='white',borderwidth = 1)
        self.calout.place(x=500,y=180)

        #labels
        
        self.lbl4=Label(self.win1,text='Adults',bg='silver',font=('arial',20,'bold'))
        self.lbl5=Label(self.win1,text='Child',bg='silver',font=('arial',20,'bold'))
        self.lbl6=Label(self.win1,text='Rooms',bg='silver',font=('arial',20,'bold'))
        
        #label places
        self.lbl4.place(x=100,y=350)
        self.lbl5.place(x=400,y=350)
        self.lbl6.place(x=650,y=350)
        #####__________________________________________________________________________
        
        self.adults=['select option','1','2','3','4','5','6','7','8','9']
        self.child=['select option','1','2','3','4','5','6','7','8','9']
        self.room=['select option','1','2','3','4']
        
        #entrys
        self.en3=ttk.Combobox(self.win1,value=self.adults,textvariable=self.cus_adults,font=('arial',20,'bold'))
        self.en3.current(0)
        self.en3.place(width=90)
        self.en4=ttk.Combobox(self.win1,value=self.child,textvariable=self.cus_child,font=('arial',20,'bold'))
        self.en4.place(width=90)
        self.en5=ttk.Combobox(self.win1,value=self.room,textvariable=self.cus_room,font=('arial',20,'bold'))
        self.en5.place(width=90)
        
        #entry places
        self.en3.place(x=100,y=400)
        self.en4.place(x=400,y=400)
        self.en5.place(x=660,y=400)
        
        #customer
        self.id=['select option','Aadhar card','Driving License','voter id']
        
        self.lbl1=Label(self.win1,text='User Details:',bg='silver',font=('arial',20,'bold'))
        self.lbl1.place(x=1170,y=50)
        self.lbl2=Label(self.win1,text='Name:',bg='silver',font=('arial',18,'bold'))
        self.lbl2.place(x=1080,y=110)
        self.lbl7=Label(self.win1,text='Phone No:',bg='silver',font=('arial',18,'bold'))
        self.lbl7.place(x=1080,y=170)
        self.lbl3=Label(self.win1,text='Address:',bg='silver',font=('arial',18,'bold'))
        self.lbl3.place(x=1080,y=230)
        self.lbl4=Label(self.win1,text='Email Id:',bg='silver',font=('arial',18,'bold'))
        self.lbl4.place(x=1080,y=290)
        self.lbl5=Label(self.win1,text='Pincode:',bg='silver',font=('arial',18,'bold'))
        self.lbl5.place(x=1080,y=350)
        self.lbl6=Label(self.win1,text='ID-Proof types:',bg='silver',font=('arial',18,'bold'))
        self.lbl6.place(x=1080,y=410)
                        
        #customer label entry
        self.en1=Entry(self.win1,textvariable=self.cus_name,font=('arial',18,'bold'))
        self.en1.place(x=1270,y=110)
        self.en2=Entry(self.win1,textvariable=self.cus_address,font=('arial',18,'bold'))
        self.en2.place(x=1270,y=230)
        self.en3=Entry(self.win1,textvariable=self.cus_emailid,font=('arial',18,'bold'))
        self.en3.place(x=1270,y=290)
        self.en4=Entry(self.win1,textvariable=self.cus_pincode,font=('arial',18,'bold'))
        self.en4.place(x=1270,y=350)
        self.en5=ttk.Combobox(self.win1,value=self.id,textvariable=self.cus_id,font=('arial',18,'bold'))
        self.en5.place(x=1270,y=410)
        self.en6=Entry(self.win1,textvariable=self.cus_Phoneno,font=('arial',18,'bold'))
        self.en6.place(x=1270,y=170)

        #Rooms info
        self.lbl1=Label(self.win1,text='Room price:',bg='silver',font=('arial',20,'bold'))
        self.lbl1.place(x=1080,y=520)
        self.lbl2=Label(self.win1,text='*Per day 1000 With Ac',bg='silver',font=('arial',18,'bold'))
        self.lbl2.place(x=1150,y=580)
        self.lbl3=Label(self.win1,text='*Two days 1800 With Ac',bg='silver',font=('arial',18,'bold'))
        self.lbl3.place(x=1150,y=640)
        self.lbl4=Label(self.win1,text='*One Weeks 5000 With Ac',bg='silver',font=('arial',18,'bold'))
        self.lbl4.place(x=1150,y=700)
        self.lbl5=Label(self.win1,text='*One Month 18000 With Ac',bg='silver',font=('arial',18,'bold'))
        self.lbl5.place(x=1150,y=760)
        
        #button            
        self.b2=Button(self.win1,text='Check for availability',bg='silver',font=('arial',20,'bold'),command=self.value)
        
        #button place
        self.b2.place(x=300,y=550)
        
    def value(self):
            
        if self.cus_name.get()== '':
            messagebox.showerror('Error','please enter your name',parent=self.win1)
        
        elif self.cus_address.get() == '':
            messagebox.showerror('Error','please enter your address',parent=self.win1)

        elif self.cus_emailid.get() == '':
            messagebox.showerror('Error','please enter your emailid',parent=self.win1)

        elif self.cus_pincode.get() == '':
            messagebox.showerror('Error','please enter your pincode',parent=self.win1)

        else:
            self.diff = ((self.calout.get_date())-(self.calin.get_date())).days

            e_name=self.cus_name.get()
            
            e_emailid=self.cus_emailid.get()
            
            e_phoneno=self.cus_Phoneno.get()
            
            e_checkin=self.calin.get()
            
            e_checkout=self.calout.get()
            
            e_adults=self.cus_adults.get()
            
            e_child=self.cus_child.get()
            
            e_room=self.cus_room.get()
            
            e_id=self.cus_id.get()
            
            conn = mc.connect(host="localhost",user="root", password="",  database="oyoroom")
            cur = conn.cursor()
            cur.execute("insert into oyo(name,phone_number,Email_id,ID_proof,Check_in_date,Check_out_date,Adults,Child,Rooms) values('"+e_name+"', '"+e_phoneno+"', '"+e_emailid+"','"+e_id+"','"+e_checkin+"','"+e_checkout+"','"+e_child+"','"+e_adults+"','"+e_room+"')")
            
            messagebox.showinfo('Info','data Inserted',parent=self.win1) 
            conn.close()
            
            screen=Toplevel(self.win1)
            obj=Roomlist(screen,self.cus_room.get(),self.cus_name.get(),self.diff)

    '''def on_entry(self,event):        
        self.en1_ent.delete(0,'end')
    def on_leave(self,event):
        name=self.en1_ent.get()
        if name=='':
            self.en1_ent.insert(0,'DD/MM/YY')

    def on_entry1(self,event):        
        self.en2_ent.delete(0,'end')
    def on_leave1(self,event):
        name=self.en2_ent.get()
        if name=='':
            self.en2_ent.insert(0,'DD/MM/YY')'''
   
if __name__=="__main__":
    win=Tk()
    sat=Userdetail(win)
