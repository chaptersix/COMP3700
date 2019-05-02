import tkinter as tk

class PeerToPeer(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        pTp_frame = tk.Frame(self)
        pTp_frame.pack()
        navigation_frame = tk.Frame(self)
        navigation_frame.pack()

        self.lbl = tk.Label(pTp_frame, text="Please enter the desired 'From' account and User to transfer to!")
        self.lbl.pack()

        self.lb2 = tk.Label(pTp_frame, text="Hit submit when the info has been entered!")
        self.lb2.pack()

        # get from
        home_label = tk.Label(pTp_frame, text="Home Account:", height=4)
        home_label.pack(side="left")
        self.home_entry = tk.Entry(pTp_frame, width=15)
        self.home_entry.pack(side="left")

        # get to
        to_label = tk.Label(pTp_frame, text="User:", height=4)
        to_label.pack(side="left")
        self.to_entry = tk.Entry(pTp_frame, width=15)
        self.to_entry.pack(side="left")

        submit_button = tk.Button(navigation_frame, text="Submit",
                                  command=lambda: self.login(self.home_entry.get(), self.to_entry.get()))
        submit_button.pack()

        return_button = tk.Button(navigation_frame, text="Back To Transfer Menu",
                                  command=lambda: controller.show_frame("TransferMenu"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit",
                                command=quit)
        exit_button.pack()

