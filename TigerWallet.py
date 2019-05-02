import tkinter as tk 
import HomePage as hp
import LoginPage as lp
import CreateAccountPage as cap
import MainMenu as mm
import ManageBankAccountPage as mbap
import AddBankAccountPage as abap
import RemoveBankAccountPage as rbap
import AccountSelectionMenu as asm
import CheckingAccountsMenu as cam
import SavingsAccountsMenu as sam
import AddGoalPage as agp
import SelectTypePage as stp
import NewExpenseGoal as neg
import NewSavingsGoal as nsg
import NewBillReminder as nbr
import TransferMenu as tm
import AccountToAccountMenu as ata
import Contacts as con
import PeerToPeer as ptp


# Each TigerWallet instance inherits tk.  
# Primary interface controller.
class TigerWallet(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set window title 
        self.title("TigerWallet")

        # container to "stack" frames 
        container = tk.Frame(self)
        # refine with args later
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # tuple containing all active pages 
        page_list = (hp.HomePage, lp.LoginPage, cap.CreateAccountPage, mm.MainMenu, mbap.ManageBankAccountPage, abap.AddBankAccountPage
                    ,rbap.RemoveBankAccountPage, asm.AccountSelectionMenu, cam.CheckingAccountsMenu,sam.SavingsAccountsMenu, agp.AddGoalPage
                    ,stp.SelectTypePage, neg.NewExpenseGoal, nsg.NewSavingsGoal, nbr.NewBillReminder, tm.TransferMenu
                    , ata.AccountToAccountMenu, con.Contacts, ptp.PeerToPeer)
        # dictionary mapping frames to the corresponding page names
        self.frames = {}
        # add additional pages to this tuple
        for F in page_list:
            page_name = F.__name__
            frame = F(context=container, controller=self)
            self.frames[page_name] = frame
            # ensures frames are placed in the same location 
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        # return a given frame from self.frames 
        frame = self.frames[page_name]
        frame.tkraise()





if __name__ == "__main__":
    tw = TigerWallet()
    tw.mainloop()