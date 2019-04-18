import tkinter as tk    
import TigerWallet

class LoginPage(tk.Frame):
    # context = parent 
    # controller = TigerWallet object
    def __init__(self, context, controller): 
        tk.Frame.__init__(self, context)

        # break up layout into multiple sub frames 
        login_frame = tk.Frame(self)
        login_frame.pack()
        navigation_frame = tk.Frame(self) 
        navigation_frame.pack()

        
        # self.context = context
        self.controller = controller

        self.lbl = tk.Label(login_frame, text="Welcome to TigerWallet!")
        self.lbl.pack()

        self.lb2 = tk.Label(login_frame, text="Enter credentials to login!")
        self.lb2.pack()

        # get username
        user_label = tk.Label(login_frame, text="Username:", height=4)
        user_label.pack(side="left")
        self.username = tk.Entry(login_frame, width=15)
        self.username.pack(side="left")

        # get password
        password_label = tk.Label(login_frame, text="Password:", height=4)
        password_label.pack(side="left")
        self.password = tk.Entry(login_frame, width=15)
        self.password.pack(side="left")


        login_button = tk.Button(navigation_frame, text="Login", 
                                command=lambda: self.login(self.username, self.password))
        login_button.pack()

        return_button = tk.Button(navigation_frame, text="Back Home", 
                                command=lambda: controller.show_frame("HomePage"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit", 
                                command=quit)
        exit_button.pack()

        

    def login(self, username, password):
        # verify login 
        # lauch main menu
        pass 