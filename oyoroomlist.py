from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import calendar
import time
import mysql.connector as mc
from oyofinalpage import Final

class Roomlist():
    def __init__(self,win,*args):
        self.win=win
        self.win.title('ROOM LIST')
        self.win.geometry('2000x900')
        url1=Image.open('oyoimg3.png')
        url1=url1.resize((2000,900),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(url1)
        lbl=Label(self.win,image=self.photo1)
        lbl.place(x=0,y=0,width=2000,height=900)
        self.diff=args[2]
        #head tittle
        self.lbl1=Label(self.win,text='WELCOME TO THE OYO ROOMS',bg='ivory',font=('arial',25,'bold'))
        self.lbl1.place(x=550,y=0)
        self.lbl2=Label(self.win,text='AVAILABLE ROOMS LIST:',font=('arial',20,'bold'))
        self.lbl2.place(x=0,y=60)
        self.lbl3=Label(self.win,text='Enter You Rooms No:',font=('arial',20,'bold'))
        self.lbl3.place(x=700,y=70)

        self.en1=Entry(self.win,width=15,font=('arial',20,'bold'))
        self.en1.place(x=700,y=110)
        self.roomno=args[0]
        #print(self.roomno)
        self.name=args[1]
        self.hotelname=''
        self.roomrate=None
        self.d1={'009':1000,'012':1200,'015':1500,'019':2000}
        
        b1=Button(self.win,text='Book Now',bg='white',font=('arial',15,'bold'),command=self.book)
        b1.place(x=1050,y=110)
        
        #buttons
        self.b2=Button(self.win,text='Room 009',font=('arial',15,'bold'),command=self.room009)
        self.b2.place(x=300,y=105)
        self.b3=Button(self.win,text='Room 012',font=('arial',15,'bold'),command=self.room012)
        self.b3.place(x=300,y=275)
        self.b4=Button(self.win,text='Room 015',font=('arial',15,'bold'),command=self.room015)
        self.b4.place(x=300,y=450)
        self.b5=Button(self.win,text='Room 019',font=('arial',15,'bold'),command=self.room019)
        self.b5.place(x=300,y=625)

        #frame
        self.frame=Frame(self.win,width=300,height=750,bg='#fff')
        self.frame.place(x=0,y=100)
        
        #frame image1
        url2=Image.open('frmimg.jpg')
        url2=url2.resize((300,165),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(url2)
        lbl1=Label(self.frame,image=self.photo2)
        lbl1.place(x=0,y=0,width=300,height=165)
        
        #frame image2
        url3=Image.open('oyoimg4.png')
        url3=url3.resize((300,170),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(url3)
        lbl2=Label(self.frame,image=self.photo3)
        lbl2.place(x=0,y=170,width=300,height=170)
        
        #frame image3
        url4=Image.open('oyoimg1.jpg')
        url4=url4.resize((300,170),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(url4)
        lbl3=Label(self.frame,image=self.photo4)
        lbl3.place(x=0,y=345,width=300,height=170)
        
        #frame image4
        url5=Image.open('oyoimg2.png')
        url5=url5.resize((300,170),Image.Resampling.LANCZOS)
        self.photo5=ImageTk.PhotoImage(url5)
        lbl4=Label(self.frame,image=self.photo5)
        lbl4.place(x=0,y=520,width=300,height=170)
        
    def room009(self):
        frame=Frame(self.win,width=900,height=670,bg='cornflowerblue')
        frame.place(x=700,y=160)

        url7=Image.open('frmimg.jpg')
        url7=url7.resize((900,330),Image.Resampling.LANCZOS)
        self.photo7=ImageTk.PhotoImage(url7)
        lbl5=Label(frame,image=self.photo7)
        lbl5.place(x=0,y=0,width=900,height=330)

        lbl1=Label(frame,text='OYO ROOMS Facilities:',bg='cornflowerblue',font=('arial',16,'bold'))
        lbl1.place(x=0,y=340)
        lbl2=Label(frame,text='* Free Parking',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl2.place(x=50,y=390)
        lbl3=Label(frame,text='* Family Rooms',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl3.place(x=50,y=440)
        lbl4=Label(frame,text='* Free WiFi',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl4.place(x=50,y=490)
        lbl5=Label(frame,text='* Non-smoking rooms',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl5.place(x=50,y=540)
        lbl6=Label(frame,text='*Hot Bath',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl6.place(x=50,y=590)

        lbl1=Label(frame,text='Room prices:',bg='cornflowerblue',font=('arial',16,'bold'))
        lbl1.place(x=300,y=340)
        lbl2=Label(frame,text='*Per day 1000 With Ac',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl2.place(x=330,y=390)
        lbl3=Label(frame,text='*Two days 1800 With Ac',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl3.place(x=330,y=440)
        lbl4=Label(frame,text='*One Weeks 5000 With Ac',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl4.place(x=330,y=490)
        lbl5=Label(frame,text='*One Month 18000 With Ac',bg='cornflowerblue',font=('arial',14,'bold'))
        lbl5.place(x=330,y=540)

        b1=Button(frame,text='cancel',bg='cornflowerblue',font=('arial',15,'bold'),command=frame.destroy)
        b1.place(x=800,y=610)

    def room012(self):
        frame=Frame(self.win,width=900,height=670,bg='#fff')
        frame.place(x=700,y=160)

        url8=Image.open('oyoimg4.png')
        url8=url8.resize((900,330),Image.Resampling.LANCZOS)
        self.photo8=ImageTk.PhotoImage(url8)
        lbl5=Label(frame,image=self.photo8)
        lbl5.place(x=0,y=0,width=900,height=330)

        lbl1=Label(frame,text='OYO ROOMS Facilities:',bg='white',font=('arial',16,'bold'))
        lbl1.place(x=0,y=340)
        lbl2=Label(frame,text='* Free Parking',bg='white',font=('arial',14,'bold'))
        lbl2.place(x=50,y=390)
        lbl3=Label(frame,text='* Family Rooms',bg='white',font=('arial',14,'bold'))
        lbl3.place(x=50,y=440)
        lbl4=Label(frame,text='* Free WiFi',bg='white',font=('arial',14,'bold'))
        lbl4.place(x=50,y=490)
        lbl5=Label(frame,text='* Non-smoking rooms',bg='white',font=('arial',14,'bold'))
        lbl5.place(x=50,y=540)
        lbl6=Label(frame,text='* Hot Both',bg='white',font=('arial',14,'bold'))
        lbl6.place(x=50,y=590)

        lbl1=Label(frame,text='Room price:',bg='white',font=('arial',16,'bold'))
        lbl1.place(x=300,y=340)
        lbl2=Label(frame,text='* Per day 1200 With Ac',bg='white',font=('arial',14,'bold'))
        lbl2.place(x=330,y=390)
        lbl3=Label(frame,text='* Two days 1800 With Ac',bg='white',font=('arial',14,'bold'))
        lbl3.place(x=330,y=440)
        lbl4=Label(frame,text='* One Weeks 6000 With Ac',bg='white',font=('arial',14,'bold'))
        lbl4.place(x=330,y=490)
        lbl5=Label(frame,text='* One Month 20000 With Ac',bg='white',font=('arial',14,'bold'))
        lbl5.place(x=330,y=540)

        b3=Button(frame,text='cancel',bg='white',font=('arial',15,'bold'),command=frame.destroy)
        b3.place(x=800,y=610)

    def room015(self):
        frame=Frame(self.win,width=900,height=670,bg='lemonchiffon')
        frame.place(x=700,y=160)

        url9=Image.open('oyoimg1.jpg')
        url9=url9.resize((900,330),Image.Resampling.LANCZOS)
        self.photo9=ImageTk.PhotoImage(url9)
        lbl5=Label(frame,image=self.photo9)
        lbl5.place(x=0,y=0,width=900,height=330)

        lbl1=Label(frame,text='OYO ROOMS Facilities:',bg='lemonchiffon',font=('arial',16,'bold'))
        lbl1.place(x=0,y=340)
        lbl2=Label(frame,text='* Free Parking',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl2.place(x=50,y=390)
        lbl3=Label(frame,text='* Family Rooms',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl3.place(x=50,y=440)
        lbl4=Label(frame,text='* Free WiFi',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl4.place(x=50,y=490)
        lbl5=Label(frame,text='* Non-smoking rooms',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl5.place(x=50,y=540)
        lbl6=Label(frame,text='* Hot Bath',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl6.place(x=50,y=590)

        lbl1=Label(frame,text='Room price:',bg='lemonchiffon',font=('arial',16,'bold'))
        lbl1.place(x=300,y=340)
        lbl2=Label(frame,text='* Per day 1500 With Ac',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl2.place(x=330,y=390)
        lbl3=Label(frame,text='* Two days 2500 With Ac',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl3.place(x=330,y=440)
        lbl4=Label(frame,text='* One Weeks 8000 With Ac',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl4.place(x=330,y=490)
        lbl5=Label(frame,text='* One Month 23000 With Ac',bg='lemonchiffon',font=('arial',14,'bold'))
        lbl5.place(x=330,y=540)

        b5=Button(frame,text='cancel',bg='lemonchiffon',font=('arial',15,'bold'),command=frame.destroy)
        b5.place(x=800,y=610)

    def room019(self):
        frame=Frame(self.win,width=900,height=670,bg='yellowgreen')
        frame.place(x=700,y=160)
            
        url10=Image.open('oyoimg2.png')
        url10=url10.resize((900,330),Image.Resampling.LANCZOS)
        self.photo10=ImageTk.PhotoImage(url10)
        lbl5=Label(frame,image=self.photo10)
        lbl5.place(x=0,y=0,width=900,height=330)

        lbl1=Label(frame,text='OYO ROOMS Facilities:',bg='yellowgreen',font=('arial',16,'bold'))
        lbl1.place(x=0,y=340)
        lbl2=Label(frame,text='* Free Parking',bg='yellowgreen',font=('arial',14,'bold'))
        lbl2.place(x=50,y=390)
        lbl3=Label(frame,text='* Family Rooms',bg='yellowgreen',font=('arial',14,'bold'))
        lbl3.place(x=50,y=440)
        lbl4=Label(frame,text='* Free WiFi',bg='yellowgreen',font=('arial',14,'bold'))
        lbl4.place(x=50,y=490)
        lbl5=Label(frame,text='* Non-smoking rooms',bg='yellowgreen',font=('arial',14,'bold'))
        lbl5.place(x=50,y=540)
        lbl6=Label(frame,text='* Hot Bath',bg='yellowgreen',font=('arial',14,'bold'))
        lbl6.place(x=50,y=590)

        lbl1=Label(frame,text='Room price:',bg='yellowgreen',font=('arial',16,'bold'))
        lbl1.place(x=300,y=340)
        lbl2=Label(frame,text='* Per day 2000 With Ac',bg='yellowgreen',font=('arial',14,'bold'))
        lbl2.place(x=330,y=390)
        lbl3=Label(frame,text='* Two days 2800 With Ac',bg='yellowgreen',font=('arial',14,'bold'))
        lbl3.place(x=330,y=440)
        lbl4=Label(frame,text='* One Weeks 10000 With Ac',bg='yellowgreen',font=('arial',14,'bold'))
        lbl4.place(x=330,y=490)
        lbl5=Label(frame,text='* One Month 32000 With Ac',bg='yellowgreen',font=('arial',14,'bold'))
        lbl5.place(x=330,y=540)

        b7=Button(frame,text='cancel',bg='yellowgreen',font=('arial',15,'bold'),command=frame.destroy)
        b7.place(x=800,y=610)

    def book(self):
        self.hotelname=(self.en1.get())
        self.roomrate=self.d1[self.hotelname]
        screen=Toplevel(self.win)
        obj=Final(screen,self.hotelname,self.roomrate,self.roomno,self.name,self.diff)
                    
   
if __name__=="__main__":
    win=Tk()
    sat1=Roomlist(win)
