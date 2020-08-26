from tkinter import*
from PIL import Image, ImageTk  
from tkinter import messagebox    

class ThankyouWindow:
    def __init__(self,win):
        self.win = win
        self.win.title("THANKYOU")
        self.win.geometry("1199x600+100+50")
        
        #=======bg image======#
        self.pic = ImageTk.PhotoImage(file="login-background.jpg")
        pic = Label(self.win, image=self.pic)
        pic.place(x=0, y=0, relwidth=1, relheight=1)

        Thankframe = Frame(self.win, bg="#F4F4F5")
        Thankframe.place(x=250, y=300, height=100, width=450)


        Thank_label = Label(Thankframe, text="THANKYOU", fg="black", bg="#F4F4F5", font=("Times",
                                                                            50, "bold"))                       
        Thank_label.place(x=25, y=10)



win = Tk()
obj = ThankyouWindow(win)
win.mainloop()