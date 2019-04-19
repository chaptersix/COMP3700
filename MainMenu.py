import tkinter as tk

# currently in placeholder mode
class MainMenu(tk.Frame):
    # context = parent 
    # controller = TigerWallet object
    def __init__(self, context, controller): 
        tk.Frame.__init__(self, context)

        # self.context = context
        self.controller = controller

        label1 = tk.Label(self, text="You have been logged in!")
        label1.pack()

        login_button = tk.Button(self, text="Login", 
                                command=lambda: controller.show_frame("LoginPage"))
        login_button.pack()

        create_account_button = tk.Button(self, text="Create Account", 
                                command=lambda: controller.show_frame("CreateAccountPage"))
        create_account_button.pack()

        exit_button = tk.Button(self, text="Exit", 
                                command=quit)        
        exit_button.pack()
