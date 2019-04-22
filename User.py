

class User():
    def __init__(self, username_in, password_in):
        self.username = username_in
        self.password = password_in
        self.bank = ""
        self.contacts = [] 
        self.bank_accounts = [] 

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_contacts(self):
        return self.contacts
    
    def get_bank_accounts(self):
        return self.bank_accounts

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_password):
        self.password = new_password

    def set_bank(self, new_bank):
        self.bank = new_bank

    def add_bank_account(self, new_account):
        self.bank_accounts.append(new_account)
    
        