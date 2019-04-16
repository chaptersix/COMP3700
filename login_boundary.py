from tkinter import *
import sys

class login_boundary():
    # context = current window
    def __init__(self, context):
        self.context = context

        # window title 
        self.context.title("Login to TigerWallet")
        
        self.lbl = Label(context, text="Welcome to TigerWallet!")
        self.lbl.pack()

        self.lb2 = Label(context, text="Enter credentials to login!.")
        self.lb2.pack()

        # get username
        self.username = Entry(context, width=10)
        self.username.pack()

        self.password = Entry(context, width=10)
        self.password.pack()

         # parameters: window, text, function 
        self.login = Button(context, text="Login", command=self.start_home)
        self.login.pack()

        # quit 
        self.exit_btn = Button(context, text="Exit", command=context.quit)
        self.exit_btn.pack()

    # Destroy the current window and start homescreen use case
    def start_home(self):
        self.context.destroy()
        home = Tk()
        # placeholder 
        home.mainloop()



def start():
    # create login instance on root
    login = Tk()
    l = login_boundary(login)
    login.mainloop()
