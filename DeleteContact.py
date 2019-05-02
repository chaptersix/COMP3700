import tkinter as tk

class DeleteContact(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        added_frame = tk.Frame(self)
        added_frame.pack()

        self.lbl = tk.Label(added_frame, text="Contact has been deleted!")
        self.lbl.pack()

        return_button = tk.Button(added_frame, text="Back To Transfer Menu",
                                  command=lambda: controller.show_frame("TransferMenu"))
        return_button.pack()

        exit_button = tk.Button(added_frame, text="Exit",
                                command=quit)
        exit_button.pack()