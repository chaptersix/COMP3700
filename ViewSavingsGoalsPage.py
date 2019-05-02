import tkinter as tk
import TigerWallet


class ViewSavingsGoalsPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Your current savings goal are listed below.")
        lbl.pack(pady=10, padx=10)

        var = tk.StringVar()
        sList_file = open("database/savingsGList.dat.", "r")
        sList = sList_file.read()
        sList_file.close()
        results = tk.Label(self, text = sList)
        results.pack()

        main_menu_btn = tk.Button(self, text="Main Menu", command=lambda: controller.show_frame("AddGoalPage"))
        main_menu_btn.pack(pady=5, padx=5)




