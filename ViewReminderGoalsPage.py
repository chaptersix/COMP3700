import tkinter as tk
import TigerWallet


class ViewReminderGoalsPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Your current Bill Reminder goals are listed below.")
        lbl.pack(pady=10, padx=10)

        var = tk.StringVar()
        rList_file = open("database/billReminderList.dat", "r")
        rList = rList_file.read()
        rList_file.close()
        results = tk.Label(self, text = rList)
        results.pack()

        main_menu_btn = tk.Button(self, text="Main Menu",
                                                       command=lambda: controller.show_frame("AddGoalPage"))
        main_menu_btn.pack(pady=3)

