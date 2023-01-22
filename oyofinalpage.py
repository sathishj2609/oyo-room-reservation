from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import calendar
import mysql.connector as mc
import time

class Final():
    def __init__(self,win,*args):
        global photo6
        self.win1=win
        self.win1.title('sucess page')
        self.win1.geometry('2000x900')
        self.win1.configure(bg='#fff')
        url6=Image.open('oyoroom2.webp')
        url6=url6.resize((1700,800),Image.Resampling.LANCZOS)
        photo6=ImageTk.PhotoImage(url6)
        lbl=Label(self.win1,image=photo6)
        lbl.place(x=0,y=0,width=1700,height=800)
        lbl=Label(self.win1,text = 'Reseversion Sucessfully Thanks For Booking',bg='white',font=('Microsoft Yahei UI Light',25,'bold'))
        lbl.place(x=490,y=270)
        
        self.hotelname=args[0]
        self.price=args[1]
        self.roomno=args[2]
        self.diff = args[4]
        
        self.name=args[3]
        self.totalamount=str(int(self.price)*int(self.roomno)*int(self.diff))

        conn = mc.connect(host="localhost",user="root", password="",  database="oyoroom")
        cur = conn.cursor()
        cur.execute("select name, phone_number,Email_Id,ID_Proof,Check_in_Date,Check_out_Date,Adults,Child from oyo where name='"+self.name+"'")
        self.det=cur.fetchall()
        self.phno=self.det[0][1]
        self.email=self.det[0][2]
        self.id=self.det[0][3]
        self.checkin=self.det[0][4]
        self.checkout=self.det[0][5]
        self.adults=self.det[0][6]
        self.child=self.det[0][7]
        
        textarea=Text(self.win1,bg='white',height=38,width=40,font=("times new roman",14,'bold'))
        textarea.place(x=0,y=0)
        bill='''*************************************************
        \t\t oyo room bill
 ************************************************'''

        textarea.insert(END,f'\n-------------------ROOM booking details--------')
        textarea.insert(END,f'\nName: {self.name}')
        textarea.insert(END,f'\nPhone number :{self.phno}')
        textarea.insert(END,f'\nId prof type :{self.id}')
        #textarea.insert(END,f'\nAddress: {self.cur.get()}') 
        textarea.insert(END,f'\n------------------booking details---------------')
        textarea.insert(END,f'\ncheck-in date: {self.checkin}')
        textarea.insert(END,f'\ncheck-out date: {self.checkout}')
        textarea.insert(END,f'\nnumber of adults: {self.adults}')
        textarea.insert(END,f'\nNumber of child; {self.child}')
        textarea.insert(END,f'\nNumber of rooms; {self.roomno}')
        textarea.insert(END,f'\nhotel name: {self.hotelname}')
        textarea.insert(END,f'\nprice per day: {self.price}')
        textarea.insert(END,f'\nNo.of day: {self.diff}')
        textarea.insert(END,f'\ntotal amount: {self.totalamount}')
        #textarea.insert(END,f'\ncheck-out date: {self.checkout}')
        textarea.config(state='disabled')

if __name__=="__main__":
    win=Tk()
    sat=Final(win)
