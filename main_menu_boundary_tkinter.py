from tkinter import *
import sys
import login_boundary
import create_account_boundary


class main_menu_boundary():
    # context = current window
    def __init__(self, context):
        self.context = context

        # window title 
        self.context.title("TigerWallet")
        
        self.lbl = Label(context, text="Welcome to TigerWallet!")
        self.lbl.pack()

        self.lb2 = Label(context, text="Login or Create an Account.")
        self.lb2.pack()

        # parameters: window, text, function 
        self.login = Button(context, text="Login", command=self.start_login)
        self.login.pack()

        self.create_account = Button(context, text="Create Account", command=self.start_create_account)
        self.create_account.pack()

        self.exit_btn = Button(context, text="Exit", command=context.quit)
        self.exit_btn.pack()

    # Destroy the current window and start login use case
    def start_login(self):
        self.context.destroy()
        login_boundary.start()

    # Destroy the current window and start create account use case
    def start_create_account(self):
        self.context.destroy()
        create_account = Tk()
        # placeholder 
        create_account.mainloop()


# create main menu instance on root
root = Tk()
m = main_menu_boundary(root)
root.mainloop()