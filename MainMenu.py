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

        add_bank_button = tk.Button(self, text="Manage Bank Accounts", 
                                command=lambda: controller.show_frame("ManageBankAccountPage"))
        add_bank_button.pack()

        # placeholder
        transfer_button = tk.Button(self, text="Make a Transfer", 
                                command=self.logout)
        transfer_button.pack()

        # placeholder
        financial_goals_button = tk.Button(self, text="Financial Goals", 
                                command=self.logout)
        financial_goals_button.pack()

        # placeholder
        balance_button = tk.Button(self, text="Check Balance", 
                                command=self.logout)
        balance_button.pack()

        view_accounts_button = tk.Button(self, text="View Accounts", 
                                command=self.logout)
        view_accounts_button.pack()

        logout_button = tk.Button(self, text="Log Out", 
                                command=self.logout)
        logout_button.pack()

        exit_button = tk.Button(self, text="Exit", 
                                command=quit)        
        exit_button.pack()

    # bind user to bank 
    def add_bank(self, new_bank):
        pass 

    def logout(self):
        # remove user from current session
        open('database/current_session.dat', 'w').close()
        self.controller.show_frame("HomePage")

