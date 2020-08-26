from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  
from tkinter import messagebox 
from tkinter import re        
import pymysql                                         
class Register:
    def __init__(self, window):
        self.window = window
        self.window.title("REGISTRATION")
        self.window.geometry("1350x700+0+0")
        self.window.config(bg="white")
        # self.window.resizable(False,False)

        ###############background image###################
        self.bg = ImageTk.PhotoImage(file="backgroundimage.jpg")
        picture = Label(self.window, image=self.bg)
        picture.place(x=0, y=0, relwidth=1, relheight=1)

        self.left = PhotoImage(file="regi.png")
        left = Label(self.window, image=self.left,bg="white")
        left.place(x=140, y=62, width=500, height=550)   
                


                ####################login frame##############
        loginframe = Frame(self.window, bg="white")
        loginframe.place(x=640, y=62, height=550, width=500)


                # create labels##############################################################
        register = Label(loginframe, text="REGISTER HERE", fg="black", bg="WHITE", font=("Times",20, "bold"))                                                                      
        register.place(x=130, y=30)

        #######################################row 1############################################
        
        firstname_label = Label(loginframe, text="First Name", font=("Times",14, "bold"),fg="grey", bg="white")                                                                              
        firstname_label.place(x=35, y=110)
        
        self.firstname_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.firstname_entrybox.place(x=35, y=140, height=25, width=180)
        self.firstname_entrybox.focus()

                
        lastname_label = Label(loginframe, text="Last Name", font=("Times", 14, "bold"),fg="grey", bg="white")                                                                             
        lastname_label.place(x=300, y=110)
                
        
        self.lastname_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.lastname_entrybox.place(x=300, y=140, height=25, width=180)
                
                
        ###############################row 2################################
                
        contact_label = Label(loginframe, text="Contact", font=("Times",14, "bold"),fg="grey", bg="white")                                                                              
        contact_label.place(x=35, y=180)
                
        self.contact_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.contact_entrybox.place(x=35, y=210, height=25, width=180)

                
        email_label = Label(loginframe, text="Email", font=("Times", 14, "bold"),fg="grey", bg="white")                                                                             
        email_label.place(x=300, y=180)
                

        self.email_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.email_entrybox.place(x=300, y=210, height=25, width=180)
                

        ###############################row 3########################################
        question_label = Label(loginframe, text="Security Question",bg="white", font=("Times",14, "bold"),fg="grey")                                                                              
        question_label.place(x=35, y=250)

        self.combo_entrybox = ttk.Combobox(loginframe, font=("Times", 15), state="readonly", justify=CENTER)
        self.combo_entrybox["values"] = ("Select", "Your Birthday", "Your favourite color", "Your pet name")
        self.combo_entrybox.place(x=35, y=280, height=25, width=180)
        self.combo_entrybox.current(0)

        answer_label = Label(loginframe, text="Answer", font=("Times", 14, "bold"),fg="grey", bg="white")                                                                             
        answer_label.place(x=300, y=250)

        self.answer_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.answer_entrybox.place(x=300, y=280, height=25, width=180)

        ############################################row4###########################################
        password_label = Label(loginframe, text="Password", font=("Times",14, "bold"),fg="grey", bg="white")                                                                              
        password_label.place(x=35, y=320)

        self.password_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.password_entrybox.place(x=35, y=350, height=25, width=180)

        confirm_label = Label(loginframe, text="Confirm Password", font=("Times", 14, "bold"),fg="grey", bg="white")                                                                             
        confirm_label.place(x=300, y=320)
                

        self.confirm_entrybox = Entry(loginframe, bg="lightgray", font=("Times",15))
        self.confirm_entrybox.place(x=300, y=350, height=25, width=180)

        #####################################chck button##############
        self.chck_var = IntVar()
        chckbtn = Checkbutton(loginframe, text = "I Agree the Terms & Condition", variable=self.chck_var, onvalue=1, offvalue=0, bg="white", font=("Times", 12))
        chckbtn.place(x=35, y=410)

        ##########################################register button#####################
        regist_button = Button(loginframe, text="REGISTER", justify=CENTER, cursor="hand2",command=self.register_data, bg="light blue", bd=0, font=("Times",15,"bold"))                           
        regist_button.place(x=190, y=480)       
                
        sign_button = Button(self.window, text="Sign In", command= self.login_window, justify=CENTER, cursor="hand2", bg="light blue", bd=0, font=("Times",15,"bold"))                           
        sign_button.place(x=340, y=480, width=80)  

    def login_window(self):
        self.window.destroy()
        import login


    def clear(self):
        self.firstname_entrybox.delete(0,END)
        self.lastname_entrybox.delete(0,END)
        self.contact_entrybox.delete(0,END)
        self.email_entrybox.delete(0,END)
        self.password_entrybox.delete(0,END)
        self.confirm_entrybox.delete(0,END)
        self.combo_entrybox.current(0)

    

    def register_data(self):
        if (self.firstname_entrybox.get()=="" or self.lastname_entrybox.get() =="" or self.contact_entrybox.get()=="" or self.email_entrybox.get()=="" or self.combo_entrybox.get()=="Select" or self.answer_entrybox.get==" " or self.password_entrybox.get()==" " or self.confirm_entrybox.get()== " "):
            messagebox.showerror("Error","All Fields are Required",parent=self.window)

        if (self.firstname_entrybox.get() and self.lastname_entrybox.get()):
            text = re.search(r'([a-zA-Z])\D*([a-zA-Z])$',self.firstname_entrybox.get()and self.lastname_entrybox.get())
            if text:
                pass
            else:
                messagebox.showerror("Error", "Enter Alphabets as First name",parent=self.window)

                
        if (self.contact_entrybox.get()):
            phone = re.search(r"^(0/91)?[7-9][0-9]{9}$",self.contact_entrybox.get())
            if (phone):
                pass
            else:
                messagebox.showerror("Error","Invalid Contact Format",parent=self.window)
        if (self.email_entrybox.get()):
            a = re.match(r"[\w-]{1,20}@\w{2,20}\.\w{2,3}$", self.email_entrybox.get())  
            if (a):
                pass
            else:
                messagebox.showerror("Error", "Please Enter a Valid Email", parent=self.window)

        if (self.password_entrybox.get()!= self.confirm_entrybox.get()):
                messagebox.showerror("Error", "Password & confirm password should be same", parent=self.window)
        if (self.chck_var.get()==0):
                messagebox.showerror("Error", "Please Agree our Terms & Condition",parent=self.window)
        

        else:
                try:
                        con = pymysql.connect(host="localhost",user="root",password="",database="login")
                        cur=con.cursor()
                        cur.execute("select * from logindetails where email=%s",self.email_entrybox.get())
                        row = cur.fetchone()
                        if row!=None:
                                messagebox.showinfo("Error","User Already ,Please Try Again with other Email",parent=self.window)

                        cur.execute("insert into logindetails(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                                                                (self.firstname_entrybox.get(),
                                                                        self.lastname_entrybox.get(),
                                                                        self.contact_entrybox.get(),
                                                                        self.email_entrybox.get(),
                                                                        self.combo_entrybox.get(),
                                                                        self.answer_entrybox.get(),
                                                                        self.password_entrybox.get()
                                                                        ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Info","Registration Successful",parent=self.window)
                        self.clear()

                except Exception as es:
                        messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.window)
                

            
        

        


win = Tk()
obj = Register(win)
win.mainloop()