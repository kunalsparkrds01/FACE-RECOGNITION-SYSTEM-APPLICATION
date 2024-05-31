from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:             #Creating main class
    def __init__(self, root):       
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1300,height=55)
        
        # 1st image
        img_top=Image.open(r"C:\Face_Recognition_System\Images\Face Recognition.jpg")
        img_top=img_top.resize((650,700),)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
         
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=600)
        
        # 2nd image
        img_bottom=Image.open(r"C:\Face_Recognition_System\Images\Face Recognition 2.jpg")
        img_bottom=img_bottom.resize((950,700),)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
                              
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=650,height=600)
        
        # Button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor= "hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=220,y=540, width=200, height=40)
    
    # ==================== Attendance =================================    
    
    def mark_attendance(self,i,r,n,d):
        with open("Aryan.csv", "r+",newline="\n")as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list)and(r not in name_list)and(n not in name_list)and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H/%M/%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},present")
                  
   # ====================Face Recognition =================================
   
    def face_recog(self):     # Main Function
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):    #Sub function 1 (Drawing Boundray)  
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                                                
            coord=[]    #Create Empty Cordinate
            
            for (x,y,w,h) in features:                    # Here x,y are Axis & w,h are width and height
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)    #Drawing Rectangle
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))     # Using formula for finding Percentage Difference from Prediction
                
                
                # Taking Data from Student.py or MySQL
                conn=mysql.connector.connect (host="localhost",username="root",password="root",database="face_recgnizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))   # Using Id to match the data
                n=my_cursor.fetchone()
                if n:
                    n = "+".join(n)  # Name

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                if r:
                    r = "+".join(r)  # Roll number

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                if d:
                    d = "+".join(d)  # Department

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                if i:
                    i = "+".join(i)  # Student ID
                                    
                
                
                if confidence>75:         # Giving Prediction Data
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   #255 gives color in language of cv2 & 3 gives thickness
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   
                    cv2.putText(img,f"Name:{n})",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)   # (0,0,255) Gives red color
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]     #Filling Cordinates
                
            return coord
        
        def recognize(img,clf,faceCascade):      # Sub Function 2
           coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
           return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   
    
    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")        # Read data of classifier
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()        # Read Image
            img=recognize(img,clf,faceCascade)   #Recognize Image
            cv2.imshow("Welcome TO face Recognition",img)    
        
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()     # Help to close window with Enter key
            
               
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()