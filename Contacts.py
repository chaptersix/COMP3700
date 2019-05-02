import tkinter as tk

class Contacts(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        contacts_frame = tk.Frame(self)
        contacts_frame.pack()
        navigation_frame = tk.Frame(self)
        navigation_frame.pack()

        label1 = tk.Label(contacts_frame, text="Contact list: view, add, remove!")
        label1.pack()


        #add contact
        user_label = tk.Label(contacts_frame, text="Enter username:", height=4)
        user_label.pack(side="left")
        self.add_entry = tk.Entry(contacts_frame, width=15)
        self.add_entry.pack(side="left")
        add_button = tk.Button(contacts_frame, text="Add")
        add_button.pack(side="left")
        delete_button = tk.Button(contacts_frame, text="Delete")
        delete_button.pack(side ="left")

        login_button = tk.Button(navigation_frame, text="View Contacts",
                                 command=lambda: controller.show_frame("AccountToAccountMenu"))
        login_button.pack()

        return_button = tk.Button(navigation_frame, text="Return to Transfer Menu",
                                  command=lambda: controller.show_frame("TransferMenu"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit",
                                command=quit)
        exit_button.pack()