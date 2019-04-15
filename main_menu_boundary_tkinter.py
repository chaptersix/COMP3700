from tkinter import *
import sys


window = Tk()
window.geometry('500x250')

window.title("TigerWallet")
 
lbl = Label(window, text="Welcome to TigerWallet!")
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Login or Create an Account.")

login = Button(window, text="Login")
login.grid(column=0, row=1)

create_account = Button(window, text="Create Account")
create_account.grid(column=0, row=2)

exit_btn = Button(window, text="Exit", command=exit)
exit_btn.grid(column=0, row=3)

window.mainloop()