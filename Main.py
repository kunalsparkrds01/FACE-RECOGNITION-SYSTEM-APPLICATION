from tkinter import*
from tkinter import ttk
import tkinter
import tkinter as tk
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
import os 
from student import Student
from train import Train
from Face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help





class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        
        
        # first image
        img=Image.open(r"C:\Face_Recognition_System\Images\collage.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk. PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0, width=500, height=130)
        
        #Second Image
        img1=Image.open(r"C:\Face_Recognition_System\Images\face.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk. PhotoImage(img1)
        
        
        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400,y=0, width=500, height=130)
        
        
        # Third Image
        img2=Image.open(r"C:\Face_Recognition_System\Images\collage.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk. PhotoImage(img2)
        
        
        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900,y=0, width=500, height=130)
        
        
        #BG Image
        img3=Image.open(r"C:\Face_Recognition_System\Images\BG.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk. PhotoImage(img3)
        
        
        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1290,height=45)
        
        #================================= Time =============================================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
                
          
        
        #Student Button
        img4=Image.open(r"C:\Face_Recognition_System\Images\student.jpg")
        img4=img4.resize((270,250))
        self.photoimg4=ImageTk. PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=80,y=70,width=200,height=160)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=78,y=205,width=201,height=40)
        
        #Detect Face Button
        img5=Image.open(r"C:\Face_Recognition_System\Images\Face Detector.jpg")
        img5=img5.resize((230,200))
        self.photoimg5=ImageTk. PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=350,y=70,width=200,height=160)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=350,y=205,width=201,height=40)
        
        #Attendance Button
        img6=Image.open(r"C:\Face_Recognition_System\Images\Attendance.png")
        img6=img6.resize((230,200))
        self.photoimg6=ImageTk. PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=650,y=70,width=200,height=160)
        
        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=650,y=205,width=201,height=40)
        
        #Help Button
        img7=Image.open(r"C:\Face_Recognition_System\Images\Help Desk.png")
        img7=img7.resize((230,200))
        self.photoimg7=ImageTk. PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Help_data)
        b1.place(x=1000,y=70,width=200,height=160)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Help_data,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=1000,y=205,width=201,height=40)
        
        #Train Face Button
        img8=Image.open(r"C:\Face_Recognition_System\Images\Train Data.png")
        img8=img8.resize((230,200))
        self.photoimg8=ImageTk. PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=79,y=300,width=200,height=160)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=79,y=450,width=201,height=40)
        
        #Photo Face Button
        img9=Image.open(r"C:\Face_Recognition_System\Images\Photos.jpg")
        img9=img9.resize((230,200))
        self.photoimg9=ImageTk. PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=300,width=200,height=160)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=350,y=450,width=201,height=40)
        
        #Developer Button
        img10=Image.open(r"C:\Face_Recognition_System\Images\Developer.png")
        img10=img10.resize((230,200))
        self.photoimg10=ImageTk. PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer_data)
        b1.place(x=650,y=300,width=200,height=160)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer_data,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=650,y=450,width=201,height=40)
        
        #Exit Button
        img11=Image.open(r"C:\Face_Recognition_System\Images\Exit.jpg")
        img11=img11.resize((230,200))
        self.photoimg11=ImageTk. PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1000,y=300,width=200,height=160)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=1000,y=450,width=201,height=40)
        
    def open_img(self):
        os.startfile("Data")
    
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return
        
                
        #=============================== Functions Button =========================================
        
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def Help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        


        

               

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
    
