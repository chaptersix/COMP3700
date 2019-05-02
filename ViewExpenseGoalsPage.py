import tkinter as tk


class ViewExpenseGoalsPage(tk. Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Your current Expense Goals are listed below.")
        lbl.pack(pady=10, padx=10)

        main_menu_btn = tk.Button(self, text="Main Menu", command=lambda: controller.show_frame("AddGoalPage"))
        main_menu_btn.pack(pady=5, padx=5)

        var = tk.StringVar()
        eList_file = open("database/expenseGList.dat", "r")
        eList = eList_file.read()
        eList_file.close()
        results = tk.Label(self, text = eList)
        results.pack()

