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

        AccTo_button = tk.Button(transfer_frame, text="Account to account",
                                 command=lambda: controller.show_frame("AccountToAccountMenu"))
        AccTo_button.pack()

        pTp_button = tk.Button(transfer_frame, text="Peer to peer",
                                          command=lambda: controller.show_frame("PeerToPeer"))
        pTp_button.pack()

        contact_button = tk.Button(transfer_frame, text="Contacts",
                                   command=lambda: controller.show_frame("Contacts"))
        contact_button.pack()

        Main_Menu_button = tk.Button(transfer_frame, text="Return to Main Menu",
                                   command=lambda: controller.show_frame("MainMenu"))
        Main_Menu_button.pack()

        exit_button = tk.Button(transfer_frame, text="Exit",
                                command=quit)
        exit_button.pack()