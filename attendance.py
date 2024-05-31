from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog

mydata =[]

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        
        #====================================== Variable ===========================================
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_attendance=StringVar()
        
    
        # first image
        img=Image.open(r"C:\Face_Recognition_System\Images\S1.jpg")
        img=img.resize((700,185))
        self.photoimg=ImageTk. PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0, width=700, height=185)
        
        #Second Image
        img1=Image.open(r"C:\Face_Recognition_System\Images\S2.jpg")
        img1=img1.resize((700,185))
        self.photoimg1=ImageTk. PhotoImage(img1)
        
        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=660,y=0, width=700, height=185)
        
        #BG Image
        img3=Image.open(r"C:\Face_Recognition_System\Images\BG.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk. PhotoImage(img3)
        
        
        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=3,y=180, width=1270, height=465)
        
        #Tittke bar
        title_lbl=Label(bg_img, text="Attendance Management System",font=("comicsansns 11 bold",24,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=-5,width=1305,height=40)
        
        # Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=4,y=40,width=1260,height=417)
        
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("comicsansns 11 bold",12,"bold"),fg="red")
        Left_frame.place(x=10,y=0,width=600,height=412)
        
        img_left=Image.open(r"C:\Face_Recognition_System\Images\CM.jpg")
        img_left=img_left.resize((580,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0, width=580, height=100)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=102,width=590,height=285)
        
        #======================================= Labeland Entry ================================================
        
        #Id
        attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("comicsansns 11 bold",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_id,font=("comicsansns 11 bold",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Roll No.
        roll_label=Label(left_inside_frame,text="Roll:",font=("comicsansns 11 bold",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_roll,font=("comicsansns 11 bold",13,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=8,sticky=W)
        
        #Name
        Name_label=Label(left_inside_frame,text="Name:",font=("comicsansns 11 bold",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Name_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_name,font=("comicsansns 11 bold",13,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Department
        dept_label=Label(left_inside_frame,text="Department:",font=("comicsansns 11 bold",13,"bold"),bg="white")
        dept_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        dept_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_dep,font=("comicsansns 11 bold",13,"bold"))
        dept_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #time
        time_label=Label(left_inside_frame,text="Time:",font=("comicsansns 11 bold",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_time,font=("comicsansns 11 bold",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Date
        date_label = Label(left_inside_frame,text="Date:",bg="white",font=("comicsansns 11 bold"))
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_attend_date,font=("comicsansns 11 bold",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Attendance
        attendance_label = Label(left_inside_frame,text="Attendance Status:",bg="white",font=("comicsansns 11 bold"))
        attendance_label.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=14,textvariable=self.var_attend_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #===========================================Buttons=============================================================
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=170,width=580,height=38)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=13,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=14,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=13,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Detail",font=("comicsansns 11 bold",12,"bold"),fg="red")
        Right_frame.place(x=613,y=0,width=643,height=412)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=0,width=632,height=385)
        
        
         #=============================== Scroll bar Table Frame =========================================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame, column=("id","roll","name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #=============================== Fetch Data using Button =========================================    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     
    # import CSV   
    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    #Export CSV
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data to export",parent=self.root)
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="open csv", filetypes=(("csv File", "*.csv"), ("ALL File", "*.*")), parent=self.root)    
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
       
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()