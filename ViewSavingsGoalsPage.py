import tkinter as tk
import TigerWallet


class ViewSavingsGoalsPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Welcome to the TigerWallet Financial Goals Menu!")
        lbl.pack(pady=10, padx=10)



