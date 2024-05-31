from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        #Tittle
        title_lbl=Label(self.root, text="DEVELOPER",font=("times new roman",28,"bold"),bg="pink",fg="darkblue")
        title_lbl.place(x=0,y=2,width=1280,height=40)
            
        #BG Image
        img_top=Image.open(r"C:\Face_Recognition_System\Images\developer.jpg")
        img_top=img_top.resize((1300,650))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
            
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40, width=1300, height=650) 
        
        # Frame of developer
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=820,y=0,width=450,height=500)
        
        # Developer Image
        img_top1=Image.open(r"C:\Users\kunalkanojiya\OneDrive\Desktop\Face_Recognition_System\me.jpg")
        img_top1=img_top1.resize((200,200))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=280,y=0,width=200,height=200)
        
        # Developer info
        dev_label=Label(main_frame,text="Hello My Self, kunal",font=("times new roman",18,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",18,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=40)
        
        #Image
        img3=Image.open(r"C:\Face_Recognition_System\Images\BG.jpg")
        img3=img3.resize((450,300))
        self.photoimg3=ImageTk. PhotoImage(img3)
        
        
        bg_img=Label(main_frame,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=450,height=300)







if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()