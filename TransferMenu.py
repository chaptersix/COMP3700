import tkinter as tk

class TransferMenu(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        transfer_frame = tk.Frame(self)
        transfer_frame.pack()

        label1 = tk.Label(transfer_frame, text="Select a transfer type or view contact!")
        label1.pack()

        login_button = tk.Button(transfer_frame, text="Account to account",
                                 command=lambda: controller.show_frame("AccountToAccountMenu"))
        login_button.pack()

        create_account_button = tk.Button(transfer_frame, text="Peer to peer",
                                          command=lambda: controller.show_frame("AccountToAccountMenu"))
        create_account_button.pack()

        exit_button = tk.Button(transfer_frame, text="Exit",
                                command=quit)
        exit_button.pack()