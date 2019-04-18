# from tkinter import *
import tkinter as tk 
import sys

class login_boundary():
    # context = current window
    def __init__(self, context):
        self.context = context

        # window title 
        self.context.title("Login to TigerWallet")
        
        self.lbl = tk.Label(context, text="Welcome to TigerWallet!")
        self.lbl.pack()

        self.lb2 = tk.Label(context, text="Enter credentials to login!.")
        self.lb2.pack()

        # get username
        self.username = tk.Entry(context, width=10)
        self.username.pack()

        self.password = tk.Entry(context, width=10)
        self.password.pack()

         # parameters: window, text, function 
        self.login = tk.Button(context, text="Login", command=self.start_home)
        self.login.pack()

        # quit 
        self.exit_btn = tk.Button(context, text="Exit", command=context.quit)
        self.exit_btn.pack()

    # Destroy the current window and start homescreen use case
    def start_home(self):
        self.context.destroy()
        home = tk.Tk()
        # placeholder 
        home.mainloop()



def start():
    # create login instance on root
    login = tk.Tk()
    l = login_boundary(login)
    login.mainloop()
