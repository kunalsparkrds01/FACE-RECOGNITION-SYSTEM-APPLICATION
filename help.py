from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        #Tittle
        title_lbl=Label(self.root, text="HELP DESK",font=("times new roman",28,"bold"),bg="pink",fg="darkblue")
        title_lbl.place(x=0,y=2,width=1280,height=40)
            
        #BG Image
        img_top=Image.open(r"C:\Face_Recognition_System\Images\developer.jpg")
        img_top=img_top.resize((1300,650))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
            
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40, width=1300, height=650) 
        
        dev_label=Label(f_lbl,text="Email: 51110804094@piemr.edu.in",font=("times new roman",18,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=5)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
        