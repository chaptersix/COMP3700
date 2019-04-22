import tkinter as tk 

class CreateAccountPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        # member username_password_map
        # store user data in user_data during execution 
        self.user_data = {}
        self.load_data()

        # break up layout into multiple sub frames 
        welcome_frame = tk.Frame(self)
        welcome_frame.pack()
        username_frame = tk.Frame(self)
        username_frame.pack()
        password_frame = tk.Frame(self)
        password_frame.pack()
        navigation_frame = tk.Frame(self) 
        navigation_frame.pack()

        # unsuccessful login notification 
        self.unsuccessful1 = tk.Label(self, text="Unsuccesful. The username you entered is already in use.")
        self.unsuccessful2 = tk.Label(self, text="Unsuccesful. Your passwords do not match.")
        # successful login notification 
        self.successful = tk.Label(self, text="Success! Your TigerWallet account has been created.\nReturn to the Home Page to login.")

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
                                command=lambda: self.verify(self.username.get(), self.password1.get(), self.password2.get()))
        create_button.pack()

        return_button = tk.Button(navigation_frame, text="Back Home", 
                                command=lambda: controller.show_frame("HomePage"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit", 
                                command=quit)
        exit_button.pack()


    def verify(self, username, password1, password2):
        """verify that the supplied username is valid"""
        # hide notifications 
        self.unsuccessful1.pack_forget()
        self.unsuccessful2.pack_forget()
        self.successful.pack_forget()
        if username in self.user_data:
            self.unsuccessful1.pack()
        elif password1 != password2:
            self.unsuccessful2.pack()
        else:
            self.write_new_user(username, password1)
            self.successful.pack()


    def write_new_user(self, username, password):
        # self.load_data()
        if username in self.user_data:
            # do nothing
            # don't write the same user data twice
            pass 
        else:
            file = open("database/user_data.dat", "a")
            file.write(username + " " + password + "\n")
            file.close()


    def load_data(self):
        # clear dictionary
        self.user_data = {}
        file = open("database/user_data.dat", "r")
        for line in file.readlines():
            line = line.split()
            print(line)
            username_in = line[0]
            password_in = line[1]
            self.user_data[username_in] = password_in
        print(self.user_data)
        file.close()