import tkinter as tk 

class CreateAccountPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        # break up layout into multiple sub frames 
        welcome_frame = tk.Frame(self)
        welcome_frame.pack()
        username_frame = tk.Frame(self)
        username_frame.pack()
        password_frame = tk.Frame(self)
        password_frame.pack()
        navigation_frame = tk.Frame(self) 
        navigation_frame.pack()

        self.controller = controller

        self.lbl = tk.Label(welcome_frame, text="Create a new TigerWallet Account!")
        self.lbl.pack()

        m_text = tk.StringVar()
        m_text.set("Enter a valid username, then enter a password twice to verify.")
        self.lbl = tk.Label(welcome_frame, textvariable=m_text)
        self.lbl.pack()

        # get username
        user_label = tk.Label(username_frame, text="Username:", height=4)
        user_label.pack(side="left")
        self.username = tk.Entry(username_frame, width=15)
        self.username.pack(side="left")

        # get password
        password_label = tk.Label(password_frame, text="Password:", height=4)
        password_label.pack(side="left")
        self.password1 = tk.Entry(password_frame, width=15)
        self.password1.pack(side="left")
        self.password2 = tk.Entry(password_frame, width=15)
        self.password2.pack(side="left")

        # navigation buttons
        create_button = tk.Button(navigation_frame, text="Create", 
                                command=lambda: self.verify(self.username, self.password1, self.password2))
        create_button.pack()

        return_button = tk.Button(navigation_frame, text="Back Home", 
                                command=lambda: controller.show_frame("HomePage"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit", 
                                command=quit)
        exit_button.pack()


    def verify(self, username, password1, password2):
        """verify that the supplied username is valid"""
        pass 