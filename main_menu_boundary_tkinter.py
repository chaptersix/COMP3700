from tkinter import *
import sys


class main_menu_boundary():
    def __init__(self, context):
        self.context = context

        self.context.title("TigerWallet")
        
        self.lbl = Label(context, text="Welcome to TigerWallet!")
        self.lbl.pack()

        self.lb2 = Label(context, text="Login or Create an Account.")
        self.lb2.pack()

        self.login = Button(context, text="Login", command=self.start_login)
        self.login.pack()

        self.create_account = Button(context, text="Create Account", command=self.start_create_account)
        self.create_account.pack()

        self.exit_btn = Button(context, text="Exit", command=context.quit)
        self.exit_btn.pack()

    def start_login(self):
        self.context.destroy()
        login = Tk()

        login.mainloop()

    def start_create_account(self):
        self.context.destroy()
        create_account = Tk()
        create_account.mainloop()




root = Tk()
m = main_menu_boundary(root)
root.mainloop()