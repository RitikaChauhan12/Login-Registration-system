from tkinter import*
from PIL import Image, ImageTk  
from tkinter import messagebox,ttk
import pymysql                                              
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.root.geometry("1199x600+100+50")
        
        #=======bg image======#
        self.pic = ImageTk.PhotoImage(file="login-background.jpg")
        pic = Label(self.root, image=self.pic)
        pic.place(x=0, y=0, relwidth=1, relheight=1)
        #####login frame###
        loginframe = Frame(self.root, bg="#90EC82")
        loginframe.place(x=150, y=150, height=400, width=500)

        login_label = Label(loginframe, text="Login Here", fg="black", bg="#90EC82", font=("Times",
                                                                            30, "bold"))                       
        login_label.place(x=75, y=30)

        username_label = Label(loginframe, text="Username: ", font=("Goudy old style",
                                                                    14, "bold"),fg="grey", bg="#90EC82")                     
        username_label.place(x=75, y=110)
        username_var = StringVar()
        self.username_entrybox = Entry(loginframe, textvariable=username_var, bg="lightgrey", font=("Times",15))
        self.username_entrybox.place(x=75, y=150, height=35, width=350)
        self.username_entrybox.focus()


        password_label = Label(loginframe, text="Password: ", font=("Goudy old style",
                                                                    14, "bold"), fg="grey", bg="#90EC82")                     
        password_label.place(x=75, y=200)

        password_var = StringVar()
        self.password_entrybox = Entry(loginframe, textvariable=password_var, bg="lightgrey",font=("Times",15))
        self.password_entrybox.place(x=75, y=240, height=35, width=350)


############################forget password#################################
        forget = Button(loginframe, text="Forget Password?", command=self.forget_window, font=("Times", 12), fg="black", bd=0, bg="#90EC82")
        forget.place(x=70, y=290)


        register = Button(loginframe, cursor="hand2", command =self.register_window, text="Register new user?",font=("Times", 12), fg="blue",bd=0, bg="#90EC82")
        register.place(x=250, y=290)


        login = Button(loginframe, cursor="hand2", text="Login", command=self.login_function,font=("Times", 20), fg="black", bg="#90EC82")
        login.place(x=160, y=340, width=180, height=40)

########################### Reset #####################
    def reset(self):
        self.combo_entrybox.current(0)
        self.answer_entrybox.delete(0,END)
        self.newpass_entrybox.delete(0,END)
        self.username_entrybox.delete(0,END)
        self.password_entrybox.delete(0,END)
#################### verifying the user details according to mention  in db########################
    def forget_pass(self):
        if self.combo_entrybox.get()=="Select" or self.answer_entrybox.get()=="" or self.newpass_entrybox.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="login")
                cur=con.cursor()
                cur.execute("select * from logindetails where email=%s and question=%s and answer=%s" ,(self.username_entrybox.get(),self.combo_entrybox.get(),self.answer_entrybox.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select Correct Security Question/Correct Answer",parent=self.root2)
                else:
                    cur.execute("update logindetails set password=%s where email=%s " ,(self.newpass_entrybox.get(),self.username_entrybox.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","You Password has been Reset, Please login with new Password",parent=self.root2)
                    self.reset()
                    self.root2.destroy() 
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root)



################################# forget window ######################################
    def forget_window(self):
        if self.username_entrybox.get()== "":
            messagebox.showerror("Error","Please Enter Username to Reset Your Password",parent=self.root)
            # messagebox.showerror("Error","Please Enter Valid Username to Reset Your Password",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="login")
                cur=con.cursor()
                cur.execute("select * from logindetails where email=%s" ,self.username_entrybox.get())
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter Valid Username to Reset Password",parent=self.root)
                else:
                    con.close()
                    self.verify_window()
            except Exception as es:
                        messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root)

################################# Display forget window ##########################
    def verify_window(self):
        self.root2= Toplevel()
        self.root2.title("FORGET PASSWORD")
        self.root2.geometry("500x400+250+230")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()
        f = Label(self.root2, text="Forget Password", fg="red", bg="white", font=("Times",
                                                                            20, "bold"))                       
        f.place(x=5, y=0,relwidth=1)

        question_label = Label(self.root2, text="Security Question",bg="white", font=("Times",14, "bold"),fg="grey")                                                                              
        question_label.place(x=125, y=100)

        self.combo_entrybox = ttk.Combobox(self.root2, font=("Times", 15), state="readonly", justify=CENTER)
        self.combo_entrybox["values"] = ("Select", "Your Birthday", "Your favourite color", "Your pet name")
        self.combo_entrybox.place(x=125, y=130, height=25, width=250)
        self.combo_entrybox.current(0)

        answer_label = Label(self.root2, text="Answer", font=("Times", 14, "bold"),fg="grey", bg="white")                                                                             
        answer_label.place(x=125, y=180)

        self.answer_entrybox = Entry(self.root2, bg="lightgray", font=("Times",15))
        self.answer_entrybox.place(x=125, y=210, height=25, width=250)


        newpass_label = Label(self.root2, text="New Password", font=("Times", 14, "bold"),fg="grey", bg="white")                                                                             
        newpass_label.place(x=125, y=260)

        self.newpass_entrybox = Entry(self.root2, bg="lightgray", font=("Times",15))
        self.newpass_entrybox.place(x=125, y=290, height=25, width=250)


        submit = Button(self.root2, cursor="hand2",command=self.forget_pass, text="Reset Password",font=("Times", 15,"bold"), fg="green", bg="white")
        submit.place(x=170, y=340, width=150, height=40)

    
############################function to connect with register ###############################
    def register_window(self):
        self.root.destroy()
        import register

########################## login function with conditions #################################
    def login_function(self):
        if self.username_entrybox.get()=="" or self.password_entrybox.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="login")
                cur=con.cursor()
                cur.execute("select * from logindetails where email=%s and password = %s",(self.username_entrybox.get(),self.password_entrybox.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import thankyou


            except Exception as es:
                        messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root)
        

    


root = Tk()
obj = LoginWindow(root)
root.mainloop()
