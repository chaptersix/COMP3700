import tkinter as tk

class AccountToAccountMenu(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        aTa_frame = tk.Frame(self)
        aTa_frame.pack()
        navigation_frame = tk.Frame(self)
        navigation_frame.pack()

        self.lbl = tk.Label(aTa_frame, text="Please enter the desired 'From' and 'To' accounts!")
        self.lbl.pack()

        self.lb2 = tk.Label(aTa_frame, text="Hit submit when the account numbers have been entered!")
        self.lb2.pack()

        #get from
        from_label = tk.Label(aTa_frame, text="From:", height=4)
        from_label.pack(side="left")
        self.from_entry = tk.Entry(aTa_frame, width=15)
        self.from_entry.pack(side="left")

        #get to
        to_label = tk.Label(aTa_frame, text="To:", height=4)
        to_label.pack(side="left")
        self.to_entry = tk.Entry(aTa_frame, width=15)
        self.to_entry.pack(side="left")

        #navigation buttons
        submit_button = tk.Button(navigation_frame, text="Submit",
                                  command=lambda: self.login(self.from_entry.get(), self.to_entry.get()))
        submit_button.pack()

        return_button = tk.Button(navigation_frame, text="Back To Transfer Menu",
                                  command=lambda: controller.show_frame("TransferMenu"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit",
                                command=quit)
        exit_button.pack()
