#import this in Header file

from Face_recognition import Face_Recognition




#In Detect face Button paste this

img5=Image.open(r"         ")                  #Insert image in blank space
img5=img5.resize((220,220),Image.ANTIALIAS)
self.photoimg5=ImageTk.PhotoImage(img5)

b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
b1.place(x=500,y=100,width=220,height=220)

b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman"))
b1_1.place(x=500,y=300,width=220,height=40)



#At last we have to add this file in main.py
def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
        
        
        
#============================================================================================================
#If error in student.py

 #=============================== Get Cursor =========================================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        # Check if data is not empty and has sufficient length
        if data and len(data) >= 15:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])