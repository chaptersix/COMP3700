import tkinter as tk    
import TigerWallet
import User

class LoginPage(tk.Frame):
    # context = parent 
    # controller = TigerWallet object
    def __init__(self, context, controller): 
        tk.Frame.__init__(self, context)

        # member username_password_map
        # store user data in user_data during execution 
        self.user_data = {}
        self.load_data()

        # break up layout into multiple sub frames 
        login_frame = tk.Frame(self)
        login_frame.pack()
        navigation_frame = tk.Frame(self)
        navigation_frame.pack()

        # unsuccessful login notification 
        self.unsuccessful = tk.Label(self, text="Unsuccesful login. Please try again.")
        # self.context = context
        self.controller = controller

        self.lbl = tk.Label(login_frame, text="Welcome to TigerWallet!")
        self.lbl.pack()

        self.lb2 = tk.Label(login_frame, text="Enter credentials to login!")
        self.lb2.pack()

        # get username
        user_label = tk.Label(login_frame, text="Username:", height=4)
        user_label.pack(side="left")
        self.username_entry = tk.Entry(login_frame, width=15)
        self.username_entry.pack(side="left")

        # get password
        password_label = tk.Label(login_frame, text="Password:", height=4)
        password_label.pack(side="left")
        self.password_entry = tk.Entry(login_frame, width=15)
        self.password_entry.pack(side="left")


        # navigation buttons
        login_button = tk.Button(navigation_frame, text="Login", 
                                command=lambda: self.login(self.username_entry.get(), self.password_entry.get()))
        login_button.pack()

        return_button = tk.Button(navigation_frame, text="Back Home", 
                                command=lambda: controller.show_frame("HomePage"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit", 
                                command=quit)
        exit_button.pack()


    def login(self, username, password):
        # verify login 
        self.load_data()
        # lauch main menu
        print(username)
        print(password)
        
        # hide notification 
        self.unsuccessful.pack_forget()
        if username in self.user_data and self.user_data[username] == password:
            # successful login 
            print("Success")
            set_current_session(username, password)
            self.controller.show_frame("MainMenu")
        else: 
            # unsuccessful login 
            print("Failure")
            self.unsuccessful.pack()
   

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

def set_current_session(username, password):
    file = open("database/current_session.dat", "w")
    file.write(username + " " + password)
    file.close()

def get_current_session():
    user_info = ["", ""]
    file = open("database/current_session.dat", "r")
    line = file.readline().split()
    print(line)
    file.close()
    user_info[0] = line[0]
    user_info[1] = line[1]
    user = User.User(user_info[0], user_info[1]) 
    print(user)
    return user
